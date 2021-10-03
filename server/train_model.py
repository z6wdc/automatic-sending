from model.fnn_simple import FNNSimpleEstimator
from adapter.training import CSVTrainingAdapter


def main():
    model = FNNSimpleEstimator()
    options = {
        'ratio_test': 0.2,
        'seed': 100,
    }

    adapter = CSVTrainingAdapter(options)
    model.set_adapter(adapter)
    model.train({'epochs': 400, 'verbose': 0})
    model.save("./models/fnn_simple")


if __name__ == "__main__":
    main()
