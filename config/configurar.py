

from os.path import exists
from os import getcwd

from config.ayuda.txt import ArchivoTxt
from config.ayuda.txt import eliminar


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
            self.txt.modificar(ruta_datos)

        else:          

            self.txt.crear()
            self.txt.modificar(ruta_datos)

        

            
