from database import DataBase
from sqlite3 import Error
from management import Management

class Student(DataBase):
    def __init__(self):
        self.manage = Management()

    def viewFaculty(self):
        self.manage.view_faculty()
    
    
        


