#!/usr/bin/python3
import mysql.connector

try:
    # CONNECT TO MYSQL SERVER
    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password=""
    )

    cursor = connection.cursor()

    # CREATE DATABASE (WILL NOT FAIL IF IT ALREADY EXISTS)
    cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")

    print("Database 'alx_book_store' created successfully!")

except mysql.connector.Error as error:
    print(f"Error connecting to MySQL: {error}")

finally:
    # CLOSE CURSOR AND CONNECTION
    if 'cursor' in locals():
        cursor.close()
    if 'connection' in locals():
        connection.close()
