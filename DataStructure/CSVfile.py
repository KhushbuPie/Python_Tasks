import csv
with open('example.csv', mode='r') as file:
    csvFile = csv.reader(file)
    for lines in csvFile:
        print(lines)

# import csv
fields = ['id','Name', 'Branch', 'Year', 'CGPA']

rows = [['1','Nikhil', 'COE', '2', '9.0'],
        ['2','Sanchit', 'COE', '2', '9.1'],
        ['3','Aditya', 'IT', '2', '9.3'],
        ['4','Sagar', 'SE', '1', '9.5'],
        ['5','Prateek', 'MCE', '3', '7.8'],
        ['6','Sahil', 'EP', '2', '9.1']]

filename = "studentdata.csv"

with open(filename,mode="w") as file:
    csvwriter = csv.writer(file)
    csvwriter.writerow(fields)
    csvwriter.writerows(rows)

