import sys, os
from PyQt6 import QtCore
from PyQt6.QtWidgets import QApplication, QWidget
from src import sikbii, started, tostarted, tosignup, tomusic

from pathlib import Path
os.chdir(Path(__file__).parent)

class Signal(QWidget):
    sikbii = QtCore.pyqtSignal()
    started = QtCore.pyqtSignal(QtCore.QPoint)
    tostarted = QtCore.pyqtSignal(QtCore.QPoint)
    tosignup = QtCore.pyqtSignal(QtCore.QPoint)
    tomusic = QtCore.pyqtSignal(QtCore.QPoint)
    
class Main_App(QWidget):
    def __init__(self):
        self.signal = Signal()
        self.sikbii = sikbii.Sikbii(self.signal)
        self.started = started.Started(self.signal)
        self.tostarted = tostarted.Tostarted(self.signal)
        self.tosignup = tosignup.Tosignup(self.signal)
        self.tomusic = tomusic.Tomusic(self.signal)
        
        self.signal.sikbii.connect(self.sikbii.sikbii_open)
        self.signal.started.connect(self.started.started_open)
        self.signal.tostarted.connect(self.tostarted.tostarted_open)
        self.signal.tosignup.connect(self.tosignup.tosignup_open)
        self.signal.tomusic.connect(self.tomusic.tomusic_open)
        
    def main_show(self):
        self.signal.sikbii.emit()
    
if __name__ == "__main__":
    app = QApplication(sys.argv)
    windows = Main_App()
    windows.main_show()
    app.exec()