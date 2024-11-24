import os
from pathlib import Path
from PyQt6 import uic, QtCore
from PyQt6.QtWidgets import QMainWindow, QMessageBox

class main_register(QMainWindow):
    def __init__(self, signal=None):
        super().__init__()
        os.chdir(Path(__file__).parent)
        self.ui = uic.loadUi('../ui/Register_main.ui', self)
        
        self.old_pos = None
        self.signal = signal
        
        self.setWindowFlag(QtCore.Qt.WindowType.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WidgetAttribute.WA_TranslucentBackground)

        self.ui.pushButton.clicked.connect(self.main_login_show)
        self.ui.pushButton_2.clicked.connect(self.main_login_show)
        
    def main_register_open(self, position):
        self.show()
        self.move(position)

    def main_login_show(self):
        self.clean_text()
        self.close()
        self.signal.main_login.emit(self.pos())
    
    def clean_text(self):
        self.ui.lineEdit.setText("")
        self.ui.lineEdit_2.setText("")
        self.ui.lineEdit_3.setText("")
        
    def mousePressEvent(self, event):
        if event.button() == QtCore.Qt.MouseButton.LeftButton:
            self.old_pos = event.globalPosition().toPoint()
    
    def mouseMoveEvent(self, event):
        if self.old_pos is not None:
            delta = event.globalPosition().toPoint() - self.old_pos
            self.move(self.pos() + delta)
            self.old_pos = event.globalPosition().toPoint()
            
    def mouseReleaseEvent(self, event):
        if event.button() == QtCore.Qt.MouseButton.LeftButton:
            self.old_pos = None
    
    def keyPressEvent(self, event):
        if event.key() == QtCore.Qt.Key.Key_Escape:
            self.close_application()
    
    def close_application(self):
        reply = QMessageBox.question(
                    self, 'Exit', 'Are you sure you want to exit?', 
                    QMessageBox.StandardButton.Yes | 
                    QMessageBox.StandardButton.No, QMessageBox.StandardButton.No
                )
        if reply == QMessageBox.StandardButton.Yes:
            self.close()