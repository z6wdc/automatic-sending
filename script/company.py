import csv
import glob

def generate_company_list():
    """
    Generate the company list from the result csv file.
    """
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

def get_label():
    """
    List the label's name.
    """
    data = []
    with open('./data/training_data/labeled_data.csv') as f:
            reader = csv.reader(f)
            for index, row in enumerate(reader):
                if index == 0:
                    continue
                data.append(row[2].lower())

    print(set(data))
    print(len(set(data)))

if __name__ == '__main__':
    get_label()
