# Databricks API Proxy

Workaround when your platform doesn't pass Bearer token to Custom Integration tools at runtime.

## Setup

1. **Set env var:** `DATABRICKS_PAT=your-databricks-token`

2. **Deploy** to one of:
   - **Railway**: `railway up` (or connect GitHub)
   - **Render**: Connect repo, add DATABRICKS_PAT env var
   - **Fly.io**: `fly launch` then `fly secrets set DATABRICKS_PAT=...`
   - **Local**: `pip install -r requirements.txt && python app.py`

3. **Update Custom Integration:**
   - Change **Server URL** from `https://dbc-0ac47e01-4f99.cloud.databricks.com`
   - To: `https://YOUR-PROXY-URL.railway.app` (or your deployed URL)
   - **Remove/disable** Bearer auth in the integration (proxy adds the token)

4. **Test:**
   ```bash
   curl "https://YOUR-PROXY-URL/api/2.1/jobs/runs/get?run_id=1097080613263872"
   ```
   Should return Databricks response (no auth needed in request).
