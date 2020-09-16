import mysql.connector


class Database:
    def __init__(self):
        self.__connection = mysql.connector.connect(host="localhost", user="root", passwd="manager", db="dbda_aug_2019")
        self.__cursor = self.__connection.cursor()

    def select(self, query):
        self.__cursor.execute(query)
        return self.__cursor.fetchall()

    def execute(self, query):
        self.__cursor.execute(query)
        return self.__connection.commit()

    def __del__(self):
        self.__cursor.close()
        self.__connection.close()
