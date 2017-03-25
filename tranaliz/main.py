#! /usr/bin/env python3
# -*- coding: utf-8 -*-


from kelime import *
from cumle import Cumle
from paragraf import Paragraf
from mysql import Veritabani
from ruleset import Ruleset

dokuman = Paragraf()
db = Veritabani()
rules = Ruleset()

db.baglan()
db.kelime_bilgi(dokuman)

dokuman.cumleleri_yaz()
