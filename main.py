#! /usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
from tranaliz.sentences import Sentence
from tranaliz.words import Word
from tranaliz.analyse import Analyser

tranaliz = Analyser()

# Take file name on parameters
if len(sys.argv != 1):
    tranaliz.fileName = sys.argv[1]


