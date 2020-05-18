import os.path as path 
from os import remove


class ArchivoTxt:
	"""Trabaja con archivos txt"""

	def __init__(self, archivo):
		
		self.ruta_archivo = archivo	

	def comprobar_si_existe(self, texto):	
		
		if path.exists(self.ruta_archivo):
			self.modificar(texto)
		else:
			self.crear()
			self.modificar(texto)
		

	def modificar(self, datos, salto_linea=True):
		
		archivo_r = open(self.ruta_archivo, "a")

		if salto_linea:
			archivo_r.write(datos + '\n')
		else:
			archivo_r.write(datos)
		
		archivo_r.close() 
		
		print("leido y escrita la INFO")

	def leer(self, lineas = True):
		try:
			if lineas:
				archivo_r = open(self.ruta_archivo, "r")
				contenido_txt = archivo_r.readlines()
				archivo_r.close() 
			else:
				archivo_r = open(self.ruta_archivo, "r")
				contenido_txt = archivo_r.read()
				archivo_r.close() 

			return contenido_txt
		except FileNotFoundError:
			pass
	
	def crear(self):

		archivo_r = open(self.ruta_archivo, "w")
		archivo_r.close()



def eliminar(ruta):
	remove(ruta)