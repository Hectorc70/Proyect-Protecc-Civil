from PyQt5.QtWidgets import QMessageBox, QFileDialog

from ui import *

from formulario.formulario import Registro
from config.configurar import ArchivoConfig
from info_obtencion.obtencion import ArchivoObtenido
from info_obtencion.obtencion import TarjetaInformativa




		

class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):

	def __init__(self, *args, **kwargs):   
		QtWidgets.QMainWindow.__init__(self, *args, **kwargs)
		#self.ruta_datos = self.ruta_guardado_input.text()
	
		self.setupUi(self)
		self.ejecutar_proceso()
		self.cargar_configuracion()
		
		

	def ejecutar_proceso(self):
		
		#self.btn_guardar.clicked.connect(self.configuracion)
	
		#self.btn_expl_carp.clicked.connect(self.explorador_archivos)

		pass

	def obtener_datos(self):
		"""Obtiene los datos del formulario"""

		ruta = self.ruta_guardado_input.text()

		folio = self.folio_input.text()
		turno = self.turno_input.text()
		agente = self.agente_input.text()
		report_o = self.report_o_input.text()
		h_report = self.h_report_input.text()
		terminal = self.terminal_input.text()
		reporte = self.reporte_input.text()
		region = self.mun_region_input.text()
		colonia = self.colonia_input.text()
		coord = self.coord_input.text() 

		dependencias = self.dependencias_input.toPlainText()
		acciones     = self.acciones_input.toPlainText()
		afectacion   = self.afectacion_input.toPlainText()
		desarrollo   = self.desarrollo_input.toPlainText()

		datos = {'folio': folio, 'turno':turno, 'agente':agente,
				'report_o': report_o, 'h_report':h_report,
				'terminal':terminal, 'reporte':reporte,
				'region':region, 'colonia':colonia, 'coord':coord,
				'dependencias':dependencias, 'acciones':acciones,
				'afectacion':afectacion, 'desarrollo':desarrollo}

		
		registro = Registro(ruta, datos)
		registro.crear_archivo()


	def configuracion(self):
		"""Guarda la configuracion cuando se escibe la ruta en el
			campo y se presiona el boton de guardar"""

			
		ruta = self.ruta_guardado_input.text()

		if ruta == '':
			self.mostrar_advertencia()

		else:
			config = ArchivoConfig()	
			config.guardar_configuraciones(ruta)
			QMessageBox.information(self, "Aviso", "Se guardo la Configuracion")


	def cargar_configuracion(self):
		"""Carga la configuracion que esta guardada en el
		archivo config.txt ubicado en la raiz"""

		ruta = self.ruta_guardado_input.text()

		

		
		config = ArchivoConfig()
		configuraciones = config.obtener_configuraciones()	

		if  configuraciones != '':
			self.ruta_guardado_input.setText(configuraciones)
			print(self.ruta_guardado_input.text())
		else:
			self.tabWidget.setCurrentIndex(2)			


	def exportar_datos(self):		
		
		registros = self.mostrando_datos()
		carpeta_guardado_excel = self.directorio_g_input.text()	

		for registro, dato in registros.items():

			nombre = dato[0]	
			ruta_datos = dato[-1]			
			ruta_excel = carpeta_guardado_excel + '/' + nombre + '.xlsx'

			tarjeta = TarjetaInformativa(registro, ruta_datos, ruta_excel)	
		
			tarjeta.formatear_datos()

	
			
			
	
			


	def  mostrar_advertencia (self, titulo = 'Advertencia',
							  texto = 'Debe indicar una ruta para el guardado de los datos'):
		"""Muestra advertencias"""
		QMessageBox.warning(self, titulo, texto)
		
		 
class WidgetsAyuda(MainWindow):

	def __init__(self):
		MainWindow.__init__(self)


	

	
	def ventana_advertencia(self, titulo, texto ):
		pass		
		


	
class ExportarDatos(MainWindow):

	def __init__(self):
		MainWindow.__init__(self)		
		
		self.btn_buscar_datos.clicked.connect(self.comprobar)
		self.btn_directorio_excel.clicked.connect(self.explorador_de_archivos)
		#self.widget = WidgetsAyuda()

	
	def exportar_datos(self):
		"""invoca la clase para exportar los datos en una
		   archivo excel """


		#registros_obtenidos = self.comprobar()
		pass




		

	def comprobar(self):

		if self.rbtn_individual.isChecked() or self.rbtn_rangos.isChecked():

			if self.rbtn_individual.isChecked():			
				registros_obtenidos = self.buscar_registro_individual()
		
			if self.rbtn_rangos.isChecked():
				registros_obtenidos = self.buscar_registro_por_rangos()
		else:
			QMessageBox.warning(self, 'Advertencia', 'Seleccione una opcion: Individual o Rangos')
		
		#return registros_obtenidos

		

	def buscar_registro_individual(self):

		
		datos_para_busqueda = dict()
		
		folio = self.b_folio_input.text()
		dia = self.b_fecha_dia_input.text()		
		mes = self.b_fecha_mes_input.text()
		anno = self.b_fecha_anno_input.text()	
		ruta_datos = self.ruta_guardado_input.text()

		ruta_guardar_en = self.directorio_g_input.text()

		fecha = dia + '-' + mes + '-' + anno

		if ruta_guardar_en != '':
			if folio != '' and fecha != '--':
				datos_para_busqueda['folio-fecha'] = [folio, fecha]		
				
			elif folio != '':
				datos_para_busqueda['folio'] = folio		
				
			
			if dia != '' and mes != '' and anno !='':
				datos_para_busqueda['fecha'] = fecha
				
				
			
			else:
				QMessageBox.warning(self, 'Advertencia', 'Llene los campos Correspondientes')

				
			
			
			if datos_para_busqueda:
				archivo = ArchivoObtenido(datos_para_busqueda, ruta_datos)
				registros = archivo.comprobar_tipo_busqueda()
				self.mostrar_datos(registros)
		
				return registros 
			
				
				

		else:
			QMessageBox.warning(self, 'Advertencia', 'Seleccione una ruta de Guardado para la informacion')
		
	

		
	



		
	def buscar_registro_por_rangos(self):
		"""Obtiene datos para buscar registros por rango
			de fechas"""

		datos_para_busqueda = dict()
		
	
		dia_ini = self.rang_fecha1_dia_input.text()
		mes_ini = self.rang_fecha1_mes_input.text()
		anno_ini = self.rang_fecha1_anno_input.text()

		

		dia_fin = self.rang_fecha2_dia_input.text()
		mes_fin = self.rang_fecha2_mes_input.text()
		anno_fin = self.rang_fecha2_anno_input.text()

		ruta_guardar_en = self.directorio_g_input.text()
		ruta_datos  = self.ruta_guardado_input.text()

		if ruta_guardar_en != '':

			if (dia_ini != '' and mes_ini != '' and anno_ini != '' and
				dia_fin != '' and mes_fin != '' and anno_fin != '' 
			):
				datos_para_busqueda['rango-fechas']= {'fecha_ini':[dia_ini, mes_ini, anno_ini], 
										'fecha_fin':[dia_fin, mes_fin, anno_fin]
									}

			else:
				QMessageBox.warning(self, 'Advertencia', 'Llene los campos Correspondientes: DD/MM/AAAA')

			#solo se ejecuta si el diccionario tiene datos
			if datos_para_busqueda:
				archivos  = ArchivoObtenido(datos_para_busqueda, ruta_datos)
				registros = archivos.comprobar_tipo_busqueda()
				
				
				return registros

		else:
			QMessageBox.warning(self, 'Advertencia', 'Seleccione una ruta de Guardado para la informacion')


	def mostrar_datos(self, datos):		
				
		if datos:
			self.plainTextEdit.setPlainText('FOLIO' +'	' + 'FECHA' +'	' + 'HORA')

			for dato in datos.values():

				folio 		   = dato[0]
				fecha_creacion = dato[1]
				hora 		   = dato[2]

				dato = folio + '	' + fecha_creacion + '	' + hora 

						
				self.plainTextEdit.appendPlainText(str(dato))

		else:
			QMessageBox.information(self, 'Aviso', 'No se encontraron registros, prueba con otro folio o fecha:DD/MM/AAAA')	




	
	
	def explorador_de_archivos(self):
		ruta_carpeta = QFileDialog.getExistingDirectory(self, 'Guardado de Tarjetas')
		self.directorio_g_input.setText(ruta_carpeta)

		return ruta_carpeta
if __name__ == "__main__":
	app = QtWidgets.QApplication([])
	window = ExportarDatos()
	window.show()
	app.exec_()