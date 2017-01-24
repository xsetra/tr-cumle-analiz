# -*- coding: utf-8 -*-


class Sentence:

    def __init__(self):
        self.sentenceIndex = 0
        self.sentenceContent = ""
        self.words = []

    def add_sentence_info(self, index, content):
        self.sentenceContent = content
        self.sentenceIndex = index

    def add_word(self, word):
        if word.parentSentenceIndex == self.sentenceIndex:
            self.words.append(word)
        else:
            exit(10)




