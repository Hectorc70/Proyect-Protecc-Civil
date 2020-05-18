

from os.path import exists
from os import getcwd

from config.ayuda.txt import ArchivoTxt
from config.ayuda.txt import eliminar
from config.ayuda.fechas import RangoFechas


class ArchivoConfig:
	def __init__(self):
		self.ruta_Actual = (getcwd())
		self.ruta = self.ruta_Actual + '\\config.txt'
		self.txt = ArchivoTxt(self.ruta)

	def obtener_configuraciones(self):
		configuraciones = self.txt.leer()


		if len(configuraciones) == 0:
			return ''
		else:
			return configuraciones[0]    

	  
	 
	
	def guardar_configuraciones(self, ruta_datos): 

		if exists(self.ruta):            
			eliminar(self.ruta)
			self.txt.crear()
			self.txt.modificar(ruta_datos, False)
		else:          

			self.txt.crear()
			self.txt.modificar(ruta_datos, False)

		

			
class ArchivoFolios:

	def __init__(self, ruta):		
		
		self.anno_actual = self.retornar_anno_actual()
		self.ruta  = ruta
		self.ruta_archivo = self.ruta_archivo_str()
		self.txt   = ArchivoTxt(self.ruta_archivo) 


	def retornar_anno_actual(self):
		fechas = RangoFechas()
		fecha_actual = fechas.fecha_actual()
		anno = fecha_actual.split('-')[-1]	

		return anno	
	def ruta_archivo_str(self):
		ruta_archivo = self.ruta + '\\' + self.anno_actual + '_' 'folios.txt'


		return ruta_archivo

	def guardar_folio(self, folio):	
		
				
		folio_a_guardar = self.anno_actual + ':' + folio

		self.txt.comprobar_si_existe(folio_a_guardar)

	def cargar_folio(self):	
		
		
		contenido = self.txt.leer()
		
		if contenido:
			folio_sin_salto = contenido[-1].replace('\n', '')  #Quita los saltos de linea del texto			
			folio = folio_sin_salto.split(':')[-1]
			
			folio_a_establecer = int(folio)+1
			
			return str(folio_a_establecer)
		else:
			pass