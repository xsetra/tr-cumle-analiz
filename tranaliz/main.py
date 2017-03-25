#! /usr/bin/env python3
# -*- coding: utf-8 -*-


from kelime import Kelime
from kelime import KelimeTipi
from cumle import Cumle
from paragraf import Paragraf
from mysql import Veritabani
from ruleset import Ruleset

dokuman = Paragraf()
db = Veritabani()

db.baglan()
db.kelime_bilgi(dokuman)

#dokuman.cumleleri_listele()


