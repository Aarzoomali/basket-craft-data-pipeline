import os
import pandas as pd
from sqlalchemy import create_engine
from dotenv import load_dotenv

# load env vars from .env file
load_dotenv()

# ✅ Load secrets from GitHub Actions environment

mysql_user = os.getenv("MYSQL_USER")
mysql_password = os.getenv("MYSQL_PASSWORD")
mysql_host = os.getenv("MYSQL_HOST")
mysql_db = os.getenv("MYSQL_DB")

pg_user = os.getenv("PG_USER")
pg_password = os.getenv("PG_PASSWORD")
pg_host = os.getenv("PG_HOST")
pg_db = os.getenv("PG_DB")

print("✅ Secrets loaded:")
print("MYSQL_USER:", mysql_user)
print("MYSQL_HOST:", mysql_host)
print("MYSQL_DB:", mysql_db)
print("PG_USER:", pg_user)
print("PG_HOST:", pg_host)
print("PG_DB:", pg_db)

# ✅ Connect to MySQL (source)
mysql_url = f"mysql+pymysql://{mysql_user}:{mysql_password}@{mysql_host}/{mysql_db}"
mysql_engine = create_engine(mysql_url)

# ✅ Query December 2023 sessions
query = """
SELECT * FROM website_sessions
WHERE created_at BETWEEN '2023-12-01' AND '2023-12-31 23:59:59';
"""
df = pd.read_sql(query, mysql_engine)


# ✅ Connect to Postgres (destination)
pg_url = f"postgresql+psycopg2://{pg_user}:{pg_password}@{pg_host}/{pg_db}?sslmode=require"
pg_engine = create_engine(pg_url)

# ✅ Load data into Postgres raw schema
df.to_sql('website_sessions', pg_engine, schema='raw', if_exists='replace', index=False)

print("✅ Data successfully loaded into raw.website_sessions")

