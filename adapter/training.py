from abc import abstractmethod
from gensim import corpora
from adapter.base import Adapter
import csv
import numpy as np


class TrainingAdapter(Adapter):
    def __init__(self, options):
        super().__init__()
        (self.be_train,
         self.ot_train,
         self.meta_train,
         self.be_test,
         self.ot_test,
         self.meta_test) = self.generate_training_data(options)

    @abstractmethod
    def generate_training_data(self, options):
        pass


class CSVTrainingAdapter(TrainingAdapter):
    def generate_training_data(self, options):
        """
        set self.dictionary, self.lable_types and
        generate train_x(y) and test_x(y)
        """
        with open('../data/training_data/labeled_data.csv', newline='') as data_csv:
            reader = csv.reader(data_csv)
            data = list(reader)

        word_vecs = self.convert_to_word_vecs(data)
        topic_vecs = self.convert_to_topic_vecs(data)
        meta_vecs = self.convert_to_meta_vecs(data)
        assert(len(word_vecs) == len(topic_vecs))
        assert(len(meta_vecs) == len(topic_vecs))

        # use dictionary and topic_types of training set
        wv_flatten = []
        for x in word_vecs:
            wv_flatten.extend(x)
        self.dictionary = corpora.Dictionary(wv_flatten)

        tp_flatten = []
        for x in topic_vecs:
            tp_flatten.extend(x)
        self.all_topics = list(set(tp_flatten))

        # select test data
        num_pages = len(word_vecs)
        print("number of total pages: " + str(num_pages))
        np.random.seed(options['seed'])
        ratio_test = options['ratio_test']
        num_test_pages = int(num_pages * ratio_test)
        test_indices = np.random.permutation(num_pages)[0:num_test_pages]

        word_vecs_train = []
        topic_vecs_train = []
        meta_train = []
        word_vecs_test = []
        topic_vecs_test = []
        meta_test = []
        for i in range(0, num_pages):
            if i not in test_indices:
                word_vecs_train.append(word_vecs[i])
                topic_vecs_train.append(topic_vecs[i])
                meta_train.append(meta_vecs[i])
            else:
                word_vecs_test.append(word_vecs[i])
                topic_vecs_test.append(topic_vecs[i])
                meta_test.append(meta_vecs[i])

        be_train = self.to_bow_element_vectors(word_vecs_train)
        ot_train = self.to_one_hot_topic_vectors(topic_vecs_train)
        be_test = self.to_bow_element_vectors(word_vecs_test)
        ot_test = self.to_one_hot_topic_vectors(topic_vecs_test)

        return (be_train, ot_train, meta_train, be_test, ot_test, meta_test)
