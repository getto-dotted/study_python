import sys
from PyQt5 import *
from PyQt5.QtCore import pyqtSignal
from PyQt5.QtWidgets import *

class SignaEx(QMainWindow):
    #데이터가 없는 시그널 하나 생성
    closeApp = pyqtSignal()# 화면에서 일어나는 일을 프로그램에 알려주는 역할을 한다./ 사용자정의 이벤트 객체
    # 시그널이 작동하는 시점은 emit()이 호출되는 시점

    def __init__(self):
        super().__init__()
        self.closeApp.connect(self.mouseHandle)

        self.setGeometry(300,300,290,150)
        self.setWindowTitle('emit 시그널')
        self.show()

    def mousePressEvent(self, event):
        self.closeApp.emit()
    # def mouseDoubleClickEvent(self, event):
    #     self.closeApp.emit()
    # def mouseMoveEvent(self, event):
    #     self.closeApp.emit()
    def mouseHandle(self):
        print('마우스 이벤트 발생')
        #self.closeApp.emit()
        



if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = SignaEx()
    sys.exit(app.exec())