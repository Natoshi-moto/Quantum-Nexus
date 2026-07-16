#!/usr/bin/env bash
set -euo pipefail

repo_root="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")/.." && pwd)"
guard="$repo_root/.codex/no_leak_guard.sh"
pattern="$(sed -n "s/^secret_pattern='\\(.*\\)'$/\\1/p" "$guard")"
[[ -n "$pattern" ]] || {
  printf 'FAIL: secret pattern could not be extracted\n' >&2
  exit 1
}

matches() {
  printf '%s\n' "$1" | LC_ALL=C grep -Eaq "$pattern"
}

expect_match() {
  local label="$1"
  local candidate="$2"
  if ! matches "$candidate"; then
    printf 'FAIL: expected match: %s\n' "$label" >&2
    exit 1
  fi
}

expect_no_match() {
  local label="$1"
  local candidate="$2"
  if matches "$candidate"; then
    printf 'FAIL: unexpected match: %s\n' "$label" >&2
    exit 1
  fi
}

twenty="$(printf 'A%.0s' {1..20})"
nineteen="$(printf 'A%.0s' {1..19})"
openai_token="s""k-$twenty"
short_openai="s""k-$nineteen"
aws_token="AK""IA$(printf 'A%.0s' {1..16})"
pem_header="-----BEGIN ""PRIVATE KEY-----"
github_classic="gh""p_$(printf 'A%.0s' {1..20})"
github_fine="github_""pat_$(printf 'A%.0s' {1..20})"
slack_token="xo""xb-$(printf 'A%.0s' {1..10})"

expect_match 'standalone OpenAI shape' "$openai_token"
expect_match 'space-prefixed OpenAI shape' " $openai_token"
expect_match 'quote-prefixed OpenAI shape' "\"$openai_token"
expect_match 'equals-prefixed OpenAI shape' "=$openai_token"
expect_match 'slash-prefixed OpenAI shape' "/$openai_token"
expect_match 'underscore-prefixed OpenAI shape' "_$openai_token"
expect_match 'AWS shape unchanged' "$aws_token"
expect_match 'PEM header unchanged' "$pem_header"
expect_match 'GitHub classic shape unchanged' "$github_classic"
expect_match 'GitHub fine-grained shape unchanged' "$github_fine"
expect_match 'Slack shape unchanged' "$slack_token"

expect_no_match 'task branch name' 'task-0009-codex-cross-provider-review-and-implementation'
expect_no_match 'risk identifier' 'risk-0000000000000000000000000000'
expect_no_match 'short OpenAI shape' "$short_openai"
expect_no_match 'ordinary task prose' 'ordinary prose about task-handling and review'

printf 'PASS: secret-pattern boundary regression\n'


