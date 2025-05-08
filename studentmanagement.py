from random import choice
from tkinter.font import names
import mysql.connector
conn = mysql.connector.connect(
host="localhost",
user="root",
password="sindhusindhu143",
database="django_db"
)
cursor = conn.cursor()
def add_student():
    id = input("enter the id:")
    name=input('enter name:')
    age=input('enter age:')
    grade=input('enter a grade:')
    cursor.execute("insert into students(id,name,age,grade)values(%s,%s,%s,%s)",(id,name,age,grade))
    conn.commit()
    print("students added.")
def view_students():
    cursor.execute("select * from students")
    for student in cursor.fetchall():
        print(student)
def update_students():
    students_id = input("enter student id to update:")
    name = input("new name:")
    age = input("new age:")
    grade = input("new grade:")
    cursor.execute("update students set name=%s, age=%s where id=%s",(name,age,grade,students_id))
    conn.commit()
    print("student update,")
def delete_students():
        students_id = input("enter student id to delete:")
        cursor.execute("delete from students where id=%s",(students_id,))
        conn.commit()
        print("students deleted.")
def menu():
    while True:
                print("\n---student management system---")
                print("1.add student")
                print("2.view students")
                print("3.update students")
                print("4.delete students")
                print("5.exit")
                choice = input("enter choice:")
                if choice == '1':
                    add_student()
                elif choice == '2':
                    view_students()
                elif choice == '3':
                    update_students()
                elif choice == '4':
                    delete_students()
                elif choice == '5':
                    break
                else:
                    print("invalid choice.")
menu()


