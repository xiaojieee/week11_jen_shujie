import mysql.connector


def get_db_connection():
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",  # Pa$$w0rd < for windows, please don't delete
        database="teajinja_db"
    )
    return mydb


def get_tea():
    mydb = get_db_connection()
    cursor = mydb.cursor()

    sql = "SELECT * FROM tea"
    cursor.execute(sql)
    result_set = cursor.fetchall()

    tea_list = []

    for tea in result_set:
        tea_list.append({'tea_id': tea[0], 'tea_name': tea[1], 'tea_price': tea[2], 'tea_filename': tea[3]})
    return tea_list


def get_last_collection_id():
    mydb = get_db_connection()
    cursor = mydb.cursor()

    sql = "SELECT MAX(collection_id) FROM collection"
    cursor.execute(sql)
    last_primary_key = cursor.fetchone()[0]

    if last_primary_key is None:
        last_primary_key = 0

    return last_primary_key


def submit_collection_db(collection_time):
    mydb = get_db_connection()
    cursor = mydb.cursor()

    primary_key = get_last_collection_id()
    collection_number = primary_key + 1

    # Insert data into the orders table
    sql = "INSERT INTO collection (collection_time, collection_number) VALUES (%s, %s)"
    values = (collection_time, collection_number)

    cursor.execute(sql, values)
    mydb.commit()


def submit_order_db(tea_id, quantity, name):
    mydb = get_db_connection()
    cursor = mydb.cursor()
    collection_id = get_last_collection_id()

    # Insert data into the orders table
    sql = "INSERT INTO orders (tea_id, quantity, customer_name, collection_id) VALUES (%s, %s, %s, %s)"
    values = (tea_id, quantity, name, collection_id)

    cursor.execute(sql, values)
    mydb.commit()
