#! /usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
from tranaliz.sentences import Sentence
from tranaliz.words import Word


# Take file name on parameters
if len(sys.argv) == 1:
    file_name = "requirements.txt"
else:
    file_name = sys.argv[1]

file_obj = open(file_name, 'r')
