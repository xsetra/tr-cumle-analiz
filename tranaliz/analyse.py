# -*- coding: utf-8 -*-

from sentences import Sentence
from words import Word

if __name__ == '__main__':
    class Analyser:
        # Global class
        def __init__(self, filename="requirements.txt"):
            self.sentences = []
            self.content = ""
            self.fileName = filename

        def read_file(self):
            file_obj = open(self.fileName, 'r')
            self.content = file_obj.read()

        def divide_to_sentence(self):
            list_sentence = self.content.split('.')
            for cumle in list_sentence:
                self.divide_to_word(cumle)

        def divide_to_word(self, cumle):

            for kelime in list_word:
                pass
                # Zemberekten gelecek veriler ve sonucların kelime sınıfına girilmesi
                #


