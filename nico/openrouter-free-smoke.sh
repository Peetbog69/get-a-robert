#!/usr/bin/env bash
set -euo pipefail

if [[ -z "${OPENROUTER_API_KEY:-}" ]]; then
  echo "OPENROUTER_API_KEY is not set."
  echo "Export a key, then rerun this script."
  exit 2
fi

prompt="${1:-Reply with NICO_OPENROUTER_OK and nothing else.}"

models=(
  "qwen/qwen3-coder:free"
  "moonshotai/kimi-k2.6:free"
  "nvidia/nemotron-3-ultra-550b-a55b:free"
  "nvidia/nemotron-3-super-120b-a12b:free"
  "openai/gpt-oss-120b:free"
  "openai/gpt-oss-20b:free"
  "meta-llama/llama-3.3-70b-instruct:free"
  "nousresearch/hermes-3-llama-3.1-405b:free"
  "openrouter/free"
)

echo "Current OpenRouter free models with tool support:"
curl -fsS https://openrouter.ai/api/v1/models |
  jq -r '.data[]
    | select(((.id|endswith(":free")) or (.pricing.prompt == "0" and .pricing.completion == "0"))
        and ((.supported_parameters // []) | index("tools")))
    | "- \(.id) ctx=\(.context_length)"' |
  sed -n '1,80p'

echo
echo "Smoke testing candidates..."
for model in "${models[@]}"; do
  printf "\n== %s ==\n" "$model"
  response="$(
    jq -n --arg model "$model" --arg prompt "$prompt" '{
      model: $model,
      messages: [{role: "user", content: $prompt}],
      max_tokens: 32,
      temperature: 0
    }' |
      curl -fsS https://openrouter.ai/api/v1/chat/completions \
        -H "Authorization: Bearer ${OPENROUTER_API_KEY}" \
        -H "Content-Type: application/json" \
        -H "HTTP-Referer: https://openclaw.local/nico" \
        -H "X-Title: Nico OpenRouter Smoke Test" \
        --data-binary @- 2>&1
  )" || {
    echo "$response" | sed -E 's/sk-or-[A-Za-z0-9_-]+/sk-or-<redacted>/g'
    continue
  }

  echo "$response" | jq -r '.choices[0].message.content // .error.message // .'
done
