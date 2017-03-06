#! /usr/bin/env python3
# -*- coding: utf-8 -*-


from kelime import *
from cumle import Cumle
from paragraf import Paragraf
import pymysql


host = "localhost"
un = "root"
pw = "ziniba"
db_name = "fatmabozyigit"


dokuman = Paragraf()
db = pymysql.connect(host, un, pw, db_name)
cursor = db.cursor()


dosya = open("requirements.txt", "r")
dokuman.paragrafIcerik = dosya.read()


dokuman.icerik_bol()
dokuman.cumleler[0].kelimeleri_yaz()

