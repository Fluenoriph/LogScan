import csv


users = [
    {"name": "Tom", "age": 28},
    {"name": "Alice", "age": 23},
    {"name": "Bob", "age": 34}
]

with open('users.csv', 'w', newline='', encoding='utf-8') as file:
    columns = ['name', 'age']
    writer = csv.DictWriter(file, fieldnames=columns)
    writer.writeheader()
    writer.writerows(users)