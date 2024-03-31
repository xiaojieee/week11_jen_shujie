import mysql.connector

# mydb = mysql.connector.connect(
#   host="localhost",
#   user="root",
#   password="Pa$$w0rd",  # blank for mac
#   database="tea_db"
# )
#
# cursor = mydb.cursor()


def get_db_connection():
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
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


def submit_order_db(customer_name, tea_name):
    mydb = get_db_connection()
    cursor = mydb.cursor()

    # Insert data into the tea_orders table
    sql = "INSERT INTO tea_orders (name_n, tea_type) VALUES (%s, %s)"
    values = (customer_name, tea_name)

    cursor.execute(sql, values)
    mydb.commit()

# def main():
#     print(mydb)
#
#     cursor = mydb.cursor()
#
#     sql = "INSERT INTO orders (tea_id, user_id, collection_time) VALUES (%s, %s, %s)"
#     val = ("1", "1", '16:00:00')
#     cursor.execute(sql, val)
#
#     mydb.commit()
#
#     print(cursor.rowcount, "record inserted.")
#
# def add_order(tea, user, collection):
#     conn = get_db_connection()
#     cursor = conn.cursor()
#
#     sql = "INSERT INTO orders (tea_id, user_id, collection_time) VALUES (%s, %s, %s)"
#     val = (tea, user, collection)
#     cursor.execute(sql, val)
#
#     conn.commit()
#
#
# if __name__ == "__main__":
#     main()
