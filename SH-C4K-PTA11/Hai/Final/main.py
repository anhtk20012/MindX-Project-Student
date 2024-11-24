import sys, os
from PyQt6 import QtCore
from PyQt6.QtWidgets import QApplication, QWidget
from src import welcome, welcome_main, signup, login, page, page2

from pathlib import Path
os.chdir(Path(__file__).parent)

class Signal(QWidget):
    welcome = QtCore.pyqtSignal()
    welcome_main = QtCore.pyqtSignal(QtCore.QPoint)
    signup = QtCore.pyqtSignal(QtCore.QPoint)
    login = QtCore.pyqtSignal(QtCore.QPoint)
    page = QtCore.pyqtSignal(QtCore.QPoint)
    page2 = QtCore.pyqtSignal(QtCore.QPoint)
    
class Main_App(QWidget):
    def __init__(self):
        self.signal = Signal()
        self.welcome = welcome.Welcome(self.signal)
        self.welcome_main = welcome_main.Welcome_main(self.signal)
        self.signup = signup.Signup(self.signal)
        self.login = login.Login(self.signal)
        self.page = page.Page(self.signal)
        self.page2 = page2.Page2(self.signal)
        
        self.signal.welcome.connect(self.welcome.welcome_open)
        self.signal.welcome_main.connect(self.welcome_main.welcome_main_open)
        self.signal.signup.connect(self.signup.signup_open)
        self.signal.login.connect(self.login.login_open)
        self.signal.page.connect(self.page.page_open)
        self.signal.page2.connect(self.page2.page2_open)
        
    def main_show(self):
        self.signal.welcome.emit()
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    windows = Main_App()
    windows.main_show()
    app.exec()