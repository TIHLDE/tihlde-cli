import csv


def read_csv(file_path: str) -> list:
    """Read a CSV file"""
    with open(file_path, newline="") as file:
        reader = csv.reader(file)
        print(reader.line_num)
        return list(reader)