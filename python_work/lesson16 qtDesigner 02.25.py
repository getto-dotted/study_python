# pip install pyqt5-tools
# C:\Users\All Users\Anaconda3\Lib\site-packages\pyqt5_tools\Qt\bin를 환경변수에 입력
# cmd에서 designer 실행
# qt디자이너에서 ui를 만들어서 저장
# pyuic5 -x lesson16.ui -o lesson16.py


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
        MainWindow.resize(637, 348)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.id = QtWidgets.QLabel(self.centralwidget)
        self.id.setGeometry(QtCore.QRect(40, 30, 64, 15))
        self.id.setObjectName("id")
        self.name = QtWidgets.QLabel(self.centralwidget)
        self.name.setGeometry(QtCore.QRect(40, 80, 64, 15))
        self.name.setObjectName("name")
        self.phone = QtWidgets.QLabel(self.centralwidget)
        self.phone.setGeometry(QtCore.QRect(40, 140, 64, 15))
        self.phone.setObjectName("phone")
        self.address = QtWidgets.QLabel(self.centralwidget)
        self.address.setGeometry(QtCore.QRect(40, 200, 64, 15))
        self.address.setObjectName("address")
        self.id_input = QtWidgets.QLineEdit(self.centralwidget)
        self.id_input.setGeometry(QtCore.QRect(110, 30, 113, 21))
        self.id_input.setObjectName("id_input")
        self.name_input = QtWidgets.QLineEdit(self.centralwidget)
        self.name_input.setGeometry(QtCore.QRect(110, 80, 113, 21))
        self.name_input.setObjectName("name_input")
        self.phone_input = QtWidgets.QLineEdit(self.centralwidget)
        self.phone_input.setGeometry(QtCore.QRect(110, 140, 113, 21))
        self.phone_input.setObjectName("phone_input")
        self.address_input = QtWidgets.QLineEdit(self.centralwidget)
        self.address_input.setGeometry(QtCore.QRect(110, 200, 113, 21))
        self.address_input.setObjectName("address_input")
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(270, 30, 311, 191))
        self.textEdit.setObjectName("textEdit")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(170, 270, 93, 28))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.btnHandler)


        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 637, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
    # end of setupUi()
    def btnHandler(self):
        name = self.name_input.text()
        id = self.id_input.text()
        phone = self.phone_input.text()
        address = self.address_input.text()
        tup = (id, name, phone, address)
        #self.textEdit.append(id + name + phone + address)
        self.textEdit.append('%s %s %s %s' %(tup))

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.id.setText(_translate("MainWindow", "아이디"))
        self.name.setText(_translate("MainWindow", "성명"))
        self.phone.setText(_translate("MainWindow", "연락처"))
        self.address.setText(_translate("MainWindow", "주소"))
        self.pushButton.setText(_translate("MainWindow", "확인"))




if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
