# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'lesson16.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!
import random

from PyQt5 import QtCore, QtGui, QtWidgets

curr_money = 0
betting = 0
list = [1,2,3,4,5,6,7,8,9,0]
cheating_num = 0
game_round = 0

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

        self.btn1000.clicked.connect(self.input_money1)
        self.btn5000.clicked.connect(self.input_money5)
        self.btn10000.clicked.connect(self.input_money10)
        self.btn1000_b.clicked.connect(self.betting1)
        self.btn5000_b.clicked.connect(self.betting5)
        self.btn10000_b.clicked.connect(self.betting10)
        self.start.clicked.connect(self.game)



    def input_money1(self):
        global curr_money
        global cheating_num
        cheating_num = random.randint(1,10)
        curr_money += 1000
        self.textEdit.clear()
        self.textEdit.append(str(curr_money))
    def input_money5(self):
        global curr_money
        global cheating_num
        cheating_num = random.randint(3, 7)
        curr_money += 5000
        self.textEdit.clear()
        self.textEdit.append(str(curr_money))
    def input_money10(self):
        global curr_money
        global cheating_num
        cheating_num = random.randint(2, 30)
        curr_money += 10000
        self.textEdit.clear()
        self.textEdit.append(str(curr_money))

    def betting1(self):
        global betting
        global curr_money
        betting = 1000
        self.display.clear()

        if curr_money >= betting:
            self.display.append('배팅액 :'+str(betting)+'원')
        else:
            self.display.append('잔액부족')

    def betting5(self):
        global betting
        global curr_money
        betting = 5000
        self.display.clear()

        if curr_money >= betting:
            self.display.append('배팅액 :' + str(betting) + '원')
        else:
            self.display.append('잔액부족')

    def betting10(self):
        global betting
        global curr_money
        betting = 10000
        self.display.clear()

        if curr_money >= betting:
            self.display.append('배팅액 :' + str(betting) + '원')
        else:
            self.display.append('잔액부족')

    def game(self):
        global betting
        global curr_money
        global list
        global cheating_num

        if curr_money - betting <0:
            self.display.clear()
            self.display.append('잔액부족')

        else:
            global game_round
            game_round += 1

            rnum1 = random.choice(list)
            rnum2 = random.choice(list)
            rnum3 = random.choice(list)

            if game_round == cheating_num:
                rnum1 = rnum2 = rnum3 = random.choice(list)
                self.numbox1.clear()
                self.numbox1.append(str(rnum1))
                self.numbox2.clear()
                self.numbox2.append(str(rnum2))
                self.numbox3.clear()
                self.numbox3.append(str(rnum3))
                game_round = 0

                if rnum1 == 7:
                    self.display.clear()
                    self.display.append('대박!! 당첨금{} 원!!'.format(str(curr_money+betting*10)))
                    curr_money = curr_money+betting*10
                    self.textEdit.clear()
                    self.textEdit.append(str(curr_money))
                elif rnum1 ==0:
                    self.display.clear()
                    self.display.append('본전치기! {} 원'.format(str(curr_money)))
                    self.textEdit.clear()
                    self.textEdit.append(str(curr_money))
                else:
                    self.display.clear()
                    self.display.append('중박! {} 원'.format(str(curr_money+betting*2)))
                    curr_money = curr_money+betting*2
                    self.textEdit.clear()
                    self.textEdit.append(str(curr_money))


            else:
                self.numbox1.clear()
                self.numbox1.append(str(rnum1))
                self.numbox2.clear()
                self.numbox2.append(str(rnum2))
                self.numbox3.clear()
                self.numbox3.append(str(rnum3))

                if rnum1 == rnum2 == rnum3 ==7:
                    self.display.clear()
                    self.display.append('대박!! 당첨금{} 원!!'.format(str(curr_money+betting*10)))
                    curr_money = curr_money+betting*10
                    self.textEdit.clear()
                    self.textEdit.append(str(curr_money))
                elif rnum1 == rnum2 == rnum3 ==0:
                    self.display.clear()
                    self.display.append('본전치기! {} 원'.format(str(curr_money)))
                    self.textEdit.clear()
                    self.textEdit.append(str(curr_money))
                elif rnum1 == rnum2 == rnum3 and not 7 or 0:
                    self.display.clear()
                    self.display.append('중박! {} 원'.format(str(curr_money+betting*2)))
                    curr_money = curr_money+betting*2
                    self.textEdit.clear()
                    self.textEdit.append(str(curr_money))
                else:
                    self.display.clear()
                    self.display.append('패배.. {} 원'.format(str(curr_money - betting)))
                    curr_money = curr_money - betting
                    self.textEdit.clear()
                    self.textEdit.append(str(curr_money))


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



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
