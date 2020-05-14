from os import getcwd


from info_obtencion.ayuda.excel import ArchivoExcel
from info_obtencion.ayuda.txt import ArchivoTxt
from info_obtencion.ayuda.rutas import Rutas
from info_obtencion.ayuda.rutas import dividir_cadena
from info_obtencion.ayuda.rutas import unir_cadenas



class TarjetaInformativa(ArchivoExcel):  
    """Crea una tarjeta informativa pasandole un
        archivo de ejemplo"""
    
    ruta_excel = (getcwd()) + '\\'+'docs' + '\\'+'modelo_tarjeta_info.xlsx'
    

    def __init__(self, ):
        ArchivoExcel.__init__(self, ruta_excel)        
        
        self.folio = folio
        self.ruta_datos = ruta_datos

        self.datos = self.obtener_datos()

    def obtener_datos(self):
        """Obtiene los datos de la base datos
        """

        #ruta = self.ruta_datos + '\\' self.archivo + '.txt' 
     

        ArchivoTxt(ruta)
        informacion_txt = ArchivoTxt.leer()

        return informacion_txt[0]

   
"""     
	def celdas_combinadas(self, hoja_activa, rango, texto):

		self.wb.active =  hoja_activa

		hoja_activa.merge_cells(rango)
 """



    








    
class ArchivoObtenido:

    def __init__(self, folio, fecha, ruta_datos):
        
        self.folio = folio
        self.fecha = fecha
        self.ruta_datos = ruta_datos
        


    def obtener_archivos(self):
        registros = list()

        fecha_div = dividir_cadena('_', self.fecha)
        ruta_anno = self.ruta_datos +'\\' + fecha_div[-1]
        
        ruta = Rutas()
        archivos = ruta.recuperar_rutas(ruta_anno, True)

        for archivo in archivos:
            nombre = archivo[-1].split('_')[0]
            if nombre == self.folio:
                fecha = archivo[-1].split('_')[1]
                hora  = archivo[-1].split('_')[-1].split('.')[0]
                
                datos = [nombre, fecha, hora]
                registros.append(datos)
        
            else:
                pass

        return registros

       
        archivo = ArchivoTxt()
       
