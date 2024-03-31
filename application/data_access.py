import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="Pa$$w0rd",  # blank for mac
  database="teajinja_db"
)


def main():
    print(mydb)

    cursor = mydb.cursor()

    sql = "INSERT INTO orders (tea_id, user_id, collection_time) VALUES (%s, %s, %s)"
    val = ("1", "1", '16:00:00')
    cursor.execute(sql, val)

    mydb.commit()

    print(cursor.rowcount, "record inserted.")


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


if __name__ == "__main__":
    main()
