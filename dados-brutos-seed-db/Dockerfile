FROM postgres:12 as db_bruno
WORKDIR /app
COPY ./scripts/db_bruno/init.sh /docker-entrypoint-initdb.d/
COPY ./scripts/db_bruno/dump.sql ./scripts/db/dump.sql