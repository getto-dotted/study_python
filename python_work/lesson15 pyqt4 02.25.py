import sys
from PyQt5 import *
from PyQt5.QtWidgets import *


class LayoutExample(QMainWindow):
    def __init__(self):
        super().__init__()

        lbl1 = QLabel('My country name is', self)
        lbl2 = QLabel('Korea', self)

        lbl1.move(20, 50)
        lbl2.move(120, 70)


        self.setGeometry(100,100,300,200)
        self.setWindowTitle('Layout Exam')
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = LayoutExample()
    sys.exit(app.exec())
