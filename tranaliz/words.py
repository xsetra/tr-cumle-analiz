# -*- coding: utf-8 -*-


class Word:
    parentSentenceIndex = 0

    def __init__(self):
        self.wordIndex = 0
        self.wordContent = ""
        self.wordType = ""
        self.wordFrequency = 0

    def add_word_info(self, index, content, parent_index, word_type):
        self.parentSentenceIndex = parent_index
        self.wordContent = content
        self.wordIndex = index
        self.wordType = word_type

    def increase_frequency(self, value=1):
        self.wordFrequency += value
