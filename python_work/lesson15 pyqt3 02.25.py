import sys

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QMainWindow, QApplication, QSlider, QLabel


class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.slider = QSlider(Qt.Horizontal, self)
        self.slider.setMaximum(1000)
        self.slider.setMinimum(0)

        self.slider.setGeometry(20,40,100,30)

        self.slider.valueChanged[int].connect(self.changeValue)

        self.label = QLabel('CURRENT: 0', self)
        self.label.setGeometry(30, 100,100,30)

        self.setGeometry(300,300,280,170)
        self.setWindowTitle('Slider Example')

        self.show()

    def changeValue(self, value):
        print('슬라이더 변경 값 출력')
        self.label.setText('CURRENT:{}'.format(value))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWindow()
    sys.exit(app.exec())