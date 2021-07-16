import mysql.connector
from os import system, name 
import random
from time import sleep 

#DB Connection
mydb = mysql.connector.connect(host='localhost', port='3306', user='root', passwd='root', database='quiz')
mycursor = mydb.cursor()
 
def clear(): 
    if name == 'nt': 
        _ = system('cls')
    else: 
        _ = system('clear')

def createAdmin(username, password):
	try:
		mycursor.execute(f"INSERT INTO admin(username, pass) VALUES('{username}', '{password}')")
		mydb.commit()
		print('			Admin Created\n     			Loading ...')
		sleep(1)
	except Exception as e:
		print(e)


def createTeacher(username, password, name = 'NULL'):
	try:
		mycursor.execute(f"INSERT INTO teacher(name, username, pass) VALUES('{name}', '{username}', '{password}')")
		mydb.commit()
		print('			Teacher Added\n     			Loading ...')
		sleep(1)
	except Exception as e:
		print(e)

def createStudent(roll, password, name = 'NULL'):
	try:
		mycursor.execute(f"INSERT INTO student(name, roll, pass) VALUES('{name}', '{roll}', '{password}')")
		mydb.commit()
		print('			Student Create\n				Loading ...')
		sleep(1)
	except Exception as e:
		print(e)

def AddQuestion(question, ans, op1, op2, op3):
	try:
		mycursor.execute(f"INSERT INTO question VALUES('{question}', '{op1}', '{op2}', '{op3}', '{ans}')")
		mydb.commit()
		print('			Question Added\n				Loading ...')
		sleep(1)
	except Exception as e:
		print(e)


def login():
	clear()
	print("\n		Choose Any Option\n")
	login_option = int(input("""
		1. Login as Admin
		2. Login as Teacher
		3. Login as Students
		"""))
	clear()
	print("\n		 LOGIN PAGE\n")
	if login_option==1:
		user = input("	Username : ")
		mycursor.execute(f"SELECT * FROM admin WHERE username = '{user}'")
		passwd = input("	Password : ")
		for usr in mycursor:
			if usr[1] == passwd:
				return 'ADMIN'
			else:
				print("	Wrong Username or Password ! ")
				sleep(1)
				startFrom()
	elif login_option == 2:
		user = input("	Username : ")
		mycursor.execute(f"SELECT * FROM teacher WHERE username = '{user}'")
		passwd = input("	Password : ")
		for usr in mycursor:
			if usr[1] == passwd:
				return 'TEACHER'
			else:
				print("	Wrong Username or Password ! ")
				sleep(1)
				startFrom()
	elif login_option == 3:
		roll = input("	Roll No : ")
		mycursor.execute(f"SELECT * FROM student WHERE roll = '{roll}'")
		passwd = input("	Password : ")
		for usr in mycursor:
			if usr[2] == passwd:
				return 'STUDENT'
			else:
				print("    Wrong Roll No or Password ! ")
				sleep(1)
				startFrom()
	else:
		startFrom()


def AdminPanel():
	clear()
	print("\n				ADMIN PANEL\n")
	inp = int(input("""
		1. Create Admin
		2. Create Teacher
		3. Create Student
		4. Log Out
		"""))
	if inp == 1:
		print("""\n			CREATE ADMIN USER\n""")
		createAdmin(input("    Enter Username: "), input("    Enter Password: "))
		AdminPanel()
	if inp == 2:
		print("""\n			ADD TEACHER\n""")
		createTeacher(input("    Enter Username: "), input("    Enter Password: "), input("    Enter Name: "))
		AdminPanel()
	if inp == 3:
		print("""\n			ADD STUDENT\n""")
		createStudent(input("    Enter Roll No: "), input("    Enter Password: "), input("    Enter Name: "))
		AdminPanel()
	elif inp == 4:
		startFrom()
	else:
		AdminPanel()


def TeacherPanel():
	clear()
	print("\n				ADD QUESTIONS\n")
	x = int(input("""
		1. Add Question
		2. Logout
		"""))
	if x==1:
		AddQuestion(input("Enter Question 	: "), input("Enter Right Answer : "), input("Enter wrong Option 1"), input("Enter wrong Option 2"), input("Enter wrong Option 3"))
		TeacherPanel()
	elif x==2:
		startFrom()
	else:
		TeacherPanel()

def StudentPanel():
	mycursor.execute(f"SELECT * FROM question")
	for q in mycursor:
		clear()
		print("\n				QUESTION\n")
		print("Q.  ",q[0])
		print()
		randomop = random.sample(q[1:], 4)
		for index, op in enumerate(randomop):
			print(f'  OP {index}: {op}')
		print()
		cop = int(input("Enter Your Choice : "))
		if randomop[cop] == q[4]:
			print("\n 		Right Answer !!!\n")
		else:
			print("\n 		Wrong Answer !!!\n")

		cc = int(input("  Press 7 for Continue\n  Press 9 for Exit"))
		if cc == 9:
			break



def startFrom():
	login_status = login()
	clear()
	if login_status == 'ADMIN':
		AdminPanel()
	elif login_status == 'TEACHER':
		TeacherPanel()
	elif login_status == 'STUDENT':
		StudentPanel()
	else:
		startFrom()

if __name__ == "__main__":
	startFrom()