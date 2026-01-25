# Bulk Ads.txt Scanner

A batch processing tool for AdOps teams to verify `ads.txt` and `app-ads.txt` availability across multiple domains simultaneously.

## Features

* **Bulk Processing:** Accepts a list of domains (copy-paste from Excel/Sheets).
* **Smart Validation:** Detects valid files, HTTP errors, and Soft 404s.
* **Reporting:** Displays results in an interactive table with record counts.
* **Export:** Download full scan results as CSV.

## Tech Stack

* Python 3
* Streamlit
* Pandas
* Requests

## Usage

1. Install requirements: `pip install -r requirements.txt`
2. Run the app: `streamlit run app.py`
3. Paste a list of domains (one per line) and click "Start Scan".
