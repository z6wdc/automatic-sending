# -*- coding: utf-8 -*-
import re
import MeCab
from bs4 import BeautifulSoup

# Work Around for mecab-python3 bug
# https://shogo82148.github.io/blog/2015/12/20/mecab-in-python3-final/
tokenizer = MeCab.Tagger("")
tokenizer.parse('')


class InputTagTokenizer(object):
    def __init__(self):
        self.tokenizer = tokenizer
        self.target_attributes = ['name', 'type', 'id', 'value',
                                  'alt', 'placeholder', 'aria-label']
        self.exclude_words = ["", ".", "(", ")", "/", "\n", "text"]

    def mecab_tokenize(self, text):
        ret = []
        node = self.tokenizer.parseToNode(text)
        while node:
            feats = node.feature.split(",")
            if feats[0] in ['名詞']:
                ret.append(node.surface)
            node = node.next
        return ret

    def get_attrs_value(self, html):
        html_soup = BeautifulSoup(html, 'html.parser')
        words = []

        s = html_soup.find('input')
        if s is not None:
            words.extend(self.__attrs_values_from_input(s))

        s = html_soup.find('option')
        if s is not None:
            words.extend(self.__attrs_values_from_option(s))

        s = html_soup.find('textarea')
        if s is not None:
            words.extend(self.__attrs_values_from_textarea(s))

        return words

    def __attrs_values_from_input(self, input_tag):
        words = []
        for k in self.target_attributes:
            if (k not in input_tag.attrs) or (input_tag.attrs[k] == ''):
                continue

            for token in self.__preprocess(input_tag.attrs[k]):
                words.append(token)

        return words

    def __attrs_values_from_textarea(self, textarea_tag):
        words = []
        for k in self.target_attributes:
            if (k not in textarea_tag.attrs) or (textarea_tag.attrs[k] == ''):
                continue

            for token in self.__preprocess(textarea_tag.attrs[k]):
                words.append(token)

        return words

    def __attrs_values_from_option(self, option_tag):
        words = []

        target_attr = ['value', 'label']
        for k in target_attr:
            if (k not in option_tag.attrs) or (option_tag.attrs[k] == ''):
                continue

            for token in self.__preprocess(option_tag.attrs[k]):
                words.append(token)

        return words

    def __convert_to_snake(self, name):
        s1 = re.sub('(.)([A-Z][a-z]+)', r'\1_\2', name)
        return re.sub('([a-z0-9])([A-Z])', r'\1_\2', s1).lower()

    def __preprocess(self, value):
        snake_case_value = self.__convert_to_snake(value)
        snake_case_value = re.sub(r'([0-9]+)', r'_\1', snake_case_value)
        tokens = re.split(r'[-_\]\[/ ]', snake_case_value)
        for t in tokens:
            japanese_tokens = self.mecab_tokenize(t)
            for j_t in japanese_tokens:
                if j_t in self.exclude_words:
                    continue
                yield j_t


if __name__ == "__main__":
    print("preprocessor")
