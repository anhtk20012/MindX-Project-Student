import os
from pathlib import Path
from PyQt6 import uic, QtCore
from PyQt6.QtWidgets import QMainWindow, QMessageBox

class Main_interface(QMainWindow):
    def __init__(self, signal=None):
        super().__init__()
        os.chdir(Path(__file__).parent)
        self.ui = uic.loadUi('../ui/Main.ui', self)
        
        # Thiết lập để lấy lại vị trí cũ và sinal
        self.old_pos = None
        self.signal = signal
        
        # Thiết lập xóa bỏ các nút tắt, thu nhỏ, phóng to
        self.setWindowFlag(QtCore.Qt.WindowType.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WidgetAttribute.WA_TranslucentBackground)
        
        self.ui.pushButton_2.clicked.connect(self.camping_show)
        self.ui.pushButton_3.clicked.connect(self.beach_show)
        self.ui.pushButton_4.clicked.connect(self.kayak_show)
        self.ui.pushButton_5.clicked.connect(self.mountain_show)
        self.ui.pushButton_8.clicked.connect(self.menu_show)
        self.ui.pushButton_6.clicked.connect(self.everest_show)
        self.ui.pushButton_7.clicked.connect(self.close_application)
    def main_interface_open(self):
        self.show()
    def camping_show(self):
        self.close()
        self.signal.camping.emit(self.pos())
    def beach_show(self):
        self.close()
        self.signal.beach.emit(self.pos())
    def kayak_show(self):
        self.close()
        self.signal.kayak.emit(self.pos())
    def mountain_show(self):
        self.close()
        self.signal.mountain.emit(self.pos())
    def menu_show(self):
        self.close()
        self.signal.menu.emit(self.pos())
    def everest_show(self):
        self.close()
        self.signal.everest.emit(self.pos())
        
        
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
                    
# if __name__ == "__main__":
#    from PyQt6.QtWidgets import QApplication
#    import sys
#    app = QApplication(sys.argv)
#    windows = Main_interface()
#    windows.show()
#    app.exec()
    