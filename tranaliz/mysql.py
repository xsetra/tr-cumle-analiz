# -*- coding: utf-8 -*-


import pymysql

class Veritabani:
	def __init__(self):
		self.hostname = "localhost"
		self.username = "root"
		self.password = "----------------SECURITY-------------"
		self.database_name = "fatmabozyigit"
		self.obj_db = None
		self.cursor = None

	def baglan(self):
		self.obj_db = pymysql.connect(self.hostname,
				     self.username,
				     self.password,
				     self.database_name)
		self.cursor = obj_db.cursor()

	def kelime_tipi_sorgula(self):
		if self.obj_db is None:
			return "Veritabanı bağlantısı kurmadan sorgulama yapamazsınız"
		else:
			# SQL sorgu cümlecikleri eklenip deger donecek
			pass
		
		
database = Veritabani()
print(database.hostname)


