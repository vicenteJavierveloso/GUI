# Desarrolle un programa que permita desplegar una GUI que permita ingresar un n ́umero y
# determine si es primo o no
import sys
from PyQt6.QtCore import QSize, Qt
from PyQt6.QtWidgets import QMainWindow, QLineEdit, QLabel, QPushButton, QWidget, QVBoxLayout, QApplication

class Ventana(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setFixedSize(QSize(200,200))
        self.setWindowTitle(f"GUI 4")
        #Elementos
        instruccion = QLabel(f"Ingrese un número")
        instruccion.setAlignment(Qt.AlignmentFlag.AlignCenter)
        caja_numero = QLineEdit("")
        self.resultado = QLabel()
        self.resultado.setAlignment(Qt.AlignmentFlag.AlignCenter)
        boton = QPushButton(f"Verificar")
        boton.clicked.connect(lambda: self.es_primo(caja_numero.text()))
        #Layout
        layout = QVBoxLayout()
        layout.addWidget(instruccion)
        layout.addWidget(caja_numero)
        layout.addWidget(self.resultado)
        layout.addWidget(boton)
        contenedor = QWidget()
        contenedor.setLayout(layout)
        self.setCentralWidget(contenedor)
    
    def es_primo(self,n):
        try:
            n = int(n)+1
            aux = []
            x = 0
            for i in range(1,n):
                x = 1
                contador = 0
                while x <= i:
                    if i%x ==0:
                        contador += 1
                    x += 1
                if contador ==2:
                    aux.append(i)
            contador = aux.count(n-1)
            if contador > 0:
                self.resultado.setText(f"{n-1} es primo")
            else:
                self.resultado.setText(f"{n-1} no es primo")
        except ValueError:
            self.resultado.setText(f"Ingresa solo numeros!")


        


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ventana = Ventana()
    ventana.show()
    app.exec()

    
        