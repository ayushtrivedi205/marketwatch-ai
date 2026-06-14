import pandas as pd
from database.db import engine

def load_data():

    query = """
    SELECT *
    FROM price_history
    ORDER BY timestamp
    """

    return pd.read_sql(query, engine)