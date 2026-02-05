# Deploy Databricks Proxy to Render

## Step 1: Push to GitHub

1. Create a new repo on GitHub (e.g. `databricks-sre-proxy`)
2. From your terminal:

```bash
cd /Users/akshithaboreddyreddy/databricks-proxy
git init
git add .
git commit -m "Databricks proxy for SRE agent"
git branch -M main
git remote add origin https://github.com/YOUR_USERNAME/databricks-sre-proxy.git
git push -u origin main
```

---

## Step 2: Deploy on Render

1. Go to **[render.com](https://render.com)** and sign up / log in
2. Click **New +** → **Web Service**
3. Connect your GitHub and select the `databricks-proxy` repo
4. Configure:
   - **Name:** `databricks-proxy`
   - **Region:** Oregon (or nearest to you)
   - **Root Directory:** Leave blank if the repo root has app.py. If you pushed only the databricks-proxy folder as the repo root, leave blank.
   - **Runtime:** Python 3
   - **Build Command:** `pip install -r requirements.txt`
   - **Start Command:** `gunicorn app:app --bind 0.0.0.0:$PORT`
5. Click **Advanced** → **Add Environment Variable**
   - **Key:** `DATABRICKS_PAT`
   - **Value:** Your Databricks token (paste it)
6. Click **Create Web Service**
7. Wait 2–3 minutes for the deploy to finish

---

## Step 3: Get Your URL

When deploy is done, you’ll see a URL like:

```
https://databricks-proxy-xxxx.onrender.com
```

Copy it.

---

## Step 4: Update Custom Integration

1. **Custom Integrations** → **Edit databricks_jobs_tools**
2. **Server URL:** `https://databricks-proxy-xxxx.onrender.com` (paste your URL, no trailing slash)
3. **Authentication:** Remove or leave empty (proxy adds the token)
4. Save

---

## Step 5: Test

```bash
curl "https://YOUR-URL.onrender.com/health"
curl "https://YOUR-URL.onrender.com/api/2.1/jobs/runs/get?run_id=1097080613263872"
```

Then run a test from the bot builder.

---

## If Repo Root Is Your Whole Project

If your GitHub repo is a parent folder and `databricks-proxy` is inside it:

- Set **Root Directory** to `databricks-proxy` in Render.
