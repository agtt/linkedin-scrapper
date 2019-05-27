import mysql.connector
from mysql.connector import Error


class db:
    def __init__(self, host='localhost', database='linkedin', user='root', password=''):
        try:
            self.connect = mysql.connector.connect(host=host, database=database, user=user, password=password)
            print('MySQL connection successfliy')
        except Error as e:
            print("Error while connecting to MySQL", e)

    def query(self, query):
        cursor = self.connect.cursor()
        cursor.execute(query)
        record = cursor.fetchall()
        return record

    def addprofile(self, url, data=""):
        """ Add Profile to MySQL """
        try:
            cursor = self.connect.cursor()
            sql = "INSERT INTO scrappers (url, data) VALUES (%s, %s)"
            val = (url, data)
            cursor.execute(sql, val)
            cursor.close()
            self.connect.commit()
        except Exception as e:
            print(str(e))
        return True

    def updateprofile(self, id, data):
        try:
            cursor = self.connect.cursor()
            sql = "UPDATE scrappers set data=%s ,is_fetch=1 where id =%s"
            cursor.execute(sql,(data,id))
            cursor.close()
            self.connect.commit()
        except Exception as e:
            print(str(e))
        return True

    def __del__(self):
        if self.connect.is_connected():
            self.connect.close()
