import mysql.connector
class Database:
    def __init__(self):
        self.connection= mysql.connector.connect(
            host="localhost",
            user="root",
            port="3306",
            database="proyecto_estaciones"
        )
        self.cursor = self.connection.cursor()