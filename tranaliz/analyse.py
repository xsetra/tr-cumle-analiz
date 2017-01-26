# -*- coding: utf-8 -*-

from sentences import Sentence
from words import Word

class Analyser:
    # Global class
    def __init__(self, filename="requirements.txt"):
        self.sentences = []
        self.content = ""
        self.fileName = filename

    def read_file(self):
        file_obj = open(self.fileName, 'r')
        self.content = file_obj.read()

    def divide_content(self):
        list_sentence = self.content.split('.')

