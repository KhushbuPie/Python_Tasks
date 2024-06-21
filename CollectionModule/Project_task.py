import csv
from collections import namedtuple

# Utilize `namedtuple` for representing rows of your CSV data, making them more accessible and readable

with open("studentdata.csv", mode="r") as file:
    csv_reader = csv.reader(file)
    header=next(csv_reader)
    reader1 = csv.reader(file)
    student=namedtuple('student',header)

    list_csv=list(reader1)

    for i in range(5):
        # print(student._make(list_csv[i]))
        s=student._make(list_csv[i]) 

    students=[student._make(row) for row in list_csv]

    for s in students:
        print(s)

    names =[s.Name for s in students]
    print("\nNames of all student")
    for name in names:
        print(name)
"""
o/p:
student(id='1', Name='Nikhil', Branch='COE', Year='2', CGPA='9.0')
student(id='2', Name='Sanchit', Branch='COE', Year='2', CGPA='9.1')
student(id='3', Name='Aditya', Branch='IT', Year='2', CGPA='9.3')
student(id='4', Name='Sagar', Branch='SE', Year='1', CGPA='9.5')
student(id='5', Name='Prateek', Branch='MCE', Year='3', CGPA='7.8')

Names of all student
Nikhil
Sanchit
Aditya
Sagar
Prateek
Sahil
"""
      