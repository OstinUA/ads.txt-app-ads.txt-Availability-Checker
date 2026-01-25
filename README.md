# Ads.txt Availability Checker

A lightweight utility tool for AdOps professionals to instantly verify the existence of `ads.txt` and `app-ads.txt` files on any given domain.

## Features

* **Instant Verification:** Checks HTTP status codes (200, 403, 404, 500).
* **Smart Parsing:** Detects "Soft 404s" (where a server returns HTML instead of a text file).
* **Line Counting:** Automatically counts the number of records if the file exists.
* **Format Switcher:** Toggle between standard web (`ads.txt`) and mobile app (`app-ads.txt`) environments.

## Tech Stack

* Python 3
* Streamlit
* Requests

## Usage

1. Install requirements: `pip install -r requirements.txt`
2. Run the app: `streamlit run app.py`
