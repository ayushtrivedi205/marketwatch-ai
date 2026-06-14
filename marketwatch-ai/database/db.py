from sqlalchemy import create_engine

DB_USER = "postgres"
DB_PASSWORD = "031103"
DB_HOST = "localhost"
DB_PORT = "5432"
DB_NAME = "marketwatch"

DATABASE_URL = (
    f"postgresql://{DB_USER}:{DB_PASSWORD}"
    f"@{DB_HOST}:{DB_PORT}/{DB_NAME}"
)

engine = create_engine(DATABASE_URL)