import csv

with open('data.csv', 'r') as file:
    reader = csv.DictReader(file)
    for row in reader:
        name = row['Name']
        age = row['Age']
        email = row['Email']
        print(f"Name: {name}, Age: {age}, Email: {email}")
