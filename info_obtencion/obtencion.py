
from ayuda.excel import ArchivoExcel
from ayuda.txt import ArchivoTxt
from os import getcwd

class TarjetaInformativa(ArchivoExcel):  
    """Crea una tarjeta informativa pasandole un
        archivo de ejemplo"""
    
    ruta_excel = (getcwd()) + '\\'+'docs' + '\\'+'modelo_tarjeta_info.xlsx'
    

    def __init__(self, registro, ruta_datos):
        ArchivoExcel.__init__(self, ruta_excel)        
        
        self.registro = registro
        self.ruta_datos = ruta_datos

        self.datos = self.obtener_datos()

    def obtener_datos(self):
        """Obtiene los datos de la base datos
        """
        ruta = self.ruta_datos + '\\' self.archivo + '.txt' 
     

        ArchivoTxt(ruta)
        informacion_txt = ArchivoTxt.leer()

        return informacion_txt[0]

    def 
"""     
	def celdas_combinadas(self, hoja_activa, rango, texto):

		self.wb.active =  hoja_activa

		hoja_activa.merge_cells(rango)
 """



    








    
    