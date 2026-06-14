from database.db import engine

def save_to_database(df):

    df = df[["symbol", "price", "timestamp"]]

    df.to_sql(
        "price_history",
        engine,
        if_exists="append",
        index=False
    )

    print("Saved to PostgreSQL")