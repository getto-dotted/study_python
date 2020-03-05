import sys
from PyQt5 import *
from PyQt5.QtWidgets import *

class LayoutEx2(QMainWindow):
    def __init__(self):
        super().__init__()

        #위젯 생성 버튼/레이블 등

        lbl1 = QLabel('My country name is')
        lbl2 = QLabel('Korea')

        okButton = QPushButton('OK')
        cancleButton = QPushButton('Cancle')

        # 레이아웃 생성
        hbox = QHBoxLayout()
        #hbox.addStretch(1)
        hbox.addWidget(okButton)
        hbox.addWidget(cancleButton)

        vbox = QVBoxLayout()
        vbox.addWidget(lbl1)
        vbox.addWidget(lbl2)
        vbox.addLayout(hbox)

        win = QWidget()
        win.setLayout(vbox)
        self.setCentralWidget(win)

        self.setGeometry(100,100,300,150)
        self.setWindowTitle('레이아웃 연습2')
        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = LayoutEx2()
    sys.exit(app.exec())