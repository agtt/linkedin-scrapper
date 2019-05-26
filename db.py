import mysql.connector
from mysql.connector import Error


class db:
    def __init__(self, host='localhost', database='linkedin', user='root', password=''):
        try:
            self.connection = mysql.connector.connect(host=host, database=database, user=user, password=password)
        except Error as e:
            print("Error while connecting to MySQL", e)

    def query(self, query):
        cursor = self.connection.cursor()
        cursor.execute(query)
        record = self.cursor.fetchall()
        return record

    def addprofile(self, url, data=""):
        """ Add Profile to MySQL """
        try:
            cursor = self.connection.cursor()
            sql = "INSERT INTO scrappers (url, data) VALUES (%s, %s)"
            val = (url, data)
            cursor.execute(sql, val)
            cursor.close()
            self.connection.commit()
        except Exception as e:
            print(str(e))
        return True

    def __del__(self):
        if self.connection.is_connected():
            # self.cursor.close()
            self.connection.close()
