import mysql.connector

def create_connection():
    try:
        conn = mysql.connector.connect(
            user = 'admin',
            password='',
            host = 'loclhost',
            port=3306,
            database = 'records'        
        )
        return conn
    except mysql.connector.Error as e:
        print(e)





 