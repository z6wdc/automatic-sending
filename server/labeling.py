from model.lsi import LsiEstimator
from adapter.inference import CSVInferenceAdapter
import csv
import pathlib

model = None


def labeling():
    global model
    print("initializing model...")
    model = LsiEstimator()
    options = {}
    adapter = CSVInferenceAdapter(options)
    model.set_adapter(adapter)
    model.load("../server/models/lsi")

    with open('../data/result/labeled_data.csv', 'w', newline='') as csvfile:
        # 建立 CSV 檔寫入器
        writer = csv.writer(csvfile)

        with open('../data/result/html_data.csv', newline='') as data_csv:
            reader = csv.reader(data_csv)
            data = list(reader)

            for record in data:
                url = record[1]

                if 'http' not in url:
                    continue

                model.adapter.set_options([[record[1], record[3]]])
                estimated_topic = model.predict()

                writer.writerow([record[0], record[1], record[2], record[3], estimated_topic])
