from formulario.ayuda.txt import ArchivoTxt
from formulario.ayuda.rutas import unir_cadenas



class Registro():
    def __init__(self,ruta_datos, datos):
        self.ruta_datos = ruta_datos
        self.datos      = datos


    def formar_datos(self):

        claves_y_datos = list()
        

        for clave, dato in self.datos.items():
            clave_dato = [clave,dato]
            formato_dato = unir_cadenas('-', clave_dato)

            claves_y_datos.append(formato_dato)

        datos_completos = unir_cadenas('|',claves_y_datos)

        return datos_completos
        
        


    def crear_archivo(self): 

        linea = self.formar_datos() 

        txt = ArchivoTxt(linea)        
        
        txt.crear()
        

        
