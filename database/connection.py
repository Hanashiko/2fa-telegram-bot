import mysql.connector
from mysql.connector.connection import MySQLConnection
from mysql.connector.cursor import MySQLCursor
from dotenv import load_dotenv
import os

load_dotenv()

DB_HOST = os.getenv("DB_HOST")
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_NAME = os.getenv("DB_DATABASE")

def get_connection():
    try:
        connection = mysql.connector.connect(
            host=DB_HOST,
            database=DB_NAME,
            user=DB_USER,
            password=DB_PASSWORD,
            charset='utf8mb4',  
            collation='utf8mb4_general_ci' 
        )
        return connection
    except mysql.connector.Error as err:
        print(f"Error connection database: {err}")
        return None

def close_connection(connection, cursor=None):
    if cursor is not None:
        try:
            cursor.close()
        except mysql.connector.Error as err:
            print(f"Error closing cursor: {err}")
    if connection is not None:
        try:
            connection.close()
        except mysql.connector.Error as err:
            print(f"Error closing connection: {err}")

def execute_query(query, values=None):
    connection = get_connection()
    if connection:
        try:
            cursor = connection.cursor()
            cursor.execute(query, values)
            connection.commit()
        except mysql.connector.Error as err:
            print(f"Error: {err}")
        finally:
            close_connection(connection, cursor)

def execute_query_fetchone(query, values=None):
    connection = get_connection()
    result = None
    if connection:
        try:
            cursor = connection.cursor()
            cursor.execute(query, values)
            result = cursor.fetchone()
        except mysql.connector.Error as err:
            print(f"Error: {err}")
        finally:
            close_connection(connection, cursor)
    return result

def execute_query_fetchall(query, values=None):
    connection = get_connection()
    result = None
    if connection:
        try:
            cursor = connection.cursor()
            cursor.execute(query, values)
            result = cursor.fetchall()
        except mysql.connector.Error as err:
            print(f"Error: {err}")
        finally:
            close_connection(connection, cursor)
    return result