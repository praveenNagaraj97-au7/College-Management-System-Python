from management import Management 
import time
import sys
import tqdm
from time import sleep
from student import Student
class Main():
    def __init__(self):
        self.manage = Management()
        self.stud = Student()

   
    def mainpage(self):
        try:
            
            animation = "✒✔༼ つ ◕_◕ ༽つ|/-\\"
            for i in range(25):
                time.sleep(0.1)
                sys.stdout.write("\r" + animation[i % len(animation)])
                sys.stdout.flush()
            print ("""
----------------------------------------------
----------------------------------------------
---------COLLEGE MANAGEMENT SYSTEM------------
----------------------------------------------
----------------------------------------------
            """)

            option = int(input("""            
Choose an Option :
1 -- >  Management
2 -- >  Student
3 -- >  Teacher
4 -- >  Exit
Enter : """))
            if option == 1 :
                self.managementpage()
                #print("Management")
            if option == 2 :
                pass
                #self.studentpage()
                #print("Student")
            if option == 3 :
                #self.teacherpage()
                print("Teachet")
            if option == 4 :
                print(" ")
            else:
                print("Choose within the options provided : ")
        except Exception:
            print("\nOption should be number only\n")
            self.mainpage()
        finally:
            pass


# management page
    def managementpage(self):
        auth = self.manage._authorize()
        if auth == True:
            try:
                print("""
----------------------------------
----------------------------------
-----------WELCOME TO-------------
-----------MANAGEMENT-------------
-------------PANEL----------------  
----------------------------------
----------------------------------
        """)
                self.option1 = int(input("""            
Choose an Option :
1 -- >  FACULTY
2 -- >  STUDENT
3 -- >  CURRICULUM
4 -- >  ADMISSION
5 -- >  EXIT
Enter : """))
                if self.option1 == 1 :
                    self.faculty()
                    self.managementpage()
                if self.option1 == 2 :
                    self.student()
                    self.managementpage()
                if self.option1 == 3 :
                    self.curriculam()
                    self.managementpage()
                if self.option1 == 4 :
                    self.admission()
                    self.managementpage()
                if self.option1 == 5 :
                    self.mainpage()
                if self.option1 > 5:
                    print("Select Otions Withon the range")
                    self.managementpage()
                    
            except ValueError:
                print("Option should be entered in number only within range")
            finally:
                pass

# FACULTY Done With all check
    def faculty(self):
        try:
            if self.option1 == 1:
                option2 = int(input("""            
Choose an Option :
    FACULTY
1 -- >  ADD FACULTY
2 -- >  VIEW FACULTY
3 -- >  DELETE FACULTY
4 -- >  EXIT
Enter : """))
                if option2 == 1 :
                    self.manage.addteachers()
                    self.faculty()
                elif option2 == 2 :
                    self.manage.view_faculty()
                    self.faculty()
                elif option2 == 3:
                    self.manage.deletefaculty()
                    self.faculty()
                elif option2 == 4:
                    self.managementpage()
                    
                else:
                    print("Option Entered is out of range")
                    self.faculty()
        except ValueError:
            print("Option should be entered only in numbers")



# STUDENT

    def student(self):
        try:
            if self.option1 == 2:
                option2 = int(input("""            
Choose an Option :
    STUDENT
1 -- >  VIEW STUDENT
2 -- >  EXIT
Enter : """))
                if option2 == 1 :
                    self.manage.viewstudent()
                    self.student()
                if option2 == 2:
                    self.managementpage()
                else:
                    print("Option Entered is out of range")
                    self.student()
        except ValueError:
            print("Option should be entered only in numbers")




# Curriculam

    def curriculam(self):
        try:
            option = int(input("""
------------------------
SELECT AN OPTION
1 --> VIEW TIME TABLE
2 --> UPDATE TIME TABLE 
3 --> VIEW EVENTS
4 --> UPDATE EVENTS
5 --> EXIT
------------------------

:"""))
            if option == 1:
                self.manage.viewtimetable()
                self.curriculam()
            if option == 2:
                self.manage._timetable()
                self.curriculam()
            if option == 3:
                self.manage.showevent()
                self.curriculam()
            if option == 4 :
                self.manage.updateevent()
                self.curriculam()
            if option == 5 :
                self.mainpage()
            if option > 5 :
                print("Choose Within the option")
                self.curriculam()
        except ValueError:
            print("Choose from the option only")
        finally:
            pass






# Admission module

    def admission(self):
        try:
            option = int(input("""
----------------------------------
----------------------------------
--------ADMISSION PORTAL----------
----------------------------------
----------------------------------
1 -- > NEW REGISTER
2 -- > VIEW REGISTERED STUDENT
3 -- > DO THE ADMIISON PROCESS 
4 -- > EXIT
 >>: """))
            if option == 1:
                self.manage.register()
                self.managementpage()
            if option == 2:
                self.manage.view_registeredstudent()
                self.managementpage()
            if option == 3 :
                self.manage.admission()
                self.managementpage()
            if option == 4 :
                self.managementpage()
            if option > 4 :
                print("Select options within the range ")
                self.admission()
        except ValueError:
            print("Enter option in numbers")




'''
# Student Page
    def studentpage(self):
        option = int(input("""
-------------------------------
-------------------------------
---COLLEGE MANAGEMENT SYSTEM---
-------------------------------
-------------------------------
SELECT OPTION :

2 -- > VIEW FACULTY
3 -- > VIEW TIMETABLE
4 -- > VIEW EXAM RESULT
        """))
        if option == 1 :
            pass
        if option == 2 :
            self.stud.viewFaculty()


'''







m = Main()
m.mainpage()