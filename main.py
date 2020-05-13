from ui import *



class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):

	def __init__(self, *args, **kwargs):   
		QtWidgets.QMainWindow.__init__(self, *args, **kwargs)
		self.setupUi(self)
		self.ejecutar_proceso()

	def ejecutar_proceso(self):
		self.btn_enviar.clicked.connect(self.obtener_datos)

	

	def obtener_datos(self):
		"""Obtiene los datos del formulario"""

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


		return datos 

if __name__ == "__main__":
	app = QtWidgets.QApplication([])
	window = MainWindow()
	window.show()
	app.exec_()