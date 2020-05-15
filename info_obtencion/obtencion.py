from os import getcwd


from info_obtencion.ayuda.excel import ArchivoExcel
from info_obtencion.ayuda.txt import ArchivoTxt
from info_obtencion.ayuda.rutas import Rutas
from info_obtencion.ayuda.rutas import dividir_cadena
from info_obtencion.ayuda.rutas import unir_cadenas



class TarjetaInformativa(ArchivoExcel):  
    """Crea una tarjeta informativa pasandole un
        archivo de ejemplo"""   
    

    def __init__(self, archivo, ruta_guardado, ruta_g_excel):
        self.ruta_excel = (getcwd()) + '\\'+'docs' + '\\'+'modelo_tarjeta_info.xlsx'
        ArchivoExcel.__init__(self, self.ruta_excel)        
        
        self.archivo = archivo
        self.ruta_guardado = ruta_guardado
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

    def __init__(self, folio, fecha, ruta_datos):
        
        self.folio = folio
        self.fecha = fecha
        self.ruta_datos = ruta_datos
        


    def obtener_archivos(self):
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
                
                
                registros[archivo[-1]] = [nombre, fecha, hora]
        
            else:
                pass

        return registros

       
        archivo = ArchivoTxt()
       
