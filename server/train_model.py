from model.fnn_simple import FNNSimpleEstimator
from model.lsi import LsiEstimator
from adapter.training import CSVTrainingAdapter


def main():
    model = 'lsi'
    if model == 'fnn':
        model = FNNSimpleEstimator()
        options = {
            'ratio_test': 0.2,
            'seed': 100,
        }

        adapter = CSVTrainingAdapter(options)
        model.set_adapter(adapter)
        model.train({'epochs': 400, 'verbose': 0})
        model.save("./models/fnn_simple")
    elif model == 'lsi':
        model = LsiEstimator()
        options = {
            'ratio_test': 0.2,
            'seed': 100,
        }
        adapter = CSVTrainingAdapter(options)
        model.set_adapter(adapter)
        model.train()
        model.save("./models/lsi")


if __name__ == "__main__":
    main()
