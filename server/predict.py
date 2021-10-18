from model.lsi import LsiEstimator
from adapter.inference import CSVInferenceAdapter
import csv

model = None

def main():
    global model
    print("initializing model...")
    # model = FNNSimpleEstimator()
    model = LsiEstimator()
    options = {}
    adapter = CSVInferenceAdapter(options)
    model.set_adapter(adapter)
    # model.load("models/fnn_simple")
    model.load("models/lsi")

    with open('../data/training_data/predict_data.csv', 'w', newline='') as csvfile:
        # 建立 CSV 檔寫入器
        writer = csv.writer(csvfile)

        writer.writerow(['url', 'input', 'type'])

        with open('../data/training_data/unlabel_data.csv', newline='') as data_csv:
            reader = csv.reader(data_csv)
            data = list(reader)

            for record in data:
                url = record[0]

                if 'http' not in url:
                    continue

                model.adapter.set_options([record])
                estimated_topic = model.predict()

                writer.writerow([url, record[1], estimated_topic])


if __name__ == "__main__":
    main()
