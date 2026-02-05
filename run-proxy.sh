#!/bin/bash
# Run the Databricks proxy locally, then expose with ngrok

cd "$(dirname "$0")"

if [ -z "$DATABRICKS_PAT" ]; then
  echo "Set DATABRICKS_PAT first:"
  echo "  export DATABRICKS_PAT='dapi...'"
  exit 1
fi

echo "Starting proxy on port 5000..."
echo "In another terminal run: ngrok http 5000"
echo "Then update Custom Integration Server URL to the ngrok URL"
echo ""

python3 app.py
