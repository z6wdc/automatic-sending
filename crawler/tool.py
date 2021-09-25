import csv

data = []

def read_csv_file(path, header=False):
    data = []
    with open(path) as f:
        reader = csv.reader(f)
        for row in reader:
            data.append(row[:2])
    
    return data if header else data[1:]
