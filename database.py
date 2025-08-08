import csv
import os
# local database functionality 
class database:
    def __init__(self, dni, password, name):
        self.dni = dni
        self.password = password
        self.name = name

    def save(self):
        with open('local_database.csv', mode='a', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow([self.dni, self.password, self.name])

    def show(self):
        rows = []
        if os.path.exists('local_database.csv'):
            with open('local_database.csv', mode='r', newline='', encoding='utf-8') as file:
                reader = csv.reader(file)
                for row in reader:
                    rows.append(row)
        return rows
