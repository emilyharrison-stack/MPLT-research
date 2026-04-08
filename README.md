# MPLT Research Dashboard

An interactive dashboard for comparing Wall Street analyst reports on Maplight Therapeutics. View report summaries by publisher, compare specific metrics across analysts, and spot where analysts disagree.

---

## Getting Started (First Time Setup)

You only need to do these steps once.

### Step 1: Install Python

Check if Python is already installed. Open **Terminal** (Mac) or **Command Prompt** (Windows) and type:

```
python3 --version
```

If you see a version number (like `Python 3.11.5`), you're good — skip to Step 2.

If not, download Python from https://www.python.org/downloads/ and install it. During installation on Windows, **check the box that says "Add Python to PATH"**.

### Step 2: Install Git

Check if Git is already installed:

```
git --version
```

If you see a version number, skip to Step 3.

If not, download Git from https://git-scm.com/downloads and install it with the default settings.

### Step 3: Download the code

Open Terminal (Mac) or Command Prompt (Windows). Navigate to where you want to put the project. For example, to put it on your Desktop:

```
cd ~/Desktop
```

Then download the code:

```
git clone https://github.com/emilyharrison-stack/MPLT-research.git
```

This creates a folder called `MPLT-research` on your Desktop.

Now go into that folder and switch to the right branch:

```
cd MPLT-research
git checkout claude/research-dashboard-1EZfh
```

### Step 4: Install the dashboard dependencies

Still in Terminal, inside the `MPLT-research` folder, run:

```
pip install -r requirements.txt
```

This installs Streamlit (the dashboard framework), Plotly (for charts), and Pandas (for data handling). It may take a minute.

---

## Running the Dashboard

Every time you want to use the dashboard, open Terminal, go to the project folder, and run:

```
cd ~/Desktop/MPLT-research
streamlit run app.py
```

Your browser will automatically open to `http://localhost:8501` with the dashboard.

To stop the dashboard, go back to Terminal and press `Ctrl+C`.

---

## Adding Your Real Data

Right now the dashboard uses sample data. To use your own analyst reports:

1. Find the `data` folder inside your project:
   - **Mac**: `~/Desktop/MPLT-research/data/`
   - **Windows**: `C:\Users\YourName\Desktop\MPLT-research\data\`

2. Drop your CSV or Excel files into that `data` folder

3. For PDF reports, create a subfolder called `reports` inside `data` and put them there:
   - `MPLT-research/data/reports/morgan_stanley_mplt.pdf`
   - `MPLT-research/data/reports/goldman_sachs_mplt.pdf`
   - etc.

4. Let me know the file names and I'll update the code to read from your real files instead of the sample data

---

## What's in the Dashboard

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

## Troubleshooting

**"command not found: streamlit"** — Try `python3 -m streamlit run app.py` instead.

**"No module named streamlit"** — Run `pip install -r requirements.txt` again.

**Dashboard won't open in browser** — Manually go to `http://localhost:8501` in your browser.

**Need help?** — Open an issue on this GitHub repo or reach out to the team.
