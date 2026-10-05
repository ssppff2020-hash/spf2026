#!/usr/bin/env bash
# C1 pipeline · step 1 — acquire the course materials.
#
# Two acquisition paths, in order of preference:
#   A. use the offline cache that ships with the challenge pack (already local);
#   B. fill the holes the cache left, by re-fetching live.
#
# Path B is what this script does. It is deliberately plain curl + jq-free
# parsing so it re-runs anywhere with bash and python3.
#
# Usage:  bash 01_fetch.sh [out_dir]        (default: ./live)
set -uo pipefail

OUT="${1:-./live}"
mkdir -p "$OUT"
UA="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0 Safari/537.36"

say() { printf '[fetch] %s\n' "$*"; }

# ---------------------------------------------------------------------------
# A. Did the offline cache already give us everything? The challenge pack's
#    CS146S_offline.zip covers 31 article pages + 3 PDFs. Four of those are
#    unusable (gated, JS-only, or blocked), so we re-fetch below.
# ---------------------------------------------------------------------------

say "=== Re-fetching items the offline cache could not capture ==="

# ---------------------------------------------------------------------------
# B1. Plain HTML pages.  Note: some hosts are unreachable from a locked-down
#     network. Record the failure instead of dying — step 2 tolerates holes.
# ---------------------------------------------------------------------------
fetch_html() {  # fetch_html <name> <url>
  local name="$1" url="$2"
  if timeout 45 curl -sSL -A "$UA" -o "$OUT/$name" -w '%{http_code}' "$url" 2>/dev/null | grep -q '^200$'; then
    say "ok       $name  ($(wc -c < "$OUT/$name") bytes)"
  else
    say "FAILED   $name  <- $url"
    printf '%s\t%s\tunreachable\n' "$name" "$url" >> "$OUT/_failures.tsv"
  fi
}

fetch_html "peeking-medium.html" \
  "https://medium.com/@outsightai/peeking-under-the-hood-of-claude-code-70f5a94a9a62"
fetch_html "good-context-stockapp.html" \
  "https://blog.stockapp.com/good-context-good-code/"

# ---------------------------------------------------------------------------
# B2. Notion-backed pages return an empty JS shell to curl. The public page
#     data lives behind Notion's own loadPageChunk endpoint, so POST to that
#     directly and parse the recordMap in 02_extract's sibling script.
#     Page id = last 32 hex chars of the notion.site URL, dash-formatted.
# ---------------------------------------------------------------------------
notion_fetch() {  # notion_fetch <out.json> <page_id_dashed>
  local out="$1" pid="$2"
  timeout 45 curl -sS -X POST "https://notion.warp.dev/api/v3/loadPageChunk" \
    -H 'Content-Type: application/json' -A "$UA" \
    -d "{\"pageId\":\"$pid\",\"limit\":100,\"cursor\":{\"stack\":[]},\"chunkNumber\":0,\"verticalColumns\":false}" \
    -o "$out" && say "ok       $out  ($(wc -c < "$out") bytes)"
}

notion_fetch "$OUT/notion-chunk.json" "21643263-616d-81a6-b9e3-e63fd8a7380c"

# ---------------------------------------------------------------------------
# B3. Talk transcript standing in for a video we cannot download.
# ---------------------------------------------------------------------------
fetch_html "lessons-transcript.html" "https://lawwu.github.io/transcripts/TswQeKftnaw.html"

# ---------------------------------------------------------------------------
# B4. Wrong-page repair.
#
#     The pack's offline cache captured the WRONG document for two readings,
#     because the crawler followed redirects. Same failure mode as B2 (HTTP 200,
#     plausible-looking text, wrong content) — so it is only caught by *reading
#     the source*, not by any status code.
#
#       Week 4 "Claude Best Practices"
#         syllabus links anthropic.com/engineering/claude-code-best-practices
#         -> 302 -> code.claude.com/docs/en/best-practices
#         cached copy is the docs *Overview* page, not the article. Re-fetch it.
#
#     Week 6 "OWASP Top Ten" was checked too and is NOT a defect: the cache
#     holds the same landing page the syllabus links to (the A01..A10 items live
#     on sub-pages). Left as-is deliberately — see C1/pipeline/qa_adjudication.md.
# ---------------------------------------------------------------------------
fetch_html "best-practices.html" "https://code.claude.com/docs/en/best-practices"

say "=== done. failures (if any) are in $OUT/_failures.tsv ==="
