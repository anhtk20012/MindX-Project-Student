import os
from pathlib import Path
from PyQt6 import uic, QtCore
from PyQt6.QtWidgets import QMainWindow, QMessageBox

class Everest (QMainWindow):
    def __init__(self, signal=None):
        super().__init__()
        os.chdir(Path(__file__).parent)
        self.ui = uic.loadUi('../ui/Everest.ui', self)
        
        # Thiết lập để lấy lại vị trí cũ và sinal
        self.old_pos = None
        self.signal = signal
        
        # Thiết lập xóa bỏ các nút tắt, thu nhỏ, phóng to
        self.setWindowFlag(QtCore.Qt.WindowType.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WidgetAttribute.WA_TranslucentBackground)
        
        self.ui.pushButton_2.clicked.connect(self.mountain_show)
        self.ui.pushButton.clicked.connect(self.success_show)
    def everest_open(self):
        self.show()
    def mountain_show(self):
        self.close()
        self.signal.mountain.emit(self.pos())
    def success_show(self):
        self.close()
        self.signal.success.emit(self.pos())
    
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
#    windows = Everest()
#    windows.show()
#    app.exec()
    