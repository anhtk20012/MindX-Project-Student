import os
from pathlib import Path
from PyQt6 import uic, QtCore
from PyQt6.QtWidgets import QMainWindow, QMessageBox

class Tostarted(QMainWindow):
    def __init__(self, signal=None):
        super().__init__()
        os.chdir(Path(__file__).parent)
        self.ui = uic.loadUi('../ui/tostarted.ui', self)
        
        self.old_pos = None
        self.signal = signal
        
        self.setWindowFlag(QtCore.Qt.WindowType.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WidgetAttribute.WA_TranslucentBackground)

        self.ui.pushButton_2.clicked.connect(self.tomusic_show)
        self.ui.pushButton_3.clicked.connect(self.tosignup_show)
        
    def tostarted_open(self, position):
        self.show()
        self.move(position)

    def tosignup_show(self):
        self.ui.lineEdit.clear()
        self.ui.lineEdit_2.clear()
        self.close()
        self.signal.tosignup.emit(self.pos())

    def tomusic_show(self):
        self.ui.lineEdit.clear()
        self.ui.lineEdit_2.clear()
        self.close()
        self.signal.tomusic.emit(self.pos())
                        
    # def main_1_show(self):
    #     self.ui.lineEdit.clear()
    #     self.ui.lineEdit_2.clear()
    #     self.close()
    #     self.signal.main_ui_1.emit(self.pos())
    
    # def sign_up_show(self):
    #     self.ui.lineEdit.clear()
    #     self.ui.lineEdit_2.clear()
    #     self.close()
    #     self.signal.sign_up.emit(self.pos())

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

     
