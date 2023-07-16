
from two import Ui_second_window
from PyQt5 import QtCore, QtGui, QtWidgets

import threading

class mythread(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
    def run(self):
        from running import no
        x=no(0,0)
        x.yarb4()


class Ui_MainWindow(object):
    thread1 = mythread();

    thread1.start()


    def clickme(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_second_window()
        self.ui.setupUi(self.window)
        user = self.lineEdit.text()
        pass1 = self.lineEdit_2.text()
        if (user == "noha" and pass1 == "12345"):
            self.window.show()
            MainWindow.hide()

        else:
            self.label_5.setText("Enter Correct Data .")



    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1212, 678)
        MainWindow.setStyleSheet("background-image: url(2.png);")
        MainWindow.setWindowIcon(QtGui.QIcon('icon.png'))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(520, 240, 161, 31))
        self.label_3.setStyleSheet("background-image: url(1.JPG);\n"
                                   "color: rgb(0, 170, 255);\n"
                                   "font: 75 14pt \"MS Shell Dlg 2\";")
        self.label_3.setObjectName("label_3")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(850, 130, 361, 401))
        self.label.setStyleSheet("background-image: url(gove.jpg);")
        self.label.setText("")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(860, 10, 231, 51))
        self.label_2.setStyleSheet("background-image: url(1.JPG);\n"
                                   "font: 75 20pt \"MS Shell Dlg 2\";\n"
                                   "color: rgb(0, 170, 255);")
        self.label_2.setObjectName("label_2")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(670, 250, 181, 22))
        self.lineEdit.setStyleSheet("background-image: url(1.JPG);")
        self.lineEdit.setObjectName("lineEdit")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(520, 340, 151, 31))
        self.label_4.setStyleSheet("background-image: url(1.JPG);\n"
                                   "color: rgb(0, 170, 255);\n"
                                   "font: 75 14pt \"MS Shell Dlg 2\";")
        self.label_4.setObjectName("label_4")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(610, 540, 201, 61))
        self.pushButton.setStyleSheet("background-image: url(1.JPG);\n"
                                      "font: 75 22pt \"MS Shell Dlg 2\";\n"
                                      "color: rgb(0, 170, 255);\n"
                                      " border-radius: 25px;\n"
                                      "border: 3px solid #00AAFF;")
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.clickme)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(670, 350, 181, 22))
        self.lineEdit_2.setStyleSheet("background-image: url(1.JPG);")
        self.lineEdit_2.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(494, 440, 391, 51))
        self.label_5.setStyleSheet("background-image: url(1.JPG);\n"
                                   "font: 75 14pt \"MS Shell Dlg 2\";")
        self.label_5.setText("")
        self.label_5.setObjectName("label_5")

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Login page"))
        self.label_3.setText(_translate("MainWindow", "User name :"))
        self.label_2.setText(_translate("MainWindow", "Govee "))
        self.label_4.setText(_translate("MainWindow", "Password:"))
        self.pushButton.setText(_translate("MainWindow", "Login"))

if __name__ == "__main__":
    import sys


    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()

    sys.exit(app.exec_())
