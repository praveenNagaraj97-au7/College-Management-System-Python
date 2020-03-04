import sqlite3
from sqlite3 import Error
from time import sleep
class DataBase:
    
    def __init__(self):
        self.dblocation = r'E:\Python\Projects\College Management System Using MySql\DATA\cms.db'
    
    def openconnection(self):
        conn = None
        try:
            conn = sqlite3.connect(self.dblocation)
            print("Connection Establishing...!")
            sleep(3)
            print("Connected ✔")
        except Error as e:
            print(e('Something Went Wrong and connection to db failed \nPlease be assured while we fix this ..! '))
        finally:
            return conn
    
    def closeconnection(self):
        self.openconnection().close()
