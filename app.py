"""
Databricks API Proxy - Run locally + ngrok for bot builder integration.
Usage: DATABRICKS_PAT='your-token' python app.py
"""
import os
import requests
from flask import Flask, request, jsonify

app = Flask(__name__)
BASE_URL = "https://dbc-0ac47e01-4f99.cloud.databricks.com"

# Job Run Failure Note
# ------------------------------------------------------
# Job ID: 320196133
# Run ID: 1081458907530444
#Cause: Task run1 failed; requires farther investigation
