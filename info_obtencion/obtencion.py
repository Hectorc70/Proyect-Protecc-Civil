from os import getcwd


from info_obtencion.ayuda.excel import ArchivoExcel
from info_obtencion.ayuda.txt import ArchivoTxt
from info_obtencion.ayuda.rutas import Rutas
from info_obtencion.ayuda.rutas import dividir_cadena
from info_obtencion.ayuda.rutas import unir_cadenas



class TarjetaInformativa(ArchivoExcel):  
    """Crea una tarjeta informativa pasandole un
        archivo de ejemplo"""   
    

    def __init__(self, archivo, ruta_datos, ruta_g_excel):
        self.ruta_excel = (getcwd()) + '\\'+'docs' + '\\'+'modelo_tarjeta_info.xlsx'
        ArchivoExcel.__init__(self, self.ruta_excel)        
        
        self.archivo = archivo
        self.ruta_guardado = ruta_datos
        self.excel_g = ruta_g_excel

    def obtener_datos(self):
        datos_txt = dict()
        ruta_archivo = self.ruta_guardado + '\\' + self.archivo
        

        archivo = ArchivoTxt(ruta_archivo)
        contenido = archivo.leer()

        contenido_div = dividir_cadena('|', contenido[0])

        for dato in contenido_div:
            clave = dato.split(':')[0]
            info  = dato.split(':')[-1]
             
            datos_txt[clave] = info

        return datos_txt





    def formatear_datos(self):
        """Junta todos los datos como
        nombre del archivo, celdas a escribir, 
        datos del txt por registro"""


        datos_registro = dict()
        datos_txt = self.obtener_datos()
        datos_completos = {'reporto':[9,9, datos_txt['report_o']], 
                  'id':[16,10, datos_txt['folio']],'turno':[21,9, datos_txt['turno']],
                  'reporte':[7,17, datos_txt['reporte']], 
                  'h-f_reporte':[11,17, datos_txt['h_report']], 
                  'municipio':[15,17, datos_txt['region']],
                  'col_juntaux':[19,17, datos_txt['colonia']], 
                  'dir_paraje':[23,17, datos_txt['coord']], 
                  'afectacion':[8,24, datos_txt['afectacion']],
                  'acc_pc':[7,35, datos_txt['acciones']],
                  'dependencias':[17,35, datos_txt['dependencias']],
                  'desarrollo':[7,45, datos_txt['desarrollo']]}

        datos_registro[self.archivo]= datos_completos

        self.escribir_celdas(datos_registro, 0)



    def escribir_celdas(self, datos, hoja):

        self.wb.active =  hoja       

        for registro, datos in datos.items():
            
                     

            for  campo in datos.values():              
                   
                columna = campo[0]
                fila    = campo[1]
                dato    = campo[-1]
                celda = self.wb.active.cell(row=fila, column=columna)
                celda.value = (dato) 

                
               
               

        self.guardar(self.excel_g)

#tarjeta = TarjetaInformativa('2321_14-05-2020_12-01.txt', 'C:\\pruebas\\2020', 'prueba.xlsx')
#tarjeta.formatear_datos()



    








    
class ArchivoObtenido:

    def __init__(self, datos_de_busqueda, ruta_datos):
        
        self.datos = datos_de_busqueda        
        self.ruta_datos = ruta_datos
        

    def comprobar_tipo_busqueda(self):
        """comprueba que tipo de busqueda debe hacer
            por numero de folio, por fecha de creacion 
            por los dos  tambien si es de forma masiva o individual"""


        registros = None
        for clave, dato in self.datos.items():
            if clave == 'folio':
                registros = self.busqueda_por_folio(dato)
                             

            elif clave == 'fecha':
                registros = self.busqueda_por_fecha(dato) 
        
        return registros
    def busqueda_por_folio(self, folio):
        """devuelve todos los registros con el
        folio que se solicito sin importar el año"""

        registros = dict()


        ruta = Rutas()
        archivos = ruta.recuperar_rutas(self.ruta_datos, True)

        for archivo in archivos:
            folio_archivo = archivo[-1].split('_')[0]
            if folio_archivo == folio:

                fecha = archivo[-1].split('_')[1]
                hora  = archivo[-1].split('_')[-1].split('.')[0]
                
                
                registros[archivo[-1]] = [folio_archivo, fecha, hora]

        return registros
    
    
    def busqueda_por_fecha(self, fecha):
        """Busca registros por fecha de creacion"""

        registros = dict()
        anno = fecha.split('-')[-1]
        ruta_con_fecha = self.ruta_datos + '\\' + anno

        ruta = Rutas()
        archivos = ruta.recuperar_rutas(ruta_con_fecha, True)


        for archivo in archivos:
            fecha_archivo = archivo[-1].split('_')[1]

            if fecha_archivo == fecha:
                
                folio = archivo[-1].split('_')[0]               
                hora  = archivo[-1].split('_')[-1].split('.')[0]
                
                
                registros[archivo[-1]] = [folio, fecha_archivo, hora]

        return registros



        
    def obtener_archivos_individual(self):
        registros = dict()

        fecha_div = dividir_cadena('_', self.fecha)
        ruta_anno = self.ruta_datos +'\\' + fecha_div[-1]
        
        ruta = Rutas()
        archivos = ruta.recuperar_rutas(ruta_anno, True)

        for archivo in archivos:
            nombre = archivo[-1].split('_')[0]
            if nombre == self.folio:
                fecha = archivo[-1].split('_')[1]
                hora  = archivo[-1].split('_')[-1].split('.')[0]
                
                
                registros[archivo[-1]] = [nombre, fecha, hora, ruta_anno]
        
            else:
                pass

        return registros

       
        
