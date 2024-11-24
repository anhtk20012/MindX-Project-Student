# Thư viện hỗ trợ cho QTDesigner
import sys, os
from PyQt6 import QtCore
from PyQt6.QtWidgets import QApplication, QWidget
from src import welcome, welcome2, sign_in, sign_up, main_interface
# Hỗ trợ đường dẫn để không bị lỗi
from pathlib import Path
os.chdir(Path(__file__).parent)

class Signal(QWidget):
    welcome = QtCore.pyqtSignal()
    welcome2 = QtCore.pyqtSignal(QtCore.QPoint)
    signin = QtCore.pyqtSignal(QtCore.QPoint)
    signup = QtCore.pyqtSignal(QtCore.QPoint)
    main_interface = QtCore.pyqtSignal(QtCore.QPoint)
    
class Main_App(QWidget):
    def __init__(self):
        # Khởi tạo signal và giao diện con
        self.signal = Signal()
        self.welcome = welcome.Welcome(self.signal)
        self.welcome2 = welcome2.Welcome2(self.signal)
        self.signin = sign_in.Sign_in(self.signal)
        self.signup = sign_up.Sign_up(self.signal)
        self.main_interface = main_interface.Main_interface(self.signal)
        
        # Kiểm tra kết nối khi nhận emit
        self.signal.welcome.connect(self.welcome.welcome_open)
        self.signal.welcome2.connect(self.welcome2.welcome2_open)
        self.signal.signin.connect(self.signin.signin_open)
        self.signal.signup.connect(self.signup.signup_open)
        self.signal.main_interface.connect(self.main_interface.main_interface_open)
    
    def main_show(self):
        self.signal.welcome.emit()
        
# Phần chính giúp mở và hiển thị nội dung đầu tiên    
if __name__ == "__main__":
    app = QApplication(sys.argv)
    windows = Main_App()
    windows.main_show()
    app.exec()