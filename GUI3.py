# Desarrolle un programa que permita desplegar una GUI que permita ingresar una palabra y
# muestre la cantidad de letras de la palabra.
import sys
from PyQt6.QtCore import QSize, Qt
from PyQt6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QLabel, QPushButton, QWidget, QLineEdit

class Ventana(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle(f"GUI 3")
        self.setFixedSize(QSize(200,200))
        #Elementos
        instruccion = QLabel(f"Ingresa una palabra,\nluego presiona el boton\npara contar las letras")
        instruccion.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.caja_de_texto = QLineEdit()
        self.palabra = QLabel("")
        self.palabra.setAlignment(Qt.AlignmentFlag.AlignCenter)
        boton = QPushButton("Contar")
        boton.clicked.connect(lambda: self.contar(self.caja_de_texto.text()))
        #layout
        layout = QVBoxLayout()
        #elementos al layout
        layout.addWidget(instruccion)
        layout.addWidget(self.caja_de_texto)
        layout.addWidget(self.palabra)
        layout.addWidget(boton)
        #insertar layout
        contenedor = QWidget()
        contenedor.setLayout(layout)
        self.setCentralWidget(contenedor)

    def contar(self, palabra):
        self.palabra.setText(f"La palabra tiene\n{str(len(palabra))}\nletras")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ventana = Ventana()
    ventana.show()

    app.exec()