import csv
import os


def read_csv_data(file_name):
    rows = []
    file_path = os.path.join(os.path.dirname(__file__), '..', 'data', file_name)
    with open(file_path, mode='r', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            rows.append(row)

    return rows

