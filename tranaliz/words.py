# -*- coding: utf-8 -*-


class Word:
    parentSentenceIndex = 0

    def __init__(self):
        self.wordIndex = 0
        self.wordContent = ""
        self.wordType = ""
        self.wordRoot = ""
        self.wordEclair = []

    def add_word_info(self, index, content, parent_index, word_type, root):
        self.parentSentenceIndex = parent_index
        self.wordContent = content
        self.wordIndex = index
        self.wordType = word_type
        self.wordRoot = root

    def add_eclair(self, eclair):
        for addition in eclair:
            self.wordEclair.append(addition)
