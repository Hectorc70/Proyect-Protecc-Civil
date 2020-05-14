import datetime
from os.path import exists
from os import makedirs

from formulario.ayuda.txt import ArchivoTxt
from formulario.ayuda.rutas import unir_cadenas






class Registro():
    def __init__(self, ruta_datos, datos):
        self.ruta_datos = ruta_datos
        self.datos      = datos


    def formar_fecha(self):
        fecha_s_formato =  datetime.datetime.now()
        dia = fecha_s_formato.strftime("%d")
        mes = fecha_s_formato.strftime("%m")
        anno = fecha_s_formato.strftime("%Y")
        hora = fecha_s_formato.strftime("%H")
        minuto = fecha_s_formato.strftime("%M")

        datos_fecha = [dia, mes, anno]
        fecha = unir_cadenas('-', datos_fecha)
        fecha_completa = fecha + '_' + hora + '-' + minuto

        return fecha_completa, anno
    
    def formar_datos(self):        
        claves_y_datos = list()
        datos_creacion = dict()

        for clave, dato in self.datos.items():
            clave_dato = [clave,dato]
            formato_dato = unir_cadenas(':', clave_dato)

            claves_y_datos.append(formato_dato)

        datos_completos = unir_cadenas('|',claves_y_datos)

       
        

        return datos_completos
        
        


    def crear_archivo(self):
        fecha = self.formar_fecha()
        ruta_completa = self.crear_carpeta_anno(self.ruta_datos, fecha[1]) #Crea carpeta del año

        datos  = self.formar_datos()      

        
        nombre = self.datos['folio'] + '_'  + fecha[0]
        ruta_archivo = ruta_completa + '\\' + nombre + '.txt'
        txt = ArchivoTxt(ruta_archivo)        
        txt.crear()
        txt.modificar(datos)

        

    def crear_carpeta_anno(self, ruta, annno):
        """Comprueba que exita la carpeta del año actual
        si no es asi la crea"""
        ruta_completa = ruta + '\\' + annno
        if exists(ruta_completa):
            pass
        else:
            makedirs(ruta_completa)

        return ruta_completa
        
