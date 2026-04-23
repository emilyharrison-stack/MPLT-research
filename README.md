# MPLT Research Dashboard

An interactive dashboard for comparing Wall Street analyst reports on Maplight Therapeutics. View report summaries by publisher, compare specific metrics across analysts, and spot where analysts disagree.

---

## How to Open the Dashboard (One-Time Setup)

No downloads or installation needed. The dashboard runs as a website through Streamlit Community Cloud (free).

### Step 1: Go to Streamlit Cloud

Open your browser and go to: **https://share.streamlit.io**

### Step 2: Sign in with GitHub

Click **"Sign in with GitHub"** and log in with your GitHub account (the same one that has access to this repo).

If you don't have a Streamlit Cloud account yet, it will create one automatically when you sign in with GitHub.

### Step 3: Deploy the app

Once you're signed in, click the **"New app"** button (top right corner). You'll see a form — fill it in like this:

- **Repository**: `emilyharrison-stack/MPLT-research`
- **Branch**: `claude/research-dashboard-1EZfh`
- **Main file path**: `app.py`

Then click **"Deploy!"**

### Step 4: Wait about 1 minute

Streamlit will install everything and start the dashboard. You'll see a loading screen, then the dashboard will appear.

### Step 5: Bookmark it

Once it's running, you'll have a URL like `https://emilyharrison-stack-mplt-research-app-xxxxx.streamlit.app`. Bookmark this — you can come back to it anytime. Share the link with teammates and they can use it too.

---

## Using the Dashboard

Once the dashboard is open in your browser, use the **left sidebar** to switch between views:

### Overview
A snapshot of all analyst coverage — ratings, price targets, and key themes at a glance.

### Publisher Summary
Pick a bank (Morgan Stanley, Goldman Sachs, etc.) and see everything from their report: investment thesis, key themes, notable quotes, and all their forecasts compared to what other analysts think.

### Metric Comparison
Pick a specific number (like "Schizophrenia Peak Sales" or "2030 EPS") and see how every analyst compares side-by-side. Includes bar charts, trend lines, and automatic outlier detection.

### Inconsistency Detector
Automatically finds where analysts disagree the most — conflicting price targets, different launch timelines, wide gaps in sales estimates. Ranked by severity so you can focus on the biggest debates.

### Competitor Mentions
Shows how analysts covering BMS, Neurocrine, and Acadia are talking about Maplight in their reports.

---

## Adding Your Real Data

Right now the dashboard uses sample data. To swap in your real analyst reports:

### How to upload files through GitHub (no terminal needed)

1. Go to the repo on GitHub: https://github.com/emilyharrison-stack/MPLT-research
2. Make sure you're on the branch `claude/research-dashboard-1EZfh` (there's a dropdown near the top left that says the branch name — click it and select the right one)
3. Click into the **`data`** folder
4. Click the **"Add file"** button (top right) and choose **"Upload files"**
5. Drag and drop your CSV or Excel files
6. At the bottom, click the green **"Commit changes"** button

The dashboard on Streamlit Cloud will automatically pick up the new files within a few minutes. (You may need to click the "Rerun" button in the top right of the dashboard, or click the three-dot menu and choose "Reboot app".)

### What files to upload

- **CSV or Excel files** with analyst estimates — put them directly in the `data` folder
- **PDF reports** — put them in `data/reports/` (you may need to create that subfolder)

Once your files are uploaded, let me know the file names and I'll update the code to read from your real data instead of the sample data.

---

## Troubleshooting

**Dashboard shows an error after uploading new data** — The code needs to be updated to read your specific file format. Share the file names and column headers with me and I'll update it.

**Can't find the repo when deploying** — Make sure you're signed into GitHub with the account that has access to `emilyharrison-stack/MPLT-research`.

**Dashboard is slow to load** — The first load after a period of inactivity takes about 30 seconds. After that it's fast.

**Need help?** — Open an issue on this GitHub repo or reach out to the team.
