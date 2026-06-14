import psycopg2

try:
    conn = psycopg2.connect(
        host="localhost",
        database="marketwatch",
        user="postgres",
        password="031103"
    )

    print("Connected Successfully!")

    conn.close()

except Exception as e:
    print("Error:", e)