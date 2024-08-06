import csv

def load_csv(csv_path: str):
    with open(csv_path, newline = '') as csvfile:
        result = [row for row in csv.DictReader(csvfile)]

    return result