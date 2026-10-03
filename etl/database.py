import mysql.connector


def get_connection():
    connection = mysql.connector.connect(
        host="localhost",
        port=3306,
        user="root",
        password="DHNiv#1107",
        database="qatarretail"
    )

    return connection