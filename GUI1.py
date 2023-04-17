# Desarrolle un programa que permita desplegar una GUI que muestre un boton que, al 
# presionarlo, muestre un numero aleatorio.
import sys
from PyQt6.QtCore import QSize, Qt
from PyQt6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QLabel, QPushButton, QWidget
import random

class Ventana(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle(f"GUI 1")
        self.setFixedSize(QSize(200,200))
        #Elementos
        texto = QLabel(f"Presiona el boton para un numero\naleatorio.")
        texto.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.numero = QLabel(f"")
        self.numero.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.boton = QPushButton(f"Boton")
        self.boton.clicked.connect(self.numero_aleatorio)
        #Layout
        layout = QVBoxLayout()
        layout.addWidget(texto)
        layout.addWidget(self.numero)
        layout.addWidget(self.boton)
        contenedor = QWidget()
        contenedor.setLayout(layout)
        self.setCentralWidget(contenedor)
        
    def numero_aleatorio(self):
        num = random.randint(0, 10)
        self.numero.setText(f"El numero es {num}")
        self.boton.setText(f"Intenta denuevo")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ventana = Ventana()
    ventana.show()

    app.exec()
