# Desarrolle un programa que permita desplegar una GUI que permita ingresar una palabra y
# al presionar un boton, se muestre la palabra al rev ́es.
import sys
from PyQt6.QtCore import QSize, Qt
from PyQt6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QLabel, QPushButton, QWidget, QLineEdit
import random

class Ventana(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle(f"GUI 2")
        self.setFixedSize(QSize(200,200))
        #Elementos
        instruccion = QLabel(f"Ingresa una palabra\nluego presione el boton\npara invertirla.")
        instruccion.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.caja_de_texto = QLineEdit()
        self.palabra = QLabel("")
        self.palabra.setAlignment(Qt.AlignmentFlag.AlignCenter)
        boton = QPushButton("Invertir")
        boton.clicked.connect(lambda: self.reves(self.caja_de_texto.text()))
        #layout
        layout = QVBoxLayout()
        #elementos al layout
        layout.addWidget(instruccion)
        layout.addWidget(self.caja_de_texto)
        layout.addWidget(self.palabra)
        layout.addWidget(boton)
        #insertar layout
        ventana = QWidget()
        ventana.setLayout(layout)
        self.setCentralWidget(ventana)

    def reves(self, palabra):
        aux = ""
        palabra = list(palabra)
        palabra.reverse()
        for i in range(len(palabra)):
            aux += palabra[i]
        self.caja_de_texto.setText("")
        self.palabra.setText(aux)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ventana = Ventana()
    ventana.show()

    app.exec()