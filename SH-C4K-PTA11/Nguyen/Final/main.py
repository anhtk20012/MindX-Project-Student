import sys, os
from PyQt6 import QtCore
from PyQt6.QtWidgets import QApplication, QWidget
from src import Welcome, Welcome_main, Login_main, Register_main, Main_interface

from pathlib import Path
os.chdir(Path(__file__).parent)

class Signal(QWidget):
    welcome = QtCore.pyqtSignal()
    welcome_main = QtCore.pyqtSignal(QtCore.QPoint)
    main_login = QtCore.pyqtSignal(QtCore.QPoint)
    main_register = QtCore.pyqtSignal(QtCore.QPoint)
    main_interface = QtCore.pyqtSignal(QtCore.QPoint)
    
class Main_App(QWidget):
    def __init__(self):
        self.signal = Signal()
        self.welcome = Welcome.welcome(self.signal)
        self.welcome_main = Welcome_main.welcome_main(self.signal)
        self.main_login = Login_main.main_login(self.signal)
        self.main_register = Register_main.main_register(self.signal)
        self.main_interface = Main_interface.main_interface(self.signal)
        
        self.signal.welcome.connect(self.welcome.welcome_open)
        self.signal.welcome_main.connect(self.welcome_main.welcome_main_open)
        self.signal.main_login.connect(self.main_login.main_login_open)
        self.signal.main_register.connect(self.main_register.main_register_open)
        self.signal.main_interface.connect(self.main_interface.main_interface_open)
    
    def main_show(self):
        self.signal.welcome.emit()
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    windows = Main_App()
    windows.main_show()
    app.exec()