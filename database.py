import mysql.connector
from mysql.connector import Error

def get_connection():
    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="aarohi1011",
            database="python_learning",
            use_pure=True
        )

        return connection

    except Error as e:
        print("MySQL connection error:", e)
        return None