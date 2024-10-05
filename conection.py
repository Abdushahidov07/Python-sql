import psycopg2
from sql_password import paswo
conn = psycopg2.connect(
    database = "Education_db",
    user = "postgres",
    host = 'localhost',
    password = "paswo",
    port = 5432
) 
