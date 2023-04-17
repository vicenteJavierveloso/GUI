# Desarrolle un programa que permita desplegar una GUI que permita ingresar dos n ́umeros
# y muestre el resultado al presionar un bot ́on.
import sys
from PyQt6.QtCore import QSize, Qt
from PyQt6.QtWidgets import QMainWindow, QLabel, QLineEdit, QPushButton, QVBoxLayout, QWidget, QApplication

class Ventana(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle(f"GUI 5")
        self.setFixedSize(QSize(200,200))
        instruccion = QLabel(f"Ingresa dos números\ny presiona el boton\npara sumarlos")
        instruccion.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.numero_1 = QLineEdit()
        self.numero_2 = QLineEdit()
        self.resultado = QLabel("")
        boton = QPushButton(f"Sumar")
        boton.clicked.connect(lambda: self.suma(self.numero_1.text(), self.numero_2.text()))
        #layout
        layout = QVBoxLayout()
        layout.addWidget(instruccion)
        layout.addWidget(self.numero_1)
        layout.addWidget(self.numero_2)
        layout.addWidget(self.resultado)
        layout.addWidget(boton)
        contenedor = QWidget()
        contenedor.setLayout(layout)
        self.setCentralWidget(contenedor)

    def suma(self, a, b):
        try:
            a = int(a)
            b = int(b)
            self.resultado.setText(f"El resultado es {a+b}")
            self.numero_1.setText(f"")
            self.numero_2.setText(f"")
        except ValueError:
            self.resultado.setText(f"Ingresa solo numeros!")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ventana = Ventana()
    ventana.show()

    app.exec()