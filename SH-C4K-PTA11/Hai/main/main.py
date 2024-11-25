import sys, os
from PyQt6 import QtCore
from PyQt6.QtWidgets import QApplication, QWidget
from src import welcome, welcome_main, SignIn, login, page, page2

from pathlib import Path
os.chdir(Path(__file__).parent)

class Signal(QWidget):
    welcome = QtCore.pyqtSignal(QtCore.QPoint)
    welcome_main = QtCore.pyqtSignal(QtCore.QPoint)
    
class Main_App(QWidget):
    def __init__(self):
        self.signal = Signal()
        self.welcome = welcome.Welcome(self.signal)
        self.welcome_main = welcome_main.Welcome_main(self.signal)
        
        self.signal.welcome.connect(self.welcome.welcome_open)
        self.signal.welcome_main.connect(self.welcome_main.welcome_main_open)
        
    def main_show(self):
        self.signal.welcome.emit()
        self.signal.welcome_main.emit()
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    windows = Main_App()
    windows.main_show
    app.exec()