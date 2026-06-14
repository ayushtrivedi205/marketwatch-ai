import pandas as pd
from database.db import engine

def get_metrics():

    query = """
    SELECT *
    FROM price_history
    """

    df = pd.read_sql(query, engine)

    return {
        "records": len(df),
        "coins": df["symbol"].nunique(),
        "avg_price": round(df["price"].mean(), 2)
    }