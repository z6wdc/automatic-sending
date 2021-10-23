from abc import abstractmethod
from adapter.base import Adapter


class InferenceAdapter(Adapter):
    def __init__(self, options):
        super().__init__()
        self.options = options
        self.inference = True

    def set_options(self, options):
        self.options = options

    @abstractmethod
    def get_bow_element_vectors(self):
        pass


class CSVInferenceAdapter(InferenceAdapter):
    def get_bow_element_vectors(self):
        # record = self.options['record']
        word_vecs = self.convert_to_word_vecs(self.options)
        return self.to_bow_element_vectors(word_vecs)