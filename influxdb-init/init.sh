#!/bin/bash
set -e

echo "InfluxDB init container starting..."

: "${INFLUX_HOST:=http://influxdb:8086}"
: "${INFLUXDB_ORG:?INFLUXDB_ORG is required}"
: "${INFLUX_TOKEN:?INFLUXDB_ADMIN_TOKEN is required}"
: "${INFLUXDB_BUCKETS:?INFLUXDB_BUCKETS is required (e.g. docker,system,metrics)}"

export INFLUX_TOKEN

echo "Waiting for InfluxDB at $INFLUX_HOST..."

until influx ping --host "$INFLUX_HOST" >/dev/null 2>&1; do
  echo "InfluxDB not ready yet..."
  sleep 3
done

echo "InfluxDB is ready. Creating buckets..."

create_bucket () {
  NAME="$1"

  if influx bucket list --host "$INFLUX_HOST" --org "$INFLUXDB_ORG" | grep -w "$NAME"; then
    echo "Bucket '$NAME' already exists"
    return
  fi

  echo "Creating bucket: $NAME"

  influx bucket create \
    --host "$INFLUX_HOST" \
    --org "$INFLUXDB_ORG" \
    --name "$NAME"
}

for bucket in ${INFLUXDB_BUCKETS//,/ }; do
  [ -z "$bucket" ] && continue
  create_bucket "$bucket"
done

echo "All buckets created successfully."
