import csv 
from collections import defaultdict #dict nad defaultdict is same but defaultdict is never raises KeyError

categorized_data = defaultdict(list)

with open('studentdata.csv', mode="r") as file:
    csv_reader = csv.DictReader(file) #csv.DictReader to read the file as dict

    for row in csv_reader:
        Branch = row['Branch']
        categorized_data[Branch].append(row)

for Branch, records in categorized_data.items():
    print(f"\nBranch: {Branch}")
    for record in records:
        print(record)

"""DataStructure
o/p:
Branch: COE
{'id': '1', 'Name': 'Nikhil', 'Branch': 'COE', 'Year': '2', 'CGPA': '9.0'}
{'id': '2', 'Name': 'Sanchit', 'Branch': 'COE', 'Year': '2', 'CGPA': '9.1'}

Branch: IT
{'id': '3', 'Name': 'Aditya', 'Branch': 'IT', 'Year': '2', 'CGPA': '9.3'}

Branch: SE
{'id': '4', 'Name': 'Sagar', 'Branch': 'SE', 'Year': '1', 'CGPA': '9.5'}

Branch: MCE
{'id': '5', 'Name': 'Prateek', 'Branch': 'MCE', 'Year': '3', 'CGPA': '7.8'}

Branch: EP
{'id': '6', 'Name': 'Sahil', 'Branch': 'EP', 'Year': '2', 'CGPA': '9.1'}
"""
