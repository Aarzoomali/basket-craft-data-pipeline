import os
import pandas as pd
from sqlalchemy import create_engine

# ✅ Load secrets from GitHub Actions environment
mysql_user = "analyst"
mysql_password = "go_lions"
mysql_host = "db.isba.co"
mysql_db = "basket_craft"
pg_user = "analyst"
pg_password = "go_lions"
pg_host = "db.isba.co"
pg_db = "basket_craft"

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
pg_url = f"postgresql+psycopg2://{pg_user}:{pg_password}@{pg_host}/{pg_db}"
pg_engine = create_engine(pg_url)

# ✅ Load data into Postgres raw schema
df.to_sql('website_sessions', pg_engine, schema='raw', if_exists='replace', index=False)

print("✅ Data successfully loaded into raw.website_sessions")
