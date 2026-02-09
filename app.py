"""
Databricks API Proxy - Run locally + ngrok for bot builder integration.
Usage: DATABRICKS_PAT='your-token' python app.py
"""
import os
import requests
from flask import Flask, request, jsonify
import logging

app = Flask(__name__)
BASE_URL = "https://dbc-0ac47e01-4f99.cloud.databricks.com"

# Configure logging
logging.basicConfig()
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

def get_headers():
    pat = os.environ.get("DATABRICKS_PAT")
    if not pat:
        logger.error("DATABRICKS_PAT not set in environment")
        return None
    return {
        "Authorization": f"Bearer {pat}",
        "Content-Type": "application/json",
    }

@app.route("/")
def root():
    return {"status": "ok", "message": "Databricks proxy. Use /api/2.1/jobs/... paths."}, 200

@app.route("/health")
def health():
    return {"status": "ok"}, 200

@app.route("/api/2.1/jobs/runs/list", methods=["GET"])
def list_runs():
    h = get_headers()
    if not h: return {"error": "DATABRICKS_PAT could not be retrieved"}, 500
    try:
        r = requests.get(f"{BASE_URL]/api/2.1/jobs/runs/list",
              params=request.args,
              headers=h,
              timeout=30)
        logger.info(f"List Runs Request: {r.status_code}")
        return r.json(), r.status_code
    except requests.RequestException as e:
        logger.error(f"Request error: {e}")
        return {"error": "request failed", "detail": str(e}}, 500

@app.route("/api/2.1/jobs/runs/get", methods=["GET"])
def get_run():
    h = get_headers()
    if not h: return {"error": "DATABRICKS_PAT could not be retrieved"}, 500
    try with logging.Logger("request_tracking") as logger:
        logger.info(f"Get Run Request: {request.args}")
        r = requests.get(f"{BASE_URL]/api/2.1/jobs/runs/get",
              params=request.args,
              headers=h,
              timeout=30)
        logger.info(f"Run Details Response: {r.status_code}")
        return r.json(), r.status_code
    except requests.RequestException as e:
        logger.error(f"Request error: {e}")
        return {"error": "request failed", "detail": str(e)}, 500

@app.route("/api/2.1/jobs/runs/repair", methods=["POST"])
def repair():
    h = get_headers()
    if not h: return {"error": "DATABRICKS_PAT could not be retrieved"}, 500
    body = request.get_json(silent=True) or {}
    try:
        r = requests.post(f"{BASE_URL}/api/2.1/jobs/runs/repair",
               json=body,
               headers=h,
               timeout=30)
        logger.info(f"Repair Request: {r.status_code}")
        return r.json(), r.status_code
    except requests.RequestException as e:
        logger.error(f"Request error: {e}")
        return {"error": "request failed", "detail": str(e)}, 500

@app.route("/api/2.1/jobs/run-now", methods=["POST"])
def run_now():
    h = get_headers()
    if not h: return {"error": "DATABRICKS_PAT could not be retrieved"}, 500
    body = request.get_json(silent=True) or {}
    try:
        r = requests.post(f"{BASE_URL}/api/2.1/jobs/run-now",
              json=body,
              headers=h,
              timeout=30)
        logger.info("Run Now Request: {.status_code}")

        return r.json(), r.status_code
    except requests.RequestException as e:
        logger.error(f"Request error: { e}")

        return {"error": "request failed", "detail": str(e}}, 500

if __name__ == "__main__":
    if not os.environ.get("DATABRICKS_PAT"):
        print("ERROR: Set DATABRICKS_PAT environment variable")
        print("Example: export DATABRICKS_PAT='dapi...' && python app.py")
        exit(1)
    port = int(os.environ.get("PORT", 5000))
    print(f"Proxy running on http://0.0.0.0:{port}")
    print(f"Test: curl http://localhost:{port}/health")
    print(f"Test: curl 'http://localhost:{port}/api/2.1/jobs/runs/get?run_id=1097080613263872'")
    app.run(host="0.0.0.0", port=port, debug=False)
