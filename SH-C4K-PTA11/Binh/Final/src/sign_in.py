import os
from pathlib import Path
from PyQt6 import uic, QtCore
from PyQt6.QtWidgets import QMainWindow, QMessageBox

class Sign_in(QMainWindow):
    def __init__(self, signal=None):
        super().__init__()
        os.chdir(Path(__file__).parent)
        self.ui = uic.loadUi('../ui/Sign_in.ui', self)
        
        # Thiết lập để lấy lại vị trí cũ và sinal
        self.old_pos = None
        self.signal = signal
        
        # Thiết lập xóa bỏ các nút tắt, thu nhỏ, phóng to
        self.setWindowFlag(QtCore.Qt.WindowType.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WidgetAttribute.WA_TranslucentBackground)

        self.ui.pushButton.clicked.connect(self.signup_show)
        self.ui.pushButton_2.clicked.connect(self.welcome2_show)
        self.ui.pushButton_3.clicked.connect(self.main_interface_show)
        
    def signin_open(self):
        self.show()

    def signup_show(self):
        self.ui.lineEdit.clear()
        self.ui.lineEdit_2.clear()
        self.close()
        self.signal.signup.emit(self.pos())

    def welcome2_show(self):
        self.ui.lineEdit.clear()
        self.ui.lineEdit_2.clear()
        self.close()
        self.signal.welcome2.emit(self.pos())

    def main_interface_show(self):
        self.ui.lineEdit.clear()
        self.ui.lineEdit_2.clear()
        self.close()
        self.signal.main_interface.emit(self.pos())
                
# <-- Nâng cao cho chương trình -->
# Giúp chương trình có thể di chuyển và lấy được vị trí cũ

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
                    
#if __name__ == "__main__":
#    from PyQt6.QtWidgets import QApplication
#    import sys
#    app = QApplication(sys.argv)
#    windows = Sign_in()
#    windows.show()
#    app.exec()
    