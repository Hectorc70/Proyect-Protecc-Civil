from os import getcwd
import calendar


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

            elif clave == 'folio-fecha':
                registros = self.busqueda_por_folio_fecha(dato) 
            
            elif clave == 'rango-fechas':
                registros = self.busqueda_rango_de_fechas(dato)
        
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


    def busqueda_por_folio_fecha(self, datos):
        """Busca en la carpeta del año y luego retorna solo
        el registro que coincida con el año y el numero de folio"""
        registros = dict()

        folio = datos[0]
        fecha = datos[1]

        anno = fecha.split('-')[-1]
        ruta_con_fecha = self.ruta_datos + '\\' + anno

        ruta = Rutas()
        archivos = ruta.recuperar_rutas(ruta_con_fecha, True)

       
        
        for archivo in archivos:
            fecha_archivo = archivo[-1].split('_')[1]
            folio_archivo = archivo[-1].split('_')[0]

            if fecha_archivo == fecha and folio_archivo == folio:

                hora  = archivo[-1].split('_')[-1].split('.')[0]                
                
                registros[archivo[-1]] = [folio_archivo, fecha_archivo, hora]

        return registros

        
    def busqueda_rango_de_fechas(self, datos):    
        fechas = RangoFechas()

        archivos_annos= list()
        annos_intermedios = list()

        fecha_ini   = datos['fecha_ini']
        fecha_final = datos['fecha_fin']
            
        dia_ini    = fecha_ini[0]
        mes_ini    = fecha_ini[1]
        anno_ini   = int(fecha_ini[-1])
        
        anno_final = int(fecha_final[-1])
        ruta = Rutas()

        if anno_ini == anno_final:
            pass
       
        else:
        
           anno_ini_con_meses= fechas.armar_annos_incompletos(fecha_ini)
           anno_fin_con_meses= fechas.armar_annos_incompletos(fecha_ini)


                
            
                



            
            
            
            

        #recupera las rutas de todos los años solicitados

        """    for anno in range(anno_ini, anno_final+1):
                ruta_con_fecha = self.ruta_datos + '\\' + str(anno)         
                archivos = ruta.recuperar_rutas(ruta_con_fecha, True)

                archivos_annos.append(archivos)"""
        
        #filtra solo los meses y dias solicitados
        """for archivo in archivos_annos:
            fecha_archivo = archivo[-1].split('_')[1]
            dia = fecha_archivo.split('-')[0]
            mes = fecha_archivo.split('-')[1]"""



        return 'hola'
       
        
    def buscar_en_mismo_año(self, datos):
        pass




class RangoFechas():
    def __init__(self):

        self.dias = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10',
                        '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', 
                        '21', '22', '23', '24', '25', '26', '27','28', '29', '30', '31'
                    ]

        self.meses = ['01', '02', '03', '04', '05', '06', '07', '08', 
                        '09', '10', '11', '12'
                        ]


    def armar_annos_incompletos(self, fecha):
        """Parametros fecha= [20,05,2020]
            Arma un año incompleto, devuelve los dias y meses
            que le faltan para el 31-12-2020 en este caso.(todos los mes son de 31 dias)
            ejemplo: 21-05-2020, 22-05-2020... 31-12-2020"""

        anno_con_meses_dias = list()
        
        dia = fecha[0]
        mes = fecha[1]
        anno = fecha[2]

        #primer mes dias que le faltan

        mes_uno_dias = self.armar_dias_restantes(dia, mes) #arma el primer mes 
        meses_restantes_completos = self.armar_meses_completos(int(mes)+1)

        todos_los_meses = mes_uno_dias + meses_restantes_completos

        for mes in todos_los_meses:

            fecha_con_meses = mes + '-' + anno

            anno_con_meses_dias.append(fecha_con_meses)

        return anno_con_meses_dias






    def armar_annos_completos(self, anno_ini, anno_final):
        """Parametros año inicial = '2019' y año final= '2020'
        Arma años con formato de dd-mm-aaa
        ejemplo: 01.01.2019, 02.01.2019...30.12.2020, 31.12.2020"""

        annos_intermedios = list()

        for anno in range(anno_ini, anno_final+1):
                for mes in self.meses:
                    for dia in self.dias:
                        annos_intermedios.append(dia + '-'+ mes + '-' + str(anno))
        

        return annos_intermedios

    def armar_dias_restantes(self, dia_ini, mes):
        """Argumentos: dia_ini = '05', mes = '05'.(como cadenas)
            Retorna dias restantes de un mes en formato string:
            ejemplo, 05.05 devolveria desde '06-05' al '31-05',
            todos los meses los toma como de 31 dias"""
        
        dias_restantes = list()
        
        for dia in range(int(dia_ini)+1, 32):
            
            dia_str = str(dia)

            dia_format = dia_str.zfill(2)

            mes_dias = dia_format + '-' + mes

            dias_restantes.append(mes_dias)

        return dias_restantes

    def armar_meses_completos(self, mes_ini):
        
        """Arma los meses con 31 dias 
            Parametros mes_ini= '05'
            devolveria '01-05', '02.05'....'30.12', '31.12',
            todos los meses son de 31 dias"""

        
        meses_dias = list()


        for mes in range(int(mes_ini), 13):
            for dia in self.dias:

                
                mes_str = str(mes)
                mes_format = mes_str.zfill(2)
                mes_con_dias = dia + '-' + mes_format
                meses_dias.append(mes_con_dias)
        
        return meses_dias

            

        

fechas = RangoFechas()
fechas.armar_dias_restantes('05', '05')
