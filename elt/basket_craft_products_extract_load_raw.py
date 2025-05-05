import pandas as pd
from sqlalchemy import create_engine

mysql_user = 'analyst'
mysql_password = 'go_lions'
mysql_host = 'db.isba.co'
mysql_db = 'basket_craft'
name: Run Basket Craft Extract and Load to Raw

on:
  workflow_dispatch:   # lets you trigger the workflow manually from GitHub
  schedule:
    - cron: '0 8 * * *'  # optional: runs daily at 8 AM UTC

env:
  MYSQL_USER: ${{ secrets.MYSQL_USER }}
  MYSQL_PASSWORD: ${{ secrets.MYSQL_PASSWORD }}
  MYSQL_HOST: ${{ secrets.MYSQL_HOST }}
  MYSQL_DB: ${{ secrets.MYSQL_DB }}
  PG_USER: ${{ secrets.PG_USER }}
  PG_PASSWORD: ${{ secrets.PG_PASSWORD }}
  PG_HOST: ${{ secrets.PG_HOST }}
  PG_DB: ${{ secrets.PG_DB }}

jobs:
  extract-load:
    runs-on: ubuntu-latest

    steps:
      - name: Checkout code
        uses: actions/checkout@v3

      - name: Set up Python
        uses: actions/setup-python@v4
        with:
          python-version: '3.12'

      - name: Install dependencies
        run: pip install pandas sqlalchemy pymysql psycopg2-binary

      - name: Run data load script
        run: python3 elt/basket_craft_website_sessions_extract_load_raw.py
