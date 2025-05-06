Website Sessions Data Pipeline (Dec 2023)
This repository contains an end-to-end data pipeline built for the SQL - Take-Home Quiz 03. The goal was to replicate a real-world analytics workflow by extracting session data for December 2023 from a MySQL database, loading it into a Postgres raw table, transforming it with modular dbt models (staging and warehouse layers), and visualizing insights in Looker Studio.

The pipeline was built using Python, Pandas, and SQLAlchemy to extract and load data (elt/basket_craft_website_sessions_extract_load_raw.py). It is automated with GitHub Actions, triggered manually or every 15 minutes, with all credentials securely managed using GitHub Secrets. Transformations are done using dbt, with staging (stg_website_sessions) and warehouse (fct_website_sessions_utm_source_daily) models that clean, structure, and aggregate data.

Finally, a Looker Studio dashboard presents the results interactively with cross-filterable components like a daily sessions table, a heatmap of repeat sessions by utm_source, a total sessions scorecard, a time-series trendline, and a sessions-by-source bar chart.

This project brings together key roles—data engineering, analytics engineering, and data visualization—to create a fully automated and stakeholder-ready solution.


Dashboard - https://lookerstudio.google.com/reporting/95600e1b-d3ff-41f4-b1d0-a7ec3be0631a

Pipeline diagram-
![Image](https://github.com/user-attachments/assets/d4863e9e-7614-43ee-8f6d-fceec0a851ee)

