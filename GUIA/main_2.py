import sys
from PyQt6 import QtCore
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QStackedLayout, QPushButton, QLabel, QHBoxLayout, QVBoxLayout

class VentanaPrincipal(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Aplicacion")
        #Elementos Generales
        boton_iniciar = QPushButton("Iniciar Sesion")
        boton_registrar = QPushButton("Registrarse")
        


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ventana = VentanaPrincipal()
    ventana.show()
    app.exec()