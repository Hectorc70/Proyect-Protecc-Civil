from os import getcwd

from os.path import splitext


from info_obtencion.ayuda.excel import ArchivoExcel
from info_obtencion.ayuda.txt import ArchivoTxt
from info_obtencion.ayuda.rutas import Rutas
from info_obtencion.ayuda.rutas import dividir_cadena
from info_obtencion.ayuda.rutas import unir_cadenas
from info_obtencion.ayuda.fechas import RangoFechas






class TarjetaInformativa(ArchivoExcel):  
    """Crea una tarjeta informativa pasandole un
        archivo de ejemplo"""   
    


    def __init__(self, archivo, anno, ruta_datos, ruta_g_excel):
        self.ruta_excel = (getcwd()) + '\\'+'docs' + '\\'+'modelo_tarjeta_info.xlsx'
        ArchivoExcel.__init__(self, self.ruta_excel)        
        
        self.archivo = archivo
        self.anno    = anno
        self.ruta_guardado = ruta_datos
        self.excel_g = ruta_g_excel


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

    def obtener_datos(self):
        datos_txt = dict()
        ruta_archivo = self.ruta_guardado + '\\' + self.anno + '\\' + self.archivo
        

        archivo = ArchivoTxt(ruta_archivo)
        contenido = archivo.leer()

        contenido_div = dividir_cadena('|', contenido[0])
        
        if contenido_div:
            for dato in contenido_div:
                clave = dato.split(':')[0]
                info  = dato.split(':')[-1]
                
                datos_txt[clave] = info

            return datos_txt





    



    def escribir_celdas(self, datos, hoja):

        self.wb.active =  hoja       

        for registro, datos in datos.items():
            
                     

            for  campo in datos.values():              
                   
                columna = campo[0]
                fila    = campo[1]
                dato    = campo[-1]
                celda = self.wb.active.cell(row=fila, column=columna)
                celda.value = (dato) 

                
               
               
        nombre = splitext(self.archivo)
        nombre_completo = self.excel_g + '\\' + nombre[0] + '.xlsx'
        
        self.guardar(nombre_completo)

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

        registros =  dict()
        fechas = RangoFechas()   
        

        fecha_ini   = datos['fecha_ini']
        fecha_final = datos['fecha_fin']
            
        dia_ini    = fecha_ini[0]
        mes_ini    = fecha_ini[1]  
        anno_ini   = int(fecha_ini[-1])
        fecha_completa_ini = [dia_ini + '-' + mes_ini + '-' + str(anno_ini)]        
        
        dia_final   = fecha_final[0]
        mes_final    = fecha_final[1]
        anno_final = int(fecha_final[-1])
        fecha_completa_final = [dia_final + '-' + mes_final + '-' + str(anno_final)]        
        ruta = Rutas()
        # se ejecuta si los años son iguales
        if anno_ini == anno_final:
            ruta_con_fecha = self.ruta_datos + '\\' + str(anno_ini)         
            archivos = ruta.recuperar_rutas(ruta_con_fecha, True)
            
            #se ejecuta si el el año y mes es el mismo
            if mes_ini == mes_final:
                fechas_mes = list()
                dias_del_mes = fechas.armar_dias_restantes(dia_ini, mes_ini, dia_final=dia_final)
                dias_completos = [dia_ini + '-' + mes_ini] + dias_del_mes
                
                for dia in dias_completos:
                    fecha = dia + '-' + str(anno_ini)
                    fechas_mes.append(fecha) 

                registros = self.retornar_registros(archivos, fechas_mes)
                
                
                return registros

            #se ejecuta si el año es el mismo pero varios meses
            else:

                fechas_anno = list()
                meses_restantes = list()
               
                
                primer_mes       = fechas.armar_dias_restantes(dia_ini, mes_ini)
                primer_mes_completo = [dia_ini+'-'+mes_ini] + primer_mes

                ultimo_mes       = fechas.armar_dias_restantes(dia_final, mes_final, reverse=True)
                ultimo_mes_completo = ultimo_mes  + [dia_final + '-' + mes_final]

                for mes in range(int(mes_ini)+1, int(mes_final)):                
                    mes_format = str(mes).zfill(2)             

                    meses_restantes.append(mes_format)

                #los meses intermedios con sus 31 dias
                todos_los_meses = ''
                if meses_restantes:                
                    meses_restantes_dias = fechas.armar_meses_completos(meses_restantes[0], meses_restantes[-1])
                
                #la suma de todos los dias de todos los meses del año                
                    todos_los_meses = primer_mes_completo + meses_restantes_dias + ultimo_mes_completo
                     #Crear la fecha_completa
                    for mes in todos_los_meses:
                        anno_mes = mes + '-' + str(anno_ini)

                        fechas_anno.append(anno_mes)
                
                else:
                    todos_los_meses = primer_mes_completo + ultimo_mes_completo

                    for mes in todos_los_meses:
                        anno_mes = mes + '-' + str(anno_ini)

                        fechas_anno.append(anno_mes)          

                
                registros = self.retornar_registros(archivos, fechas_anno)
                
                return registros



               

            

        # se ejecuta si los años son diferentes   
        if anno_ini != anno_final:    
            archivos_annos= list()       
            
        
            anno_ini_con_meses= fechas.armar_annos_incompletos(fecha_ini)
            anno_ini_con_meses_completo = fecha_completa_ini + anno_ini_con_meses
            
            anno_fin_con_meses= fechas.armar_annos_incompletos(fecha_final, reverse=True)
            anno_fin_con_meses_completo =  anno_fin_con_meses + fecha_completa_final

            annos_intermedios =  fechas.armar_annos_completos(int(anno_ini)+1, int(anno_final)-1)
            
            
            todos_annos = anno_ini_con_meses_completo + annos_intermedios + anno_fin_con_meses_completo

            #recupera las rutas de todos los años solicitados
            for anno in range(anno_ini, anno_final+1):
                ruta_con_fecha = self.ruta_datos + '\\' + str(anno)         
                archivos = ruta.recuperar_rutas(ruta_con_fecha, True)               

                archivos_annos.append(archivos)

            
            registros = self.retornar_registros_por_fecha(archivos_annos, todos_annos)

            return registros


        else:
            return ' '
        return registros

            


            
            
    def retornar_registros_por_fecha(self, carpetas, lista_de_comparacion):
        """Parametros: archivos(como lista debe contener
            todas las ruta de los archivos separadas por carpeta)
            lista_de_comparacion(como lista debe contener los datos que se
            van a comparar con los archivos obtenidos)
            """

        registros = dict()
        if type(carpetas) is list and len(carpetas) >1:
            for carpeta in carpetas: 
                for archivo in carpeta:
                    fecha_archivo = archivo[-1].split('_')[1]               

                    if fecha_archivo in lista_de_comparacion:
                        folio = archivo[-1].split('_')[0].split('.')[0]      
                        hora  = archivo[-1].split('_')[-1].split('.')[0] 
                                
                    
                        registros[archivo[-1]] = [folio, fecha_archivo, hora]
        
        
        return registros

    def retornar_registros(self, archivos, lista_de_comparacion):

        registros = dict()

        for archivo in archivos:
            fecha_archivo = archivo[-1].split('_')[1]              

            if fecha_archivo in lista_de_comparacion:
                folio = archivo[-1].split('_')[0].split('.')[0]      
                hora  = archivo[-1].split('_')[-1].split('.')[0] 
                                
                    
                registros[archivo[-1]] = [folio, fecha_archivo, hora]

        return registros

            

            

        
        




