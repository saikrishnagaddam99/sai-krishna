import mysql.connector

def get_db_connection():
    """Get database connection"""
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="Samuel@123",
        database="payment_db"
    )

