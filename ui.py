# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'in-PROTECC-CIVIL.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(998, 679)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(998, 679))
        MainWindow.setMaximumSize(QtCore.QSize(998, 679))
        MainWindow.setSizeIncrement(QtCore.QSize(0, 0))
        MainWindow.setAutoFillBackground(False)
        MainWindow.setStyleSheet("background-color: rgb(255, 255, 255);")
        MainWindow.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setEnabled(True)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setEnabled(True)
        self.tabWidget.setGeometry(QtCore.QRect(0, 70, 1001, 611))
        self.tabWidget.setFocusPolicy(QtCore.Qt.TabFocus)
        self.tabWidget.setObjectName("tabWidget")
        self.tab_form = QtWidgets.QWidget()
        self.tab_form.setAutoFillBackground(False)
        self.tab_form.setObjectName("tab_form")
        self.grupo1 = QtWidgets.QGroupBox(self.tab_form)
        self.grupo1.setGeometry(QtCore.QRect(10, 20, 561, 201))
        self.grupo1.setTitle("")
        self.grupo1.setObjectName("grupo1")
        self.folio_text = QtWidgets.QLabel(self.grupo1)
        self.folio_text.setGeometry(QtCore.QRect(10, 10, 41, 21))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.folio_text.setFont(font)
        self.folio_text.setAlignment(QtCore.Qt.AlignCenter)
        self.folio_text.setObjectName("folio_text")
        self.folio_input = QtWidgets.QLineEdit(self.grupo1)
        self.folio_input.setGeometry(QtCore.QRect(60, 10, 71, 21))
        self.folio_input.setObjectName("folio_input")
        self.turno_text = QtWidgets.QLabel(self.grupo1)
        self.turno_text.setGeometry(QtCore.QRect(150, 10, 51, 21))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.turno_text.setFont(font)
        self.turno_text.setAlignment(QtCore.Qt.AlignCenter)
        self.turno_text.setObjectName("turno_text")
        self.turno_input = QtWidgets.QLineEdit(self.grupo1)
        self.turno_input.setGeometry(QtCore.QRect(210, 10, 91, 21))
        self.turno_input.setObjectName("turno_input")
        self.agente_text = QtWidgets.QLabel(self.grupo1)
        self.agente_text.setGeometry(QtCore.QRect(320, 10, 51, 21))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.agente_text.setFont(font)
        self.agente_text.setAlignment(QtCore.Qt.AlignCenter)
        self.agente_text.setObjectName("agente_text")
        self.agente_input = QtWidgets.QLineEdit(self.grupo1)
        self.agente_input.setGeometry(QtCore.QRect(380, 10, 91, 21))
        self.agente_input.setObjectName("agente_input")
        self.report_o_text = QtWidgets.QLabel(self.grupo1)
        self.report_o_text.setGeometry(QtCore.QRect(10, 80, 71, 21))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        self.report_o_text.setFont(font)
        self.report_o_text.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.report_o_text.setObjectName("report_o_text")
        self.report_o_input = QtWidgets.QLineEdit(self.grupo1)
        self.report_o_input.setGeometry(QtCore.QRect(90, 80, 101, 21))
        self.report_o_input.setObjectName("report_o_input")
        self.h_report_text = QtWidgets.QLabel(self.grupo1)
        self.h_report_text.setGeometry(QtCore.QRect(10, 110, 71, 21))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        self.h_report_text.setFont(font)
        self.h_report_text.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.h_report_text.setObjectName("h_report_text")
        self.h_report_input = QtWidgets.QLineEdit(self.grupo1)
        self.h_report_input.setGeometry(QtCore.QRect(90, 110, 101, 21))
        self.h_report_input.setObjectName("h_report_input")
        self.terminal_text = QtWidgets.QLabel(self.grupo1)
        self.terminal_text.setGeometry(QtCore.QRect(10, 140, 71, 21))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        self.terminal_text.setFont(font)
        self.terminal_text.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.terminal_text.setObjectName("terminal_text")
        self.terminal_input = QtWidgets.QLineEdit(self.grupo1)
        self.terminal_input.setGeometry(QtCore.QRect(90, 140, 101, 21))
        self.terminal_input.setObjectName("terminal_input")
        self.reporte_text = QtWidgets.QLabel(self.grupo1)
        self.reporte_text.setGeometry(QtCore.QRect(10, 170, 71, 21))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        self.reporte_text.setFont(font)
        self.reporte_text.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.reporte_text.setObjectName("reporte_text")
        self.reporte_input = QtWidgets.QLineEdit(self.grupo1)
        self.reporte_input.setGeometry(QtCore.QRect(90, 170, 101, 21))
        self.reporte_input.setObjectName("reporte_input")
        self.mun_region_text = QtWidgets.QLabel(self.grupo1)
        self.mun_region_text.setGeometry(QtCore.QRect(230, 80, 111, 21))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        self.mun_region_text.setFont(font)
        self.mun_region_text.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.mun_region_text.setObjectName("mun_region_text")
        self.mun_region_input = QtWidgets.QLineEdit(self.grupo1)
        self.mun_region_input.setGeometry(QtCore.QRect(360, 80, 191, 21))
        self.mun_region_input.setObjectName("mun_region_input")
        self.colonia_text = QtWidgets.QLabel(self.grupo1)
        self.colonia_text.setGeometry(QtCore.QRect(230, 110, 111, 21))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        self.colonia_text.setFont(font)
        self.colonia_text.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.colonia_text.setObjectName("colonia_text")
        self.colonia_input = QtWidgets.QLineEdit(self.grupo1)
        self.colonia_input.setGeometry(QtCore.QRect(360, 110, 191, 21))
        self.colonia_input.setObjectName("colonia_input")
        self.coord_text = QtWidgets.QLabel(self.grupo1)
        self.coord_text.setGeometry(QtCore.QRect(230, 140, 121, 21))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        self.coord_text.setFont(font)
        self.coord_text.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.coord_text.setObjectName("coord_text")
        self.coord_input = QtWidgets.QLineEdit(self.grupo1)
        self.coord_input.setGeometry(QtCore.QRect(360, 140, 191, 21))
        self.coord_input.setObjectName("coord_input")
        self.grupo2 = QtWidgets.QGroupBox(self.tab_form)
        self.grupo2.setGeometry(QtCore.QRect(10, 230, 561, 211))
        self.grupo2.setTitle("")
        self.grupo2.setObjectName("grupo2")
        self.dependencias_text = QtWidgets.QLabel(self.grupo2)
        self.dependencias_text.setGeometry(QtCore.QRect(10, 10, 231, 31))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        self.dependencias_text.setFont(font)
        self.dependencias_text.setAlignment(QtCore.Qt.AlignCenter)
        self.dependencias_text.setObjectName("dependencias_text")
        self.acciones_text = QtWidgets.QLabel(self.grupo2)
        self.acciones_text.setGeometry(QtCore.QRect(320, 10, 231, 31))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        self.acciones_text.setFont(font)
        self.acciones_text.setAlignment(QtCore.Qt.AlignCenter)
        self.acciones_text.setObjectName("acciones_text")
        self.dependencias_input = QtWidgets.QPlainTextEdit(self.grupo2)
        self.dependencias_input.setGeometry(QtCore.QRect(10, 50, 231, 151))
        self.dependencias_input.setObjectName("dependencias_input")
        self.acciones_input = QtWidgets.QPlainTextEdit(self.grupo2)
        self.acciones_input.setGeometry(QtCore.QRect(320, 50, 231, 151))
        self.acciones_input.setObjectName("acciones_input")
        self.grupo3 = QtWidgets.QGroupBox(self.tab_form)
        self.grupo3.setGeometry(QtCore.QRect(580, 20, 401, 421))
        self.grupo3.setTitle("")
        self.grupo3.setObjectName("grupo3")
        self.afectacion_text = QtWidgets.QLabel(self.grupo3)
        self.afectacion_text.setGeometry(QtCore.QRect(10, 10, 381, 31))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        self.afectacion_text.setFont(font)
        self.afectacion_text.setAlignment(QtCore.Qt.AlignCenter)
        self.afectacion_text.setObjectName("afectacion_text")
        self.desarollo_text = QtWidgets.QLabel(self.grupo3)
        self.desarollo_text.setGeometry(QtCore.QRect(10, 210, 381, 31))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        self.desarollo_text.setFont(font)
        self.desarollo_text.setAlignment(QtCore.Qt.AlignCenter)
        self.desarollo_text.setObjectName("desarollo_text")
        self.afectacion_input = QtWidgets.QPlainTextEdit(self.grupo3)
        self.afectacion_input.setGeometry(QtCore.QRect(10, 40, 381, 161))
        self.afectacion_input.setObjectName("afectacion_input")
        self.desarrollo_input = QtWidgets.QPlainTextEdit(self.grupo3)
        self.desarrollo_input.setGeometry(QtCore.QRect(10, 240, 381, 171))
        self.desarrollo_input.setObjectName("desarrollo_input")
        self.btn_enviar = QtWidgets.QPushButton(self.tab_form)
        self.btn_enviar.setGeometry(QtCore.QRect(800, 450, 181, 41))
        self.btn_enviar.setStyleSheet("border-color: rgb(0, 0, 0);")
        self.btn_enviar.setObjectName("btn_enviar")
        self.btn_cancelar = QtWidgets.QPushButton(self.tab_form)
        self.btn_cancelar.setGeometry(QtCore.QRect(580, 450, 171, 41))
        self.btn_cancelar.setStyleSheet("border-color: rgb(0, 0, 0);")
        self.btn_cancelar.setObjectName("btn_cancelar")
        self.tabWidget.addTab(self.tab_form, "")
        self.tab_descarga_datos = QtWidgets.QWidget()
        self.tab_descarga_datos.setObjectName("tab_descarga_datos")
        self.desc_grupo1 = QtWidgets.QGroupBox(self.tab_descarga_datos)
        self.desc_grupo1.setGeometry(QtCore.QRect(9, 40, 411, 91))
        self.desc_grupo1.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.desc_grupo1.setObjectName("desc_grupo1")
        self.b_folio_input = QtWidgets.QLineEdit(self.desc_grupo1)
        self.b_folio_input.setGeometry(QtCore.QRect(80, 20, 111, 21))
        self.b_folio_input.setObjectName("b_folio_input")
        self.b_folio_text = QtWidgets.QLabel(self.desc_grupo1)
        self.b_folio_text.setGeometry(QtCore.QRect(10, 20, 61, 21))
        self.b_folio_text.setObjectName("b_folio_text")
        self.b_fecha_text = QtWidgets.QLabel(self.desc_grupo1)
        self.b_fecha_text.setGeometry(QtCore.QRect(230, 20, 61, 21))
        self.b_fecha_text.setObjectName("b_fecha_text")
        self.b_fecha_dia_input = QtWidgets.QLineEdit(self.desc_grupo1)
        self.b_fecha_dia_input.setGeometry(QtCore.QRect(280, 20, 21, 21))
        self.b_fecha_dia_input.setText("")
        self.b_fecha_dia_input.setMaxLength(2)
        self.b_fecha_dia_input.setAlignment(QtCore.Qt.AlignCenter)
        self.b_fecha_dia_input.setObjectName("b_fecha_dia_input")
        self.b_fecha_mes_input = QtWidgets.QLineEdit(self.desc_grupo1)
        self.b_fecha_mes_input.setGeometry(QtCore.QRect(310, 20, 21, 21))
        self.b_fecha_mes_input.setText("")
        self.b_fecha_mes_input.setMaxLength(2)
        self.b_fecha_mes_input.setAlignment(QtCore.Qt.AlignCenter)
        self.b_fecha_mes_input.setObjectName("b_fecha_mes_input")
        self.b_fecha_anno_input = QtWidgets.QLineEdit(self.desc_grupo1)
        self.b_fecha_anno_input.setGeometry(QtCore.QRect(340, 20, 61, 21))
        self.b_fecha_anno_input.setText("")
        self.b_fecha_anno_input.setMaxLength(4)
        self.b_fecha_anno_input.setAlignment(QtCore.Qt.AlignCenter)
        self.b_fecha_anno_input.setObjectName("b_fecha_anno_input")
        self.btn_buscar_datos = QtWidgets.QPushButton(self.desc_grupo1)
        self.btn_buscar_datos.setGeometry(QtCore.QRect(170, 50, 101, 31))
        self.btn_buscar_datos.setObjectName("btn_buscar_datos")
        self.desc_grupo2 = QtWidgets.QGroupBox(self.tab_descarga_datos)
        self.desc_grupo2.setGeometry(QtCore.QRect(430, 40, 551, 91))
        self.desc_grupo2.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.desc_grupo2.setObjectName("desc_grupo2")
        self.rang_fecha1_text = QtWidgets.QLabel(self.desc_grupo2)
        self.rang_fecha1_text.setGeometry(QtCore.QRect(10, 50, 41, 21))
        self.rang_fecha1_text.setObjectName("rang_fecha1_text")
        self.rang_fecha1_dia_input = QtWidgets.QLineEdit(self.desc_grupo2)
        self.rang_fecha1_dia_input.setGeometry(QtCore.QRect(50, 50, 31, 21))
        self.rang_fecha1_dia_input.setText("")
        self.rang_fecha1_dia_input.setMaxLength(2)
        self.rang_fecha1_dia_input.setAlignment(QtCore.Qt.AlignCenter)
        self.rang_fecha1_dia_input.setObjectName("rang_fecha1_dia_input")
        self.btn_buscar_datos_rang = QtWidgets.QPushButton(self.desc_grupo2)
        self.btn_buscar_datos_rang.setGeometry(QtCore.QRect(440, 50, 101, 31))
        self.btn_buscar_datos_rang.setObjectName("btn_buscar_datos_rang")
        self.b_fecha_text_3 = QtWidgets.QLabel(self.desc_grupo2)
        self.b_fecha_text_3.setGeometry(QtCore.QRect(90, 20, 21, 21))
        self.b_fecha_text_3.setObjectName("b_fecha_text_3")
        self.b_fecha_text_4 = QtWidgets.QLabel(self.desc_grupo2)
        self.b_fecha_text_4.setGeometry(QtCore.QRect(280, 20, 21, 21))
        self.b_fecha_text_4.setObjectName("b_fecha_text_4")
        self.rang_fecha1_mes_input = QtWidgets.QLineEdit(self.desc_grupo2)
        self.rang_fecha1_mes_input.setGeometry(QtCore.QRect(90, 50, 31, 21))
        self.rang_fecha1_mes_input.setText("")
        self.rang_fecha1_mes_input.setMaxLength(2)
        self.rang_fecha1_mes_input.setAlignment(QtCore.Qt.AlignCenter)
        self.rang_fecha1_mes_input.setObjectName("rang_fecha1_mes_input")
        self.rang_fecha1_anno_input = QtWidgets.QLineEdit(self.desc_grupo2)
        self.rang_fecha1_anno_input.setGeometry(QtCore.QRect(130, 50, 51, 21))
        self.rang_fecha1_anno_input.setText("")
        self.rang_fecha1_anno_input.setMaxLength(4)
        self.rang_fecha1_anno_input.setAlignment(QtCore.Qt.AlignCenter)
        self.rang_fecha1_anno_input.setObjectName("rang_fecha1_anno_input")
        self.rang_fecha2_dia_input = QtWidgets.QLineEdit(self.desc_grupo2)
        self.rang_fecha2_dia_input.setGeometry(QtCore.QRect(250, 50, 31, 21))
        self.rang_fecha2_dia_input.setText("")
        self.rang_fecha2_dia_input.setMaxLength(2)
        self.rang_fecha2_dia_input.setAlignment(QtCore.Qt.AlignCenter)
        self.rang_fecha2_dia_input.setObjectName("rang_fecha2_dia_input")
        self.rang_fecha2_dia_input_2 = QtWidgets.QLineEdit(self.desc_grupo2)
        self.rang_fecha2_dia_input_2.setGeometry(QtCore.QRect(300, 50, 31, 21))
        self.rang_fecha2_dia_input_2.setText("")
        self.rang_fecha2_dia_input_2.setMaxLength(2)
        self.rang_fecha2_dia_input_2.setAlignment(QtCore.Qt.AlignCenter)
        self.rang_fecha2_dia_input_2.setObjectName("rang_fecha2_dia_input_2")
        self.rang_fecha2_anno_input = QtWidgets.QLineEdit(self.desc_grupo2)
        self.rang_fecha2_anno_input.setGeometry(QtCore.QRect(350, 50, 51, 21))
        self.rang_fecha2_anno_input.setText("")
        self.rang_fecha2_anno_input.setMaxLength(4)
        self.rang_fecha2_anno_input.setAlignment(QtCore.Qt.AlignCenter)
        self.rang_fecha2_anno_input.setObjectName("rang_fecha2_anno_input")
        self.rang_fecha2_text = QtWidgets.QLabel(self.desc_grupo2)
        self.rang_fecha2_text.setGeometry(QtCore.QRect(200, 50, 41, 21))
        self.rang_fecha2_text.setObjectName("rang_fecha2_text")
        self.plainTextEdit = QtWidgets.QPlainTextEdit(self.tab_descarga_datos)
        self.plainTextEdit.setEnabled(False)
        self.plainTextEdit.setGeometry(QtCore.QRect(13, 220, 971, 321))
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.btn_exportar = QtWidgets.QPushButton(self.tab_descarga_datos)
        self.btn_exportar.setGeometry(QtCore.QRect(330, 170, 221, 31))
        self.btn_exportar.setObjectName("btn_exportar")
        self.tabWidget.addTab(self.tab_descarga_datos, "")
        self.config = QtWidgets.QWidget()
        self.config.setObjectName("config")
        self.groupBox = QtWidgets.QGroupBox(self.config)
        self.groupBox.setGeometry(QtCore.QRect(10, 10, 971, 101))
        self.groupBox.setObjectName("groupBox")
        self.ruta_guardado_text = QtWidgets.QLabel(self.groupBox)
        self.ruta_guardado_text.setGeometry(QtCore.QRect(10, 40, 141, 16))
        self.ruta_guardado_text.setObjectName("ruta_guardado_text")
        self.ruta_guardado_input = QtWidgets.QLineEdit(self.groupBox)
        self.ruta_guardado_input.setGeometry(QtCore.QRect(150, 40, 741, 20))
        self.ruta_guardado_input.setObjectName("ruta_guardado_input")
        self.btn_guardar = QtWidgets.QPushButton(self.groupBox)
        self.btn_guardar.setGeometry(QtCore.QRect(810, 70, 75, 23))
        self.btn_guardar.setObjectName("btn_guardar")
        self.tabWidget.addTab(self.config, "")
        self.titulo = QtWidgets.QLabel(self.centralwidget)
        self.titulo.setGeometry(QtCore.QRect(10, 0, 971, 61))
        font = QtGui.QFont()
        font.setPointSize(31)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.titulo.setFont(font)
        self.titulo.setAlignment(QtCore.Qt.AlignCenter)
        self.titulo.setWordWrap(False)
        self.titulo.setTextInteractionFlags(QtCore.Qt.NoTextInteraction)
        self.titulo.setObjectName("titulo")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "PROTECCION CIVIL"))
        self.folio_text.setText(_translate("MainWindow", "FOLIO"))
        self.turno_text.setText(_translate("MainWindow", "TURNO"))
        self.agente_text.setText(_translate("MainWindow", "AGENTE"))
        self.report_o_text.setText(_translate("MainWindow", "Reporto"))
        self.h_report_text.setText(_translate("MainWindow", "H. Reporte"))
        self.terminal_text.setText(_translate("MainWindow", "H. Terminal"))
        self.reporte_text.setText(_translate("MainWindow", "Reporte"))
        self.mun_region_text.setText(_translate("MainWindow", "Municipio/Region"))
        self.colonia_text.setText(_translate("MainWindow", "Col/Junta Auxiliar"))
        self.coord_text.setText(_translate("MainWindow", "Dir/Parje/Coordenadas"))
        self.dependencias_text.setText(_translate("MainWindow", "Dependencias Participantes"))
        self.acciones_text.setText(_translate("MainWindow", "Acciones de PC"))
        self.afectacion_text.setText(_translate("MainWindow", "Afectación"))
        self.desarollo_text.setText(_translate("MainWindow", "Desarrollo del Reporte"))
        self.btn_enviar.setText(_translate("MainWindow", "Enviar"))
        self.btn_cancelar.setText(_translate("MainWindow", "Cancelar"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_form), _translate("MainWindow", "FORMULARIO"))
        self.desc_grupo1.setTitle(_translate("MainWindow", "Individual"))
        self.b_folio_text.setText(_translate("MainWindow", "FOLIO*"))
        self.b_fecha_text.setText(_translate("MainWindow", "FECHA"))
        self.btn_buscar_datos.setText(_translate("MainWindow", "BUSCAR"))
        self.desc_grupo2.setTitle(_translate("MainWindow", "Rangos"))
        self.rang_fecha1_text.setText(_translate("MainWindow", "FECHA*"))
        self.btn_buscar_datos_rang.setText(_translate("MainWindow", "BUSCAR"))
        self.b_fecha_text_3.setText(_translate("MainWindow", "DE"))
        self.b_fecha_text_4.setText(_translate("MainWindow", "A"))
        self.rang_fecha2_text.setText(_translate("MainWindow", "FECHA*"))
        self.btn_exportar.setText(_translate("MainWindow", "EXPORTAR REGISTROS"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_descarga_datos), _translate("MainWindow", "OBTENER DATOS"))
        self.groupBox.setTitle(_translate("MainWindow", "GroupBox"))
        self.ruta_guardado_text.setText(_translate("MainWindow", "Ruta de guardado de datos*"))
        self.btn_guardar.setText(_translate("MainWindow", "Guardar"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.config), _translate("MainWindow", "CONFIGURACION"))
        self.titulo.setText(_translate("MainWindow", "PRUEBA TITULO"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
