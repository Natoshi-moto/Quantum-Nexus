#!/usr/bin/env bash
set -euo pipefail

die() {
  printf 'NO_LEAK BLOCKED: %s\n' "$1" >&2
  exit 1
}

info() {
  printf 'NO_LEAK: %s\n' "$1"
}

normalize_origin() {
  local value="$1"
  case "$value" in
    https://github.com/*) value="${value#https://github.com/}" ;;
    http://github.com/*) value="${value#http://github.com/}" ;;
    git@github.com:*) value="${value#git@github.com:}" ;;
    ssh://git@github.com/*) value="${value#ssh://git@github.com/}" ;;
  esac
  value="${value%.git}"
  printf '%s' "$value"
}

repo_root="$(git rev-parse --show-toplevel 2>/dev/null)" || die 'not inside a Git checkout'
repo_root="$(realpath -- "$repo_root")"
vault="$repo_root/.codex/NO_LEAK_VAULT"

[[ -f "$vault" ]] || die '.codex/NO_LEAK_VAULT is missing; copy and edit NO_LEAK_VAULT.example'
[[ ! -L "$vault" ]] || die 'the vault must be a regular file, not a symlink'

version=''
expected_origin=''
dump_root=''
configured_repo_root=''
max_staged_file_bytes='5242880'
declare -a no_export_paths=()
declare -a no_export_sha256=()
declare -a deny_repo_paths=()

while IFS= read -r line || [[ -n "$line" ]]; do
  line="${line%$'\r'}"
  [[ -z "$line" || "$line" == \#* ]] && continue
  [[ "$line" == *=* ]] || die 'vault contains a non-comment line without ='
  key="${line%%=*}"
  value="${line#*=}"
  [[ -n "$value" ]] || die "vault key $key has an empty value"
  case "$key" in
    VERSION) version="$value" ;;
    EXPECTED_ORIGIN) expected_origin="$value" ;;
    DUMP_ROOT) dump_root="$value" ;;
    REPO_ROOT) configured_repo_root="$value" ;;
    MAX_STAGED_FILE_BYTES) max_staged_file_bytes="$value" ;;
    NO_EXPORT_PATH) no_export_paths+=("$value") ;;
    NO_EXPORT_SHA256) no_export_sha256+=("${value,,}") ;;
    DENY_REPO_PATH) deny_repo_paths+=("$value") ;;
    *) die "unknown vault key: $key" ;;
  esac
done < "$vault"

[[ "$version" == '1' ]] || die 'vault VERSION must be 1'
[[ -n "$expected_origin" && -n "$dump_root" && -n "$configured_repo_root" ]] || die 'vault is missing a required setting'
[[ "$max_staged_file_bytes" =~ ^[0-9]+$ ]] || die 'MAX_STAGED_FILE_BYTES must be an integer'

dump_root="$(realpath -- "$dump_root")"
configured_repo_root="$(realpath -- "$configured_repo_root")"
[[ "$repo_root" == "$configured_repo_root" ]] || die 'current Git root does not match REPO_ROOT'
[[ "$repo_root" != "$dump_root" ]] || die 'the writable Git checkout cannot be the outer dump itself'
case "$repo_root/" in
  "$dump_root/"*) ;;
  *) die 'REPO_ROOT is not nested inside DUMP_ROOT' ;;
esac

actual_origin="$(git remote get-url origin 2>/dev/null)" || die 'Git remote origin is missing'
[[ "$(normalize_origin "$actual_origin")" == "$(normalize_origin "$expected_origin")" ]] || die 'origin is not the expected Quantum-Nexus repository'

for digest in "${no_export_sha256[@]}"; do
  [[ "$digest" =~ ^[0-9a-f]{64}$ ]] || die 'NO_EXPORT_SHA256 must be 64 lowercase hexadecimal characters'
done
[[ ${#no_export_paths[@]} -gt 0 || ${#no_export_sha256[@]} -gt 0 ]] || die 'vault must define at least one NO_EXPORT_PATH or NO_EXPORT_SHA256'

if [[ "${1:-}" == '--config-only' ]]; then
  info 'vault, repository root, dump nesting, and origin are valid'
  exit 0
fi
[[ $# -eq 0 || "${1:-}" == '--staged' ]] || die 'usage: no_leak_guard.sh [--config-only|--staged]'

mapfile -d '' staged_paths < <(git diff --cached --name-only -z --diff-filter=ACMR)
[[ ${#staged_paths[@]} -gt 0 ]] || die 'nothing is staged'

declare -A protected_hashes=()
for digest in "${no_export_sha256[@]}"; do
  protected_hashes["$digest"]=1
done

for relative in "${no_export_paths[@]}"; do
  [[ "$relative" != /* ]] || die 'NO_EXPORT_PATH values must be relative to DUMP_ROOT'
  protected="$(realpath -m -- "$dump_root/$relative")"
  case "$protected" in
    "$dump_root"|"$dump_root/"*) ;;
    *) die 'NO_EXPORT_PATH escapes DUMP_ROOT' ;;
  esac
  [[ -e "$protected" ]] || die 'a configured NO_EXPORT_PATH does not exist'
  if [[ -f "$protected" && ! -L "$protected" ]]; then
    digest="$(sha256sum -- "$protected" | awk '{print $1}')"
    protected_hashes["$digest"]=1
  elif [[ -d "$protected" && ! -L "$protected" ]]; then
    while IFS= read -r -d '' source_file; do
      digest="$(sha256sum -- "$source_file" | awk '{print $1}')"
      protected_hashes["$digest"]=1
    done < <(find -P "$protected" -type f -print0)
  else
    die 'NO_EXPORT_PATH must name a regular file or directory, not a symlink'
  fi
done

always_deny=(
  '.codex/NO_LEAK_VAULT'
  '.codex/NO_LEAK_VAULT.*'
  '.codex/local-runs/*'
  '.env'
  '.env.*'
  '*.pem'
  '*.key'
  '*.p12'
  '*.pfx'
  'local-dump/*'
)
deny_repo_paths+=("${always_deny[@]}")

secret_pattern='AKIA[0-9A-Z]{16}|-----BEGIN ([A-Z ]+ )?PRIVATE KEY-----|(^|[^A-Za-z0-9])sk-[A-Za-z0-9_-]{20,}|gh[pousr]_[A-Za-z0-9]{20,}|github_pat_[A-Za-z0-9_]{20,}|xox[baprs]-[A-Za-z0-9-]{10,}'

for path in "${staged_paths[@]}"; do
  [[ "$path" != /* ]] || die 'an absolute path is staged'
  resolved="$(realpath -m -- "$repo_root/$path")"
  case "$resolved" in
    "$repo_root/"*) ;;
    *) die 'a staged path escapes the nested repository' ;;
  esac

  for pattern in "${deny_repo_paths[@]}"; do
    if [[ "$path" == $pattern ]]; then
      die 'a staged path matches a NO_LEAK deny rule'
    fi
  done

  mode="$(git ls-files -s -- "$path" | awk 'NR==1 {print $1}')"
  [[ "$mode" != '120000' ]] || die 'staged symlinks are forbidden'
  [[ "$mode" != '160000' ]] || die 'staged submodules are forbidden'

  size="$(git cat-file -s ":$path")"
  [[ "$size" -le "$max_staged_file_bytes" ]] || die 'a staged file exceeds MAX_STAGED_FILE_BYTES'

  digest="$(git show ":$path" | sha256sum | awk '{print $1}')"
  [[ -z "${protected_hashes[$digest]:-}" ]] || die 'a staged file exactly matches protected dump content'

  if git show ":$path" | LC_ALL=C grep -Eaq "$secret_pattern"; then
    die 'a staged file matches an obvious credential or private-key pattern'
  fi
done

git diff --cached --check >/dev/null || die 'staged diff fails whitespace/error checks'
info "passed for ${#staged_paths[@]} staged file(s); no protected content was printed"


