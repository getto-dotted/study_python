import sys
from PyQt5 import *
from PyQt5.QtWidgets import *

class GridLayoutEx(QMainWindow):
    def __init__(self):
        super().__init__()

        #라벨 생성
        title = QLabel('Title')
        writer = QLabel('Writer')
        comment = QLabel('Comment')

        titleEdit = QLineEdit()
        writerEdit = QLineEdit()
        commentEdit = QTextEdit()

        confirm = QPushButton('Confirm')

        #레이아웃
        grid = QGridLayout()
        grid.setSpacing(10) # 간격

        grid.addWidget(title, 1, 0)
        grid.addWidget(titleEdit, 1,1)
        grid.addWidget(writer, 2,0)
        grid.addWidget(writerEdit,2,1)

        grid.addWidget(comment, 3,0)
        grid.addWidget(commentEdit, 3,1,4,1)
        grid.addWidget(confirm,7,1)

        # 레이아웃 붙이기
        win = QWidget()
        win.setLayout(grid)
        self.setCentralWidget(win)

        self.setGeometry(300,300,550,600)
        self.setWindowTitle('그리드레이아웃')
        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = GridLayoutEx()
    sys.exit(app.exec())