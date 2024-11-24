import sys, os
from PyQt6 import QtCore
from PyQt6.QtWidgets import QApplication, QWidget
from src import welcome, sign_up, main_ui_1, main_ui_2, login

from pathlib import Path
os.chdir(Path(__file__).parent)

class Signal(QWidget):
    welcome = QtCore.pyqtSignal()
    sign_up = QtCore.pyqtSignal(QtCore.QPoint)
    login = QtCore.pyqtSignal(QtCore.QPoint)
    main_ui_1 = QtCore.pyqtSignal(QtCore.QPoint)
    main_ui_2 = QtCore.pyqtSignal(QtCore.QPoint)
    
class Main_App(QWidget):
    def __init__(self):
        self.signal = Signal()
        self.welcome = welcome.Welcome(self.signal)
        self.sign_up = sign_up.Sign_up(self.signal)
        self.login = login.Login(self.signal)
        self.main_ui_1 = main_ui_1.Main_ui_1(self.signal)
        self.main_ui_2 = main_ui_2.Main_ui_2(self.signal)
        
        self.signal.welcome.connect(self.welcome.welcome_open)
        self.signal.sign_up.connect(self.sign_up.sign_up_open)
        self.signal.main_ui_1.connect(self.main_ui_1.main_ui_1_open)
        self.signal.main_ui_2.connect(self.main_ui_2.main_ui_2_open)
        self.signal.login.connect(self.login.login_open)
        
    def main_show(self):
        self.signal.welcome.emit()
    
if __name__ == "__main__":
    app = QApplication(sys.argv)
    windows = Main_App()
    windows.main_show()
    app.exec()