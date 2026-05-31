import os
from dotenv import load_dotenv
import psycopg2

load_dotenv()

def get_db_connection():
    conn = psycopg2.connect(os.getenv("DATABASE_URL"))
    return conn

conn = get_db_connection()
cursor = conn.cursor()

cursor.execute("SELECT * FROM authors WHERE author_id = 1;")
rows = cursor.fetchall()
print(rows)
cursor.close()
conn.close()
