import csv
import glob

csv_list = glob.glob('./data/result-*.csv')

data = []
for path in csv_list:
    with open(path) as f:
        reader = csv.reader(f)
        for index, row in enumerate(reader):
            if index == 0:
                continue
            data.append(row[:2])

with open('./data/company_list.csv', 'w') as f:
    writer = csv.writer(f)
    writer.writerow(['企業名', 'URL'])
    for row in data:
        writer.writerow(row)
