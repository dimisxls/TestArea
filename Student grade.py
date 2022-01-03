from random import randrange, seed
from datetime import datetime


class Student:
    def __init__(self, full_name, grade=-1):
        self.full_name = full_name
        self.grade = grade


def grade_student(student_a):
    student_a.grade = randrange(0, 11)
    print(student_a.full_name, student_a.grade)


def average(students_b):
    s = 0
    for student_c in students_b:
        s += student_c.grade

    print('\nAverage: ' + str(s/len(students)))

names=['Enrique Mckee',
'Jareth Hampton',
'Kelsie Benitez',
'Nolan Callahan',
'Akshay Lowe',
'Olly Plant',
'Landon Mullen',
'Huxley Guevara',
'Eisa Neale',
'Hana Robin']


students = [Student(names[i]) for i in range(len(names))]
print(students[1].grade)

print("*"*20)

for student in students:
    grade_student(student)

average(students)
