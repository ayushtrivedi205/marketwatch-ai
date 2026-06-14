import pandas as pd

from database.db import engine


def load_alerts():

    query = """
    SELECT *
    FROM price_alerts
    ORDER BY alert_time DESC
    """

    return pd.read_sql(
        query,
        engine
    )