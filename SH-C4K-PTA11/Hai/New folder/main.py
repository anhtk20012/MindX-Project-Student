import sys, os
from PyQt6 import QtCore, uic
from PyQt6.QtWidgets import QApplication, QWidget, QMainWindow

from pathlib import Path
os.chdir(Path(__file__).parent)

class Signal(QWidget):
    login = QtCore.pyqtSignal()
    register = QtCore.pyqtSignal()

class Login(QMainWindow):
    def __init__(self, signal = None):
        super().__init__()
        self.ui = uic.loadUi('./ui/Login_main.ui', self)

        self.ui.pushButton_2.clicked.connect(self.show_register)
        
    def login_open(self):
        self.show()
    
    def show_register(self):
        self.close()
        signal.register.emit()
        
class Register(QMainWindow):
    def __init__(self, signal = None):
        super().__init__()
        self.ui = uic.loadUi('./ui/Register_main.ui', self)
        
        self.ui.pushButton_2.clicked.connect(self.show_login)
        
    def register_open(self):
        self.show()
    
    def show_login(self):
        self.close()
        signal.login.emit()
            
if __name__ == "__main__":
    app = QApplication(sys.argv)
    signal = Signal()
    windows_login = Login(signal)
    windows_register = Register(signal)
    
    signal.login.connect(windows_login.login_open)
    signal.register.connect(windows_register.register_open)
    
    windows_login.login_open()
    app.exec()