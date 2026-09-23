#!/usr/bin/env bash
# Test migration + RLS + apply_changes trên Postgres thường (không cần Supabase).
# Dùng: PGHOST=... PGPORT=... PGUSER=postgres supabase/tests/db_test.sh
set -e
cd "$(dirname "$0")"
DB=nn_test_$$
createdb "$DB"
trap 'dropdb --if-exists "$DB"' EXIT
psql -q -v ON_ERROR_STOP=1 -d "$DB" -f auth_stub.sql >/dev/null
for f in ../migrations/*.sql; do psql -q -v ON_ERROR_STOP=1 -d "$DB" -f "$f" >/dev/null; done
psql -q -v ON_ERROR_STOP=1 -d "$DB" -f db.test.sql | tail -1 | tee /dev/stderr | grep -q 'ALL DB TESTS PASSED'
psql -q -v ON_ERROR_STOP=1 -d "$DB" -f db2.test.sql | tail -1 | tee /dev/stderr | grep -q 'ALL DB2 TESTS PASSED'
