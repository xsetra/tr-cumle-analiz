#! /usr/bin/env python3
# -*- coding: utf-8 -*-


from kelime import *
from cumle import Cumle
from paragraf import Paragraf
from mysql import Veritabani

dokuman = Paragraf()
db = Veritabani()

db.baglan()
db.kelime_bilgi(dokuman)

dokuman.cumleleri_yaz()
