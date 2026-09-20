#!/usr/bin/env bash
# Chạy toàn bộ test mobile: server tĩnh tạm + a/b/c. Cần Node ≥18 và `npm i -D playwright` (hoặc PLAYWRIGHT_MODULE trỏ tới bản cài sẵn).
set -e
cd "$(dirname "$0")/.."
PORT=${PORT:-8765}
python3 -m http.server $PORT >/dev/null 2>&1 & SRV=$!
trap "kill $SRV" EXIT
sleep 1
export BASE_URL="http://localhost:$PORT/"
for t in tests/a.mjs tests/b.mjs tests/c.mjs tests/d.mjs tests/e.mjs; do echo "== $t"; node "$t"; done
