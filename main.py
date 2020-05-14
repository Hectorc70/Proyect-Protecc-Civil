from PyQt5.QtWidgets import QMessageBox

from ui import *

from formulario.formulario import Registro
from config.configurar import ArchivoConfig
from info_obtencion.obtencion import TarjetaInformativa



class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):

	def __init__(self, *args, **kwargs):   
		QtWidgets.QMainWindow.__init__(self, *args, **kwargs)
		self.setupUi(self)
		self.ejecutar_proceso()
		self.cargar_configuracion()

	def ejecutar_proceso(self):
		self.btn_enviar.clicked.connect(self.obtener_datos)

		self.btn_guardar.clicked.connect(self.configuracion)

	def tarjeta_informativa(self):
		datos_ruta = self.ruta_guardado_input.text()
		tar_info = TarjetaInformativa(nombre_registro,datos_ruta)

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

			
		  
			
			


	def  mostrar_advertencia (self):
		"""Muestra advertencias"""
		QMessageBox.critical(self, "Advertencia", "Debe indicar una ruta para el guardado de los datos" )
		 



	
if __name__ == "__main__":
	app = QtWidgets.QApplication([])
	window = MainWindow()
	window.show()
	app.exec_()