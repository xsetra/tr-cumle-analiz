# -*- coding: utf-8 -*-


import pymysql
from kelime import Kelime
from kelime import KelimeTipi
from cumle import Cumle
from paragraf import Paragraf


class Veritabani:
    def __init__(self):
        self.hostname = "localhost"
        self.username = "root"
        self.password = "ziniba"
        self.database_name = "fatma_turkish"
        self.obj_db = None
        self.cursor = None

    def baglan(self):
        self.obj_db = pymysql.connect(host=self.hostname,
                                      user=self.username,
                                      passwd=self.password,
                                      db=self.database_name,
                                      charset='latin5')
        self.cursor = self.obj_db.cursor()

    def kapat(self):
        self.obj_db.close()
        print("Veritabanı bağlantısı kapatıldı.")

    def kelime_tipi_sorgula(self):
        if self.obj_db is None:
            return "Veritabanı bağlantısı kurmadan sorgulama yapamazsınız"
        else:
            # SQL sorgu cümlecikleri eklenip deger donecek
            pass

    def kelime_bilgi(self, paragraf):
        query = "SELECT * FROM kelimeler"
        self.cursor.execute(query)
        results = self.cursor.fetchall()
        for row in results:
            c_index = row[4]
            cumle = paragraf.search_index(c_index)
            if cumle is None:
                cumle = paragraf.cumle_ekle(index=c_index, icerik="DB Data")
            k_index = row[5]
            kelime = row[1]
            k_tip = row[2]
            cumle.kelime_ekle(index=k_index, kelime_icerik=kelime, tip=k_tip)

    def isim_ve_fiil_cek(self, paragraf):
        query = "SELECT * FROM kelimeler WHERE tip='{}' or tip='{}'".format(KelimeTipi.isim.value, KelimeTipi.fiil.value)
        self.cursor.execute(query)
        results = self.cursor.fetchall()
        for row in results:
            ekle = 1
            k = Kelime()
            k.kelimeIndex = row[0]
            k.kelimeIcerik = str(row[1])
            tip = row[2]
            k.kelimeEk = str(row[3])
            k.kelimeFreq = self.frekans_degeri_ver(k.kelimeIcerik)

            if tip == KelimeTipi.isim.value:
                k.kelimeTipi = KelimeTipi.isim
                for i in paragraf._isimler:
                    if i.kelimeIcerik == k.kelimeIcerik:
                        ekle = 0
                        break
                if ekle == 1:
                    paragraf._isimler.append(k)

            elif tip == KelimeTipi.fiil.value:
                k.kelimeTipi = KelimeTipi.fiil
                for i in paragraf._fiiller:
                    if i.kelimeIcerik == k.kelimeIcerik:
                        ekle = 0
                        break
                if ekle == 1:
                    paragraf._fiiller.append(k)

    def frekans_degeri_ver(self, kelime_icerik):
        kelime_query = "SELECT * FROM kelimeler_freq WHERE kelime='{}'".format(kelime_icerik)
        self.cursor.execute(kelime_query)
        row = self.cursor.fetchone()
        if row is not None:
            return row[1]
        else:
            return 0

if __name__ == '__main__':
    database = Veritabani()
    print(database.hostname)
