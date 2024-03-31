import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="Pa$$w0rd",  # blank for mac
  database="teajinja_db"
)


def get_db_connection():
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Pa$$w0rd",  # blank for mac
        database="teajinja_db"
    )

    return mydb


def add_order(tea, user, collection):
    conn = get_db_connection()
    cursor = conn.cursor()

    sql = "INSERT INTO orders (tea_id, user_id, collection_time) VALUES (%s, %s, %s)"
    val = (tea, user, collection)
    cursor.execute(sql, val)

    conn.commit()

