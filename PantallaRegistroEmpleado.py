# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'RegistroEmpleados.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from base_datos import conn

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(873, 362)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.nombre = QtWidgets.QLineEdit(self.centralwidget)
        self.nombre.setGeometry(QtCore.QRect(130, 80, 113, 23))
        self.nombre.setObjectName("nombre")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(70, 80, 54, 15))
        self.label.setObjectName("label")
        self.sueldo = QtWidgets.QLineEdit(self.centralwidget)
        self.sueldo.setGeometry(QtCore.QRect(130, 170, 113, 23))
        self.sueldo.setText("")
        self.sueldo.setObjectName("sueldo")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(70, 140, 54, 15))
        self.label_2.setObjectName("label_2")
        self.guardar = QtWidgets.QPushButton(self.centralwidget)
        self.guardar.setGeometry(QtCore.QRect(80, 210, 81, 21))
        self.guardar.setObjectName("guardar")
        self.actualizar = QtWidgets.QPushButton(self.centralwidget)
        self.actualizar.setGeometry(QtCore.QRect(190, 210, 91, 21))
        self.actualizar.setObjectName("actualizar")
        self.listaEmpleados = QtWidgets.QTableWidget(self.centralwidget)
        self.listaEmpleados.setGeometry(QtCore.QRect(320, 70, 521, 211))
        self.listaEmpleados.setObjectName("listaEmpleados")
        self.listaEmpleados.setColumnCount(0)
        self.listaEmpleados.setRowCount(0)
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(70, 110, 54, 15))
        self.label_3.setObjectName("label_3")
        self.apellido = QtWidgets.QLineEdit(self.centralwidget)
        self.apellido.setGeometry(QtCore.QRect(130, 110, 113, 23))
        self.apellido.setText("")
        self.apellido.setObjectName("apellido")
        self.cargo = QtWidgets.QLineEdit(self.centralwidget)
        self.cargo.setGeometry(QtCore.QRect(130, 140, 113, 23))
        self.cargo.setText("")
        self.cargo.setObjectName("cargo")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(70, 170, 54, 15))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(70, 20, 221, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 873, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        # Manejo de base de datos
        self.crear_base()
        self.obtener_informacion()
        self.guardar.clicked.connect(self.guardar_informacion)
        self.actualizar.clicked.connect(self.obtener_informacion)
        #

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        
    def crear_base(self):
            cursor = conn.cursor()
            cadena_sql = 'CREATE TABLE Empleado (nombre TEXT,apellido TEXT,cargo TEXT, sueldo INTEGER, bono FLOAT)'
            try:
                cursor.execute(cadena_sql)
            except:
                pass
            cursor.close()

    def guardar_informacion(self):
        cursor = conn.cursor()
        nombre = str(self.nombre.text())
        apellido = str(self.apellido.text())
        cargo = str(self.cargo.text())
        sueldo = int(self.sueldo.text())
        bono = sueldo*0.10
        cadena_sql = """INSERT INTO Empleado (nombre, apellido, cargo, sueldo, bono) VALUES ('%s','%s','%s', %d, %s);""" % \
    (nombre, apellido, cargo, sueldo, bono)
        # ejecutar el SQL
        cursor.execute(cadena_sql)
        # confirmar los cambios
        conn.commit()
        cursor.close()

    def obtener_informacion(self):
        cursor = conn.cursor()
        cadena_consulta_sql = "SELECT * from Empleado"
        cursor.execute(cadena_consulta_sql)
        informacion = cursor.fetchall()
        database_table_column_count = 5
        self.listaEmpleados.setColumnCount(database_table_column_count)
        numero_filas = len(informacion)
        self.listaEmpleados.setRowCount(numero_filas)
        for j in range(numero_filas):
            valor = informacion[j]
            for i in range(0, len(valor)):
                elemento = valor[i]
                elemento = str(elemento)
                nuevo_registro = QtWidgets.QTableWidgetItem(elemento)
                self.listaEmpleados.setItem(j, i, nuevo_registro)
             
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Nombre"))
        self.label_2.setText(_translate("MainWindow", "Cargo"))
        self.guardar.setText(_translate("MainWindow", "Guardar"))
        self.actualizar.setText(_translate("MainWindow", "Actualizar"))
        self.label_3.setText(_translate("MainWindow", "Apellido"))
        self.label_4.setText(_translate("MainWindow", "Sueldo"))
        self.label_5.setText(_translate("MainWindow", "Registro de empleados"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
