import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="Digipie"
)
rows = [['1','Nikhil', 'COE', '2', '9.0'],
        ['2','Sanchit', 'COE', '2', '9.1'],
        ['3','Aditya', 'IT', '2', '9.3'],
        ['4','Sagar', 'SE', '1', '9.5'],
        ['5','Prateek', 'MCE', '3', '7.8'],
        ['6','Sahil', 'EP', '2', '9.1']]

mycursor = mydb.cursor()

# sql = "Insert into student (name,Branch,year,CGPA) values(%s,%s,%s,%s)"
# val = ("Nikhil","COE",2,9.0)

# enter list data into database
for item in rows:
    sql = "Insert into student (name,Branch,year,CGPA) values(%s,%s,%s,%s)"
    val = (item[1],item[2],item[3],item[4])
    mycursor.execute(sql,val)
    mydb.commit()

