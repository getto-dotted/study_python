# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'lesson16.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1480, 673)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(460, 0, 481, 351))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap(":/pic/sea.webp"))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(200, 40, 261, 271))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(940, 40, 261, 271))
        self.label_3.setObjectName("label_3")
        self.numbox1 = QtWidgets.QTextEdit(self.centralwidget)
        self.numbox1.setGeometry(QtCore.QRect(510, 350, 104, 87))
        self.numbox1.setObjectName("numbox1")
        self.numbox2 = QtWidgets.QTextEdit(self.centralwidget)
        self.numbox2.setGeometry(QtCore.QRect(660, 350, 104, 87))
        self.numbox2.setObjectName("numbox2")
        self.numbox3 = QtWidgets.QTextEdit(self.centralwidget)
        self.numbox3.setGeometry(QtCore.QRect(810, 350, 104, 87))
        self.numbox3.setObjectName("numbox3")
        self.display = QtWidgets.QTextEdit(self.centralwidget)
        self.display.setGeometry(QtCore.QRect(510, 450, 401, 61))
        self.display.setObjectName("display")
        self.btn1000 = QtWidgets.QPushButton(self.centralwidget)
        self.btn1000.setGeometry(QtCore.QRect(1100, 270, 61, 61))
        self.btn1000.setObjectName("btn1000")
        self.btn5000 = QtWidgets.QPushButton(self.centralwidget)
        self.btn5000.setGeometry(QtCore.QRect(1190, 270, 61, 61))
        self.btn5000.setObjectName("btn5000")
        self.btn10000 = QtWidgets.QPushButton(self.centralwidget)
        self.btn10000.setGeometry(QtCore.QRect(1290, 270, 61, 61))
        self.btn10000.setObjectName("btn10000")
        self.btn5000_b = QtWidgets.QPushButton(self.centralwidget)
        self.btn5000_b.setGeometry(QtCore.QRect(1190, 410, 61, 61))
        self.btn5000_b.setObjectName("btn5000_b")
        self.btn10000_b = QtWidgets.QPushButton(self.centralwidget)
        self.btn10000_b.setGeometry(QtCore.QRect(1290, 410, 61, 61))
        self.btn10000_b.setObjectName("btn10000_b")
        self.btn1000_b = QtWidgets.QPushButton(self.centralwidget)
        self.btn1000_b.setGeometry(QtCore.QRect(1100, 410, 61, 61))
        self.btn1000_b.setObjectName("btn1000_b")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(1190, 350, 61, 31))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(1150, 490, 181, 91))
        self.label_5.setObjectName("label_5")
        self.start = QtWidgets.QPushButton(self.centralwidget)
        self.start.setGeometry(QtCore.QRect(600, 520, 221, 91))
        self.start.setText("")
        self.start.setObjectName("start")
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(40, 340, 291, 61))
        self.textEdit.setObjectName("textEdit")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(40, 290, 151, 41))
        self.label_6.setObjectName("label_6")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1480, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_2.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:36pt;\">바 다</span></p></body></html>"))
        self.label_3.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:36pt;\">이 야 기</span></p></body></html>"))
        self.btn1000.setText(_translate("MainWindow", "1000원"))
        self.btn5000.setText(_translate("MainWindow", "5000원"))
        self.btn10000.setText(_translate("MainWindow", "10000원"))
        self.btn5000_b.setText(_translate("MainWindow", "5000원"))
        self.btn10000_b.setText(_translate("MainWindow", "10000원"))
        self.btn1000_b.setText(_translate("MainWindow", "1000원"))
        self.label_4.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:18pt;\">충전하기</span></p></body></html>"))
        self.label_5.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:48pt;\">베팅</span></p></body></html>"))
        self.label_6.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:16pt;\">남은 충전금</span></p></body></html>"))
import resource_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
