import os
from pathlib import Path
from PyQt6 import uic, QtCore
from PyQt6.QtWidgets import QMainWindow, QMessageBox

class Mountain (QMainWindow):
    def __init__(self, signal=None):
        super().__init__()
        os.chdir(Path(__file__).parent)
        self.ui = uic.loadUi('../ui/Mountains.ui', self)
        
        # Thiết lập để lấy lại vị trí cũ và sinal
        self.old_pos = None
        self.signal = signal
        
        # Thiết lập xóa bỏ các nút tắt, thu nhỏ, phóng to
        self.setWindowFlag(QtCore.Qt.WindowType.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WidgetAttribute.WA_TranslucentBackground)
        
        self.ui.pushButton_2.clicked.connect(self.main_interface_show)
        self.ui.pushButton_6.clicked.connect(self.mountFuji_show)
        self.ui.pushButton_10.clicked.connect(self.himalaya_show)
        self.ui.pushButton_9.clicked.connect(self.alps_show)
        self.ui.pushButton_12.clicked.connect(self.everest_show)
        self.ui.pushButton_7.clicked.connect(self.close_application)
        self.ui.pushButton_8.clicked.connect(self.menu_show)
    def mountain_open(self):
        self.show()
    def main_interface_show(self):
        self.close()
        self.signal.main_interface.emit(self.pos())
    def mountFuji_show(self):
        self.close()
        self.signal.mountFuji.emit(self.pos())
    def himalaya_show(self):
        self.close()
        self.signal.himalaya.emit(self.pos())
    def alps_show(self):
        self.close()
        self.signal.alps.emit(self.pos())
    def everest_show(self):
        self.close()
        self.signal.everest.emit(self.pos())
    def menu_show(self):
        self.close()
        self.signal.menu.emit(self.pos())
        
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
#    windows = Mountain()
#    windows.show()
#    app.exec()
    