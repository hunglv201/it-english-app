#!/usr/bin/env bash
# Đẩy code lên GitHub bằng token trong .env. Dùng: ./push.sh "commit message"
set -e
cd "$(dirname "$0")"
[ -f .env ] || { echo "Thiếu .env — copy từ .env.example rồi điền GITHUB_TOKEN"; exit 1; }
set -a; . ./.env; set +a
BR="$(git rev-parse --abbrev-ref HEAD)"
if [ -n "$1" ]; then git add -A && git commit -m "$1"; fi
git push "https://x-access-token:${GITHUB_TOKEN}@github.com/${GITHUB_REPO}.git" "${BR}:${BR}"
echo "Đã push nhánh ${BR}."
