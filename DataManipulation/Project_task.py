import csv
from collections import defaultdict

# Read CSV data into a list of dictionaries
data = []
with open('data.csv', 'r') as file:
    reader = csv.DictReader(file)
    for row in reader:
        # Convert Year and CGPA to appropriate types
        row['Year'] = int(row['Year']) if row['Year'] != 'NaN' else None
        row['CGPA'] = float(row['CGPA']) if row['CGPA'] != 'NaN' else None
        data.append(row)

# Filter 
filtered_data = [entry for entry in data if entry['CGPA'] is not None]

# Sort 
sorted_data = sorted(filtered_data, key=lambda x: x['CGPA'], reverse=True)

# Get the top 10 entries with the highest CGPA
top_10_data = sorted_data[:10]

# Group the top 10 data by branch
grouped_data = defaultdict(list)
for entry in top_10_data:
    grouped_data[entry['Branch']].append(entry)

# Print the grouped data
for branch, entries in grouped_data.items():
    print(f"\nBranch: {branch}")
    for entry in entries:
        print(entry)

# To save the results into a CSV file (optional)
with open('top_10_grouped_by_branch.csv', 'w', newline='') as file:
    fieldnames = ['id', 'Name', 'Branch', 'Year', 'CGPA']
    writer = csv.DictWriter(file, fieldnames=fieldnames)
    
    writer.writeheader()
    for branch, entries in grouped_data.items():
        for entry in entries:
            writer.writerow(entry)
