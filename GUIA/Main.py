import sys
import typing
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QTableWidgetItem, QDateEdit, QTableWidget, QHBoxLayout,QVBoxLayout, QCheckBox ,QRadioButton, QMainWindow, QWidget, QPushButton, QApplication, QGridLayout, QLabel, QLineEdit, QPlainTextEdit, QSpinBox, QSlider, QComboBox


class VentanaPrincipal(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setFixedSize(750,800)
        self.setWindowTitle("Ejercicios de GUIs")
        #Elementos
        boton = QPushButton("Aceptar")
        boton.clicked.connect(self.mostrar)
        #-Labels
        self.label_resultado = QLabel("Mensaje del boton")
        self.label_resultado.setAlignment(Qt.AlignmentFlag.AlignCenter)
        label_nom_ap = QLabel("Nombre y Apellido")
        label_descripcion = QLabel("Descripcion")
        label_edad = QLabel("Edad")
        self.label_altura = QLabel(f"Altura 0 cm")
        label_ced_pas = QLabel("Cedula de identidad / Pasaporte")
        label_identificador = QLabel("Identificador del Documento")
        label_genero = QLabel("Género")
        label_estado_civ = QLabel("Estado civil")
        label_nivel = QLabel("Nivel educativo")
        label_habilidades = QLabel("Habilidades")
        label_nivel_ingles = QLabel("Nivel de Inglés")
        label_nacimiento = QLabel("Fecha de Nacimiento")
        label_nombreusuario = QLabel("Nombre de Usuario (Sin espacios)")
        label_contrasena = QLabel("Contraseña (Sin espacios)")

        #-Entradas
        self.entrada_nom_ap = QLineEdit()
        self.entrada_descripcion = QPlainTextEdit()
        self.entrada_descripcion.setFixedSize(466,100)
        self.entrada_edad = QSpinBox()
        #  Slider altura
        self.entrada_altura = QSlider(Qt.Orientation.Horizontal)
        self.entrada_altura.setMaximum(300)
        self.entrada_altura.setTickInterval(50)
        self.entrada_altura.setTickPosition(QSlider.TickPosition.TicksAbove)
        self.entrada_altura.valueChanged.connect(lambda: self.label_altura.setText(f"Altura {self.entrada_altura.value()} cm"))
        
        #Cedula de identidad o pasaporte
        ced_pas_layout = QHBoxLayout()
        self.entrada_ced_pas = QSlider(Qt.Orientation.Horizontal)
        self.entrada_ced_pas.setMaximum(1)
        self.entrada_ced_pas.setFixedWidth(30)
        ced = QLabel("Cedula de Identidad")
        ced.setAlignment(Qt.AlignmentFlag.AlignCenter)
        pas = QLabel("Pasaporte")
        pas.setAlignment(Qt.AlignmentFlag.AlignCenter)
        ced_pas_layout.addWidget(ced)
        ced_pas_layout.addWidget(self.entrada_ced_pas)
        ced_pas_layout.addWidget(pas)
        
        ced_pas = QWidget()
        ced_pas.setLayout(ced_pas_layout)

        self.entrada_identificador = QLineEdit()
        
        self.entrada_genero = QComboBox()
        self.entrada_genero.addItems(["Masculino", "Femenino", "Otro"])
        self.entrada_genero.currentTextChanged.connect(lambda: self.genero(self.entrada_genero.currentText()))

        self.entrada_estado_civ = QComboBox()
        self.entrada_estado_civ.addItems(["Soltero", "Casado", "Divorciado"])

        #Creo un widget que contiene los dos RadioButtons
        nivel = QWidget()
        #Le doy un layout
        nivel_layout = QVBoxLayout()
        #Elementos
        self.entrada_nivel1 = QRadioButton("Estudiante")
        self.entrada_nivel1.setChecked(True)
        self.entrada_nivel2 = QRadioButton("Egresado")
        #Añado
        nivel_layout.addWidget(self.entrada_nivel1)
        nivel_layout.addWidget(self.entrada_nivel2)
        #Seteo el layout al widget
        nivel.setLayout(nivel_layout)

        #Creo widget que contiene checkboxes
        habilidades = QWidget()

        habilidades_layout = QVBoxLayout()
        self.entrada_habilidades_prog = QCheckBox("Programacion")
        self.entrada_habilidades_ges = QCheckBox("Gestion")
        self.entrada_habilidades_soc = QCheckBox("Habilidades sociales")
        self.entrada_habilidades_idi = QCheckBox("Manejo de Idiomas")
        habilidades_layout.addWidget(self.entrada_habilidades_prog)
        habilidades_layout.addWidget(self.entrada_habilidades_ges)
        habilidades_layout.addWidget(self.entrada_habilidades_soc)
        habilidades_layout.addWidget(self.entrada_habilidades_idi)

        habilidades.setLayout(habilidades_layout)

        self.entrada_nivel_ingles = QComboBox()
        self.entrada_nivel_ingles.addItems(["A1","A2","B1","B2","C1","C2"])
        
        self.entrada_nacimiento = QDateEdit()
        self.entrada_nacimiento.setCalendarPopup(True)

        self.entrada_nombreusuario = QLineEdit()
        self.entrada_contrasena = QLineEdit()
        self.entrada_contrasena.setEchoMode(QLineEdit.EchoMode.PasswordEchoOnEdit)

        self.visor = QTableWidget()
        self.visor.setColumnCount(12)
        self.visor.setHorizontalHeaderItem(0,QTableWidgetItem("Nombre y Apellido"))
        self.visor.setHorizontalHeaderItem(1,QTableWidgetItem("Descripcion"))
        self.visor.setHorizontalHeaderItem(2,QTableWidgetItem("Edad"))
        self.visor.setHorizontalHeaderItem(3,QTableWidgetItem("Altura"))
        self.visor.setHorizontalHeaderItem(4,QTableWidgetItem("Identificador Documento"))
        self.visor.setHorizontalHeaderItem(5,QTableWidgetItem("Género"))
        self.visor.setHorizontalHeaderItem(6,QTableWidgetItem("Estado Civil"))
        self.visor.setHorizontalHeaderItem(7,QTableWidgetItem("Nivel educativo"))
        self.visor.setHorizontalHeaderItem(8,QTableWidgetItem("Habilidades"))
        self.visor.setHorizontalHeaderItem(9,QTableWidgetItem("Nivel de Ingles"))
        self.visor.setHorizontalHeaderItem(10,QTableWidgetItem("Fecha de nacimiento"))
        self.visor.setHorizontalHeaderItem(11,QTableWidgetItem("Nombre de usuario"))

        #Layout
        contenedor = QGridLayout()

        #Añadir elementos al contenedor
        #Columna 1
        contenedor.addWidget(label_nom_ap,0,0)
        contenedor.addWidget(label_descripcion,1,0)
        contenedor.addWidget(label_edad,2,0)
        contenedor.addWidget(self.label_altura,3,0)
        contenedor.addWidget(label_ced_pas,4,0)
        contenedor.addWidget(label_identificador,5,0)
        contenedor.addWidget(label_genero,6,0)
        contenedor.addWidget(label_estado_civ,7,0)
        contenedor.addWidget(label_nivel,8,0)
        contenedor.addWidget(label_habilidades,9,0)
        contenedor.addWidget(label_nivel_ingles,10,0)
        contenedor.addWidget(label_nacimiento,11,0)
        contenedor.addWidget(label_nombreusuario,12,0)
        contenedor.addWidget(label_contrasena,13,0)
        #Columna 2
        contenedor.addWidget(self.entrada_nom_ap,0,1)
        contenedor.addWidget(self.entrada_descripcion,1,1)
        contenedor.addWidget(self.entrada_edad,2,1)
        contenedor.addWidget(self.entrada_altura,3,1)
        contenedor.addWidget(ced_pas,4,1)
        contenedor.addWidget(self.entrada_identificador,5,1)
        contenedor.addWidget(self.entrada_genero,6,1)
        contenedor.addWidget(self.entrada_estado_civ,7,1)
        #Usar el widget de RadioButton
        contenedor.addWidget(nivel,8,1)
        contenedor.addWidget(habilidades,9,1)
        contenedor.addWidget(self.entrada_nivel_ingles,10,1)
        contenedor.addWidget(self.entrada_nacimiento,11,1)
        contenedor.addWidget(self.entrada_nombreusuario,12,1)
        contenedor.addWidget(self.entrada_contrasena,13,1)
        contenedor.addWidget(self.visor,20,1)
        #Columna 3
        contenedor.addWidget(boton,0,2)

        #Darle comportamiento de widget al contenedor grid y asignarlo a la ventana principal.
        contenedor_principal = QWidget()
        contenedor_principal.setLayout(contenedor)
        self.setCentralWidget(contenedor_principal)

    # def mostrar(self):
    #     if self.entrada_nivel1.isChecked() == True:
    #         if self.entrada_ced_pas.value() == 0:
    #             self.label_resultado.setText(f"{self.entrada_nom_ap.text()} - {self.entrada_descripcion.toPlainText()} - {self.entrada_edad.value()} - {self.entrada_altura.value()} cm - Cedula de Identidad {self.entrada_identificador.text()} - {self.entrada_genero.currentText()} - {self.entrada_estado_civ.currentText()} - Estudiante")
    #         else:
    #             self.label_resultado.setText(f"{self.entrada_nom_ap.text()} - {self.entrada_descripcion.toPlainText()} - {self.entrada_edad.value()} - {self.entrada_altura.value()} cm - Pasaporte {self.entrada_identificador.text()} - {self.entrada_genero.currentText()} - {self.entrada_estado_civ.currentText()} - Estudiante")
    #     else:
    #         if self.entrada_ced_pas.value() == 0:
    #             self.label_resultado.setText(f"{self.entrada_nom_ap.text()} - {self.entrada_descripcion.toPlainText()} - {self.entrada_edad.value()} - {self.entrada_altura.value()} cm - Cedula de Identidad {self.entrada_identificador.text()} - {self.entrada_genero.currentText()} - {self.entrada_estado_civ.currentText()}- Egresado")
    #         else:
    #             self.label_resultado.setText(f"{self.entrada_nom_ap.text()} - {self.entrada_descripcion.toPlainText()} - {self.entrada_edad.value()} - {self.entrada_altura.value()} cm - Pasaporte {self.entrada_identificador.text()} - {self.entrada_genero.currentText()} - {self.entrada_estado_civ.currentText()} - Egresado")
    
    def anadir(self,nom_ap,descripcion,edad,altura,)
    
    def genero(self, valor):
        if valor == "Masculino":
            self.entrada_estado_civ.clear()
            self.entrada_estado_civ.addItems(["Soltero", "Casado", "Divorciado"])
        elif valor == "Femenino":
            self.entrada_estado_civ.clear()
            self.entrada_estado_civ.addItems(["Soltera", "Casada", "Divorciada"])
        else:
            self.entrada_estado_civ.clear()
            self.entrada_estado_civ.addItems(["Solterx", "Casadx", "Divorciadx"])

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ventana = VentanaPrincipal()
    ventana.show()
    app.exec()