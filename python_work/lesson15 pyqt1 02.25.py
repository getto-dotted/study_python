#파이참 설정에서 인스톨
#pip install pyqt5
#PyQt5Designer
#PyInstaller
import sys

from PyQt5.QtWidgets import QMainWindow, QApplication


class HelloWindow(QMainWindow): # 객체지향이므로 상속이 필요하다
    def __init__(self):
        super().__init__()

        self.setGeometry(200,300,600,400) # 창의 위치 크기
        self.setWindowTitle('창 이름 설정')
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = HelloWindow()
    sys.exit(app.exec())