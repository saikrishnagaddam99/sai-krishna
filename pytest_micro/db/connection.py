import mysql.connector


def get_connection():

    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Samuel@123",   
        database="university_db"
    )
    return conn