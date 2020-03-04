
import sqlite3
from sqlite3 import Error
from database import DataBase
from time import sleep
import getpass
from tqdm import tqdm
import datetime


class Management(DataBase):
    

# private key
    '''
    Don't Modify/Call this method :
    as it will destroy whole project by crashing the DataBase
    i have made this as a private method
    '''

    def _key_authorizer(self):
        try:
            conn = self.openconnection()
            curser = conn.cursor()
            curser.execute("""CREATE TABLE IF NOT EXISTS CMSHEAD(
                USERNAME VARCHAR(250),
                PASSWORD VARCHAR(250)
            )
            """)
            curser.execute("""INSERT INTO CMSHEAD (USERNAME,PASSWORD)
            VALUES('P','P')
            """)
            conn.commit()
            print("College head Username and Password creating..!")
            sleep(3)
            print("Success")
        except Error as e:
            print(e("Something went wrong"))
        finally:
            conn.close()
            print("Connection closing...")
            sleep(3)
            print("Closed")

    def _authorize(self):
        auth = False
        try:
            userinput = input('Enter Username : ' )
            passinput = getpass.getpass(prompt=f'{userinput} Enter Your Password : ',stream='*')
            conn = self.openconnection()
            cursor = conn.cursor()
            cursor.execute("""SELECT USERNAME FROM CMSHEAD""")
            user = cursor.fetchone()
            cursor.execute("""SELECT PASSWORD FROM CMSHEAD""")
            passw = cursor.fetchone()
            user = user[0]
            passwd = passw[0]
            conn.close()
        except Error as e:
            print(e)
        finally:
            print("Checking for Username and Password Match ...!")
            sleep(3)
            if user == userinput and  passwd == passinput:
                auth = True
                conn.close()
                return auth
                print("Login Access Gained ...🛅")
            else:
                print("Access Failed")
            print("Connectin Closed")

# Teacher Module

    def addteachers(self):
        #auth = self._authorize()
        if 1 == 1:
                
            try:               
                name = input("Enter the Name of the teacher : ").capitalize()
                if name.isnumeric():
                    print("Name should be a string.")
                    name = input("Enter the name of the teacher : ").capitalize()
                    if name.isnumeric():
                        print("Exiting!! ")

                
                age = int(input(f"Please enter {name}'s age :  "))
                if age > 50 :
                    print("Age should be less than 50")
                    age = int(input(f"Please enter {name}'s age :  "))
                    if age > 50 :
                        print("Exiting!!")

                option = int(input("""
                    Select an option:
                    1 -- > EEE
                    2 -- > CSE 
                    3 -- > ISE
                    4 -- > ECE
                    >>:   
                    """))
                if option == 1:
                    branch = 'EEE'
                if option == 2 :
                    branch = 'CSE'
                if option == 3:
                    branch = 'ISE'
                if option == 4:
                    branch = 'ISE'
                if option >= 5:
                    print("Select options provided")
                    option = int(input("""
                    Select an option:
                    1 -- > EEE
                    2 -- > CSE 
                    3 -- > ISE
                    4 -- > ECE
                    >>:   
                    """))
                    if option == 1:
                        branch = 'EEE'
                    if option == 2 :
                        branch = 'CSE'
                    if option == 3:
                        branch = 'ISE'
                    if option == 4:
                        branch = 'ISE'
                    if option >= 5:
                        print("Alien Invasion Exiting")

                mail = input("Please enter Mail ID : ")
                if '@' not in mail:
                    print("Enter a valid mail.")
                    mail = input("Please enter Mail ID : ")
                    if "@" not in mail:
                        print("Exiting!!!")
                
                subject = input(f"Enter the Name of subject that {name} going to teach : ").upper()
                username = name.upper()+"@CMS"

                conn = self.openconnection()
                cursor = conn.cursor()
                print("Checking For Table Existance !")
                sleep(2)


                cursor.execute("""CREATE TABLE IF NOT EXISTS FACULTY (
                    EMPID INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                    NAME text,
                    AGE INT,
                    MAIL text, 
                    SUBJECT text,
                    BRANCH text,
                    USERNAME text,
                    PASSWORD text
                )
                """)

                print("Table exists")

                cursor.execute("""INSERT INTO FACULTY (NAME,AGE,BRANCH,MAIL,SUBJECT,USERNAME,PASSWORD)
                VALUES(?,?,?,?,?,?,?)
                """,(name,age,branch,mail,subject,username,username))
                print(f"""Adding new faculty with :\n
                Name    :     {name}
                Age     :     {age}
                BRANCH  :     {branch}
                Mail    :     {mail}
                Subject :     {subject}
                Username:     {username}
                Password:     {username}
                """)
                
                conn.commit()
                sleep(2)
                print("FACULTY ADDED SUCCESFULLY 💨")
                option = input("Enter Y/y to add one more Faculty : ")
                if option == 'y' or option == 'Y':
                    self.addteachers()
                else:
                    print(" ")

            except Exception :
                print("Wrong input or something went wrong")
                self.addteachers()
            finally:
                conn.close()
        else:
            n = input("Enter Y/y to : ")
            if n == 'Y' or n == 'y':
                print("Try Again")
                self.addteachers()
            else:
                print("Good Bye")
    

        '''
        View Faculty :
        where this method will be used in management , student , teacher 
        used tqdm module for console based loading gui
        '''

    def view_faculty(self):
        
        try:
            conn = self.openconnection()
            curser = conn.cursor()
            curser.execute("SELECT EMPID,NAME,AGE,BRANCH FROM FACULTY ")
            details = curser.fetchall()
            detaillst = [x for x in details]
            names = []
            age = []
            empid = []
            branch = []
            for each in detaillst:
                empid.append(each[0])
                names.append(each[1])
                age.append(each[2])
                branch.append(each[3])
            com = list(zip(empid,names,age,branch))
            #print("Getting Details of Faculty ..!")

            loop = tqdm(total = 100,position = 0 ,leave = False)
            for k in range(100):
                loop.set_description("PLEASE WAIT Getting list")
                sleep(.02)
                loop.update(1)
            loop.close()
            print("DETAILS OF FACULTY")
            print("-------------------------------------------------------------")
            print("EMPID       ||    AGE      ||   BRANCH   ||    NAME ")
            print("-------------------------------------------------------------")
            for each in com:
                print(" ",each[0],"        ||   ",each[2],"      ||   ",each[3],"    ||   ",each[1])
                
                
            
        except Error :
            print("Something went wrong...!")
        finally:
            conn.close()
       
    def deletefaculty(self):
        #auth = self._authorize()
        if 1 == 1:
            try:
                n = int(input("Enter the Employee ID to Remove : "))
                conn = self.openconnection()
                cursor = conn.cursor()
                cursor.execute("SELECT EMPID FROM FACULTY")
                prevdate = cursor.fetchall()
                #print(len(prevdate))
                print("Removing Employee from CM")
                cursor.execute("DELETE FROM FACULTY WHERE EMPID = (?)",(n,))
                conn.commit()
                cursor.execute("SELECT EMPID FROM FACULTY")
                aftrdate = cursor.fetchall()
                #print(len(aftrdate))
                if len(prevdate) == len(aftrdate):
                    print("Faculty is not found at provided ID")
                    option = input("Do You Wish to View the DataBase to see the empid enter Y/y: ")
                    if option == 'Y' or option == 'y':
                        self.view_faculty()
                        self.deletefaculty()
                else:
                    print("Successfully Removed")
            
            except (Error ,ValueError):
                print("Enter employee as number only ")
                option = input("Do You Wish to View the DataBase to see the empid enter Y/y: ")
                if option == 'Y' or option == 'y':
                    self.view_faculty()
                    self.deletefaculty()
                else:
                    print(Error)
            finally:
                conn.close()
        else:
            n = input("Enter Y/y to : ")
            if n == 'Y' or n == 'y':
                print("Try Again")
                self.deletefaculty()
            else:
                print("Good Bye")

# Student Module
    def viewstudent(self):
        try:
            conn = self.openconnection()
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM TESTSTUD")
            detail = cursor.fetchall()
            loop = tqdm(total = 100,position = 0 ,leave = False)
            for k in range(100):
                loop.set_description("PLEASE WAIT Getting list")
                sleep(.02)
                loop.update(1)
            loop.close()
            print(" STUDENT_ID    AGE      DEPT     PHONE_NO       NAME")
            for each in detail:
                print("    ",each[0],"       ",each[2], "     ",each[3], "   ",each[7],"    ", each[1] )
            conn.close()
        except:
            pass

# Admission
    def register(self):
        try:
            name = input("Enter Name : ").capitalize()
            if name.isnumeric():
                print("Name should string")
                name = input("Enter Name : ").capitalize()
                if name.isnumeric() :
                    print("Exiting")
                    sleep(2)
                    print("Alien Invasion..!")

            age = int(input(f"Enter {name}'s Age : "))
            if age > 30:
                print("Age cannot be more than 30")
                age = int(input(f"Enter {name}'s Age : "))
            mail = input("Enter Mail : ")
            if '@' not in mail:
                print("Enter a valid mail")
                mail = input("Enter Mail : ")
                if '@' not in mail:
                    mail = 1 + ''
            phno = int(input("Enter Contact Number : "))
            if len(str(phno)) < 10:
                print("Enter a valid Phone Number")
                phno = int(input("Enter Contact Number : "))
                if len(str(phno)) < 10:
                    phno = 1+""
            fathername = input("Enter FATHER Name : ").capitalize()
            if fathername.isnumeric() :
                print("Name should string")
                fathername = input("Enter Father Name : ").capitalize()
                if fathername.isnumeric():
                    print("Exiting")
                    sleep(2)
                    print("Alien Invasion..!")
            mothername = input("Enter MOTHER Name : ").capitalize()
            if mothername.isnumeric():
                print("Name should string")
                mothername = input("Enter Mother Name : ").capitalize()
                if mothername.isnumeric():
                    print("Exiting")
                    sleep(2)
                    print("Alien Invasion..!")
            parentmail = input("Enter Parent Mail ID :  ")
            if '@' not in parentmail:
                print("Enter a valid mail")
                parentmail = input("Enter Parent Mail ID :  ")
                if '@' not in parentmail:
                    print("Alien invasion")
                    parentmail = 1 + ' '
            parentno = int(input("Enter Parent Number : "))
            if len(str(parentno)) < 10:
                print("Enter a valid Phone Number")
                parentno = int(input("Enter Contact Number : "))
                if len(str(parentno)) < 10:
                    parentno = 1+""
            prevclgname = input("Enter Previous College Name : ").upper()
            if prevclgname.isnumeric():
                print("Name should string")
                prevclgname = input("Enter Previous College Name : ").upper()
                if prevclgname.isnumeric():
                    print("Exiting")
                    sleep(2)
                    print("Alien Invasion..!")
            branchoption = input("""
-------------------------------
-------------------------------
---COLLEGE MANAGEMENT SYSTEM---
-------------------------------
-------------------------------
CHOOSE ONE OPTION :
1 -- > EEE
2 -- > CSE 
3 -- > ISE
4 -- > ECE            
: """).upper()
            if int(branchoption) == 1 or branchoption == 'EEE':
                branch = 'EEE'
            elif int(branchoption) == 2 or branchoption == 'CSE':
                branch = 'CSE'
            elif int(branchoption) == 3 or branchoption == 'ISE':
                branch = 'ISE'
            elif int(branchoption) == 4 or branchoption == 'ECE':
                branch = 'ECE'
            feeop = input("Enter Y/y to continue if fee is paid and student have refno : ")
            if feeop == 'y' or feeop == 'Y':
                _fee = input("Enter the amount paid with bank ref.no \n'hit a space after fee amount and enter ref.no': ").split(" ")
                feepaid = int(_fee[0])
                refno = _fee[1]
            else:
                print("Pay and get the refno.")
                feepaid = ' '
            


            conn = self.openconnection()
            cursor = conn.cursor()
            cursor.execute("""CREATE TABLE IF NOT EXISTS NEWREGISTER (
                RID INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                NAME TEXT,
                AGE INT,
                MAILID TEXT,
                PHONE_NO INT,
                FATHER TEXT,
                MOTHER TEXT,
                PARENT_MAIL TEXT,
                PARENT_NO INT,
                PREVCLGNAME TEXT,
                BRANCH TEXT,
                FEEPAID INT,
                REFNO TEXT 
                )""")
            cursor.execute("""INSERT INTO NEWREGISTER (
                NAME ,AGE,MAILID,PHONE_NO,FATHER,MOTHER,PARENT_MAIL,PARENT_NO ,PREVCLGNAME ,BRANCH ,FEEPAID ,REFNO)
                VALUES (?,?,?,?,?,?,?,?,?,?,?,?)
            """,(name,age,mail,parentno,fathername,mothername,parentmail,parentno,prevclgname,branch,feepaid,refno))
            conn.commit()
            print("Registration Succesful...!")
        except (TypeError,UnboundLocalError,ValueError,Error):
            print("Fill the details properly")
            self.register()
        finally:
            conn.close()



    def view_registeredstudent(self):
        #auth = self._authorize()
        if 1 == 1:
            try:
                conn = self.openconnection()
                cursor = conn.cursor()
                cursor.execute("SELECT * FROM NEWREGISTER")
                newregstud = cursor.fetchall()
                print(newregstud)
            except Error:
                print("No one registered")
            finally:
                conn.close()

    def admission(self):
        try:
            conn = self.openconnection()
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM NEWREGISTER WHERE FEEPAID = 45000")
            reg = cursor.fetchall()
            name = []
            
            
            
            print("Checking database for students with paid slip..")
            sleep(1)
            print("Checked")
            cursor.execute("DROP TABLE NEWREGISTER")

            cursor.execute("""CREATE TABLE IF NOT EXISTS TESTSTUD(
            STUDID INTEGER PRIMARY KEY AUTOINCREMENT, 
            NAME TEXT,
            AGE INTEGER,
            DEPT TEXT,
            EMAIL TEXT,
            PHONO INTEGER,
            PARMAIL TEXT,
            PARENTNO INTEGER,
            EXAMRESULT	TEXT,
	        ATTENDANCE	INTEGER
            )""")
            for each in reg:
                cursor.execute("""INSERT INTO TESTSTUD (NAME,AGE,DEPT,EMAIL,PHONO,PARMAIL,PARENTNO)
                VALUES (?,?,?,?,?,?,?,?)
                """,(each[1],each[2],each[10],each[3],each[4],each[7],each[8]))
                conn.commit()
            
            print("Admission Done")
        except Error:
            print("NO DATABASE in NEW REGISTERS TO FILL")
        finally:
            
            conn.close()

# Curriculam
    def _timetable(self):
        #auth = self._authorize()
        if 1 == 1 :
            try:
                conn = self.openconnection()
                cursor = conn.cursor()
                cursor.execute("""
                    CREATE TABLE OF NOT EXISTS SEM1 (
	                "TIME"	TEXT,
	                "MONDAY"	TEXT,
	                "TUESDAY"	TEXT,
	                "WEDNESDAY"	TEXT,
	                "THURSDAY"	TEXT,
	                "FRIDAY"	TEXT,
	                "SATURDAY"	TEXT,
	                PRIMARY KEY("TIME")
                )""")
                conn.commit()
                print("Table Created")
            except Error: 
                print("Something went wrong")
            finally:
                print("Update Time Table Module is not Updated")
                conn.close()






 # view time table
    def viewtimetable(self):
        sem = 1#int(input("ENTER THE SEM : "))
        sem = "SEM"+str(sem)
        try:
            conn = self.openconnection()
            cursor = conn.cursor()
            cursor.execute(f"SELECT * FROM {sem}")
            timetable = cursor.fetchall()
            loop = tqdm(total = 100,position = 0 ,leave = False)
            for k in range(100):
                loop.set_description("PLEASE WAIT Getting list")
                sleep(.02)
                loop.update(1)
            loop.close()
            print("  TIME        MONDAY       TUESDAY        WEDNESDAY    THURSDAY      FRIDAY         SATURDAY")
            
            for each in timetable:
                print(each[0],"    ",each[1],"    ",each[2],"    ",each[3],"    ",each[4],"    ",each[5],"    ",each[6])
        except Error:
            print(Error)
        finally:
            conn.close()




 # Update Events

    def _updateeventsinput(self):
        
        try:
            month = input("Enter the Month : ").upper()
            if month == '0':
                print("Month cannot be zero")
                self._updateeventsinput()
            if month == '1' or month == 'JANUARY' or month == 'JAN':
                day = int(input("Enter the Date of the Event : "))
                if day in range(1,32):
                    date = day
                    month = '1'
                else:
                    print("January has only 31 days")
                    self._updateeventsinput()
            if month == '2' or month == 'FEBRUARY' or month == 'FEB':
                day = int(input("Enter the Date of the Event : "))
                if day in range(1,29):
                    date = day
                    month = '2'
                else:
                    print("February has only 28 days")
                    self._updateeventsinput()
            if month == '3' or month == 'MARCH' or month == 'MAR':
                day = int(input("Enter the Date of the Event : "))
                if day in range(1,32):
                    date = day
                    month = '3'
                else:
                    print("March has only 31 days")
                    self._updateeventsinput()
            if month == '4' or month == 'APRIL' or month == 'APR':
                day = int(input("Enter the Date of the Event : "))
                if day in range(1,31):
                    date = day
                    month = '4'
                else:
                    print("April has only 30 days")
                    self._updateeventsinput()
            if month == '5' or month == 'MAY' :
                day = int(input("Enter the Date of the Event : "))
                if day in range(1,32):
                    date = day
                    month = '5'
                else:
                    print("May has only 31 days")
                    self._updateeventsinput()
            if month == '6' or month == 'JUNE' :
                day = int(input("Enter the Date of the Event : "))
                if day in range(1,31):
                    date = day
                    month = '6'
                else:
                    print("June has only 30 days")
                    self._updateeventsinput()

            if month == '7' or month == 'JULY' :
                day = int(input("Enter the Date of the Event : "))
                if day in range(1,32):
                    date = day
                    month = '7'
                else:
                    print("July has only 31 days")
                    self._updateeventsinput()
            if month == '8' or month == 'AUGUST' or month == 'AUG':
                day = int(input("Enter the Date of the Event : "))
                if day in range(1,32):
                    date = day
                    month = '8'
                else:
                    print("August has only 31 days")
                    self._updateeventsinput()
            if month == '9' or month == 'SEPTEMBER' or month == 'SEPT':
                day = int(input("Enter the Date of the Event : "))
                if day in range(1,31):
                    date = day
                    month = '9'
                else:
                    print("September has only 30 days")
                    self._updateeventsinput()
            if month == '10' or month == 'OCTOBER' or month == 'OCT':
                day = int(input("Enter the Date of the Event : "))
                if day in range(1,32):
                    date = day
                    month = '10'
                else:
                    print("October has only 31 days")
                    self._updateeventsinput()
            if month == '11' or month == 'NOVEMBER' or month == 'NOV':
                day = int(input("Enter the Date of the Event : "))
                if day in range(1,31):
                    date = day
                    month = '11'
                else:
                    print("November has only 30 days")
                    self._updateeventsinput()
            if month == '12' or month == 'DECEMBER' or month == 'DEC':
                day = int(input("Enter the Date of the Event : "))
                if day in range(1,32):
                    date = day
                    month = '12'
                else:
                    print("December has only 31 days")
                    self._updateeventsinput()
            #date = int(input("Enter the date of the event : "))
            date1 = day
            month1 = month
            print("checking")
            sleep(0.3)
            if int(month)  in  range(1,13):
                
                x = datetime.datetime.now()
                return f"{date1}/{month1}/{x.year}"
            else:
                print("A year has only 12 Months")
            
        except Exception:
            print("Enter Details Properly")
            self._updateeventsinput()







    def _eventdetailsinput(self):
        try:
            event = input("Enter the Event Details : ")
        except ValueError:
            print("Enter Details Properly")
        finally:
            return event







    def updateevent(self):
        _date = self._updateeventsinput()
        _event = self._eventdetailsinput()
        print(_date , "\n", _event)
        try:    
            conn = self.openconnection()
            cursor = conn.cursor()
            cursor.execute("""CREATE TABLE IF NOT EXISTS EVENTS(
                DATE TEXT,
                EVENT TEXT
            )""")
            print(f"""            DATE        ||      EVENT
            {_date}           {_event}""")
            print("Adding event ...")
            cursor.execute("INSERT INTO EVENTS (DATE,EVENT) VALUES (?,?)",(_date,_event))
            conn.commit()
            sleep(1)
            print("Added !")
        except Exception:
            print("Something went wrong..!")
        finally:
            conn.close()







    def showevent(self):
        try:
            
            conn = self.openconnection()
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM EVENTS ORDER BY DATE")
            event = cursor.fetchall()
            print("  DATE               EVENT")
            for each in event:
                print(each[0] ,"         ",each[1])
        except:
            pass