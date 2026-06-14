import pandas as pd
from database.db import engine

query = """
SELECT *
FROM price_history
"""

df = pd.read_sql(query, engine)

print(df.head())
print("\nTotal Rows:", len(df))