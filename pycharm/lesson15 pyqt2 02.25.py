# pyinstaller -F 파일명.py

import sys

from PyQt5.QtWidgets import QMainWindow, QPushButton, QMessageBox, QApplication


class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        button = QPushButton('BTN', self)
        button.move(10,10)
        button.clicked.connect(self.message) #이벤트 핸들러 연결
        self.show()

    # 이벤트 핸들러 함수
    def message(self):
        #print('message 함수 호출 됨')
        msg = QMessageBox(self)
        msg.setText('Ok! 4딸라!')
        msg.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWindow()
    sys.exit(app.exec())
