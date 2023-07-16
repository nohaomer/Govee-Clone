import os

import PyQt5
from PyQt5 import QtWidgets

class Ui_MainWindow2(object):
    def refresh(self):

        # MainWindow.hide()

        os.system("python t.py")
        print("2")
        # MainWindow.close()
        # os.system("python t.py")


    def setupUi(self, MainWindow):
        s = 1
        for row in open("table.csv"):
            s += 1
            print(s)
        MainWindow.setObjectName("Govee")
        MainWindow.resize(800, 612)
        MainWindow.setStyleSheet("background-image: url(2.png);")
        MainWindow.setWindowIcon(PyQt5.QtGui.QIcon('icon.png'))
        self.centralwidget = PyQt5.QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tableWidget_2 = PyQt5.QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget_2.setGeometry(PyQt5.QtCore.QRect(50, 180, 721, 351))
        self.tableWidget_2.setLayoutDirection(PyQt5.QtCore.Qt.LeftToRight)
        self.tableWidget_2.setAutoFillBackground(False)
        self.tableWidget_2.setStyleSheet("background-image: url(1.JPG);")
        self.tableWidget_2.setEditTriggers(PyQt5.QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tableWidget_2.setTabKeyNavigation(False)
        self.tableWidget_2.setProperty("showDropIndicator", True)
        self.tableWidget_2.setAlternatingRowColors(True)
        self.tableWidget_2.setTextElideMode(PyQt5.QtCore.Qt.ElideRight)
        self.tableWidget_2.setShowGrid(True)
        self.tableWidget_2.setGridStyle(PyQt5.QtCore.Qt.SolidLine)
        self.tableWidget_2.setCornerButtonEnabled(True)
        self.tableWidget_2.setObjectName("tableWidget_2")
        self.tableWidget_2.setColumnCount(8)
        self.tableWidget_2.setRowCount(s)
        rowcount = 1
        # iterating through the whole file
        item = PyQt5.QtWidgets.QTableWidgetItem()
        for row in open("table.csv"):
            self.tableWidget_2.setVerticalHeaderItem(rowcount, item)
            item = PyQt5.QtWidgets.QTableWidgetItem()
            rowcount += 1


        print(rowcount)

        ########################################################################Column style #########################################################
        font = PyQt5.QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        brush = PyQt5.QtGui.QBrush(PyQt5.QtGui.QColor(0, 139, 209)) # To color it
        brush.setStyle(PyQt5.QtCore.Qt.SolidPattern)
        item.setForeground(brush)
        self.tableWidget_2.setHorizontalHeaderItem(0, item)
        item = PyQt5.QtWidgets.QTableWidgetItem()
        font = PyQt5.QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        brush = PyQt5.QtGui.QBrush(PyQt5.QtGui.QColor(0, 138, 207))
        brush.setStyle(PyQt5.QtCore.Qt.SolidPattern)
        item.setForeground(brush)
        self.tableWidget_2.setHorizontalHeaderItem(1, item)
        item = PyQt5.QtWidgets.QTableWidgetItem()
        font = PyQt5.QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        brush = PyQt5.QtGui.QBrush(PyQt5.QtGui.QColor(0, 149, 223))
        brush.setStyle(PyQt5.QtCore.Qt.SolidPattern)
        item.setForeground(brush)
        self.tableWidget_2.setHorizontalHeaderItem(2, item)
        item = PyQt5.QtWidgets.QTableWidgetItem()
        font = PyQt5.QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        brush = PyQt5.QtGui.QBrush(PyQt5.QtGui.QColor(0, 135, 203))
        brush.setStyle(PyQt5.QtCore.Qt.SolidPattern)
        item.setForeground(brush)
        self.tableWidget_2.setHorizontalHeaderItem(3, item)
        item = PyQt5.QtWidgets.QTableWidgetItem()
        font = PyQt5.QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        brush = PyQt5.QtGui.QBrush(PyQt5.QtGui.QColor(0, 135, 203))
        brush.setStyle(PyQt5.QtCore.Qt.SolidPattern)
        item.setForeground(brush)
        self.tableWidget_2.setHorizontalHeaderItem(4, item)
        item = PyQt5.QtWidgets.QTableWidgetItem()
        font = PyQt5.QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        brush = PyQt5.QtGui.QBrush(PyQt5.QtGui.QColor(0, 135, 203))
        brush.setStyle(PyQt5.QtCore.Qt.SolidPattern)
        item.setForeground(brush)
        self.tableWidget_2.setHorizontalHeaderItem(5, item)
        item = PyQt5.QtWidgets.QTableWidgetItem()
        font = PyQt5.QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        brush = PyQt5.QtGui.QBrush(PyQt5.QtGui.QColor(0, 135, 203))
        brush.setStyle(PyQt5.QtCore.Qt.SolidPattern)
        item.setForeground(brush)
        self.tableWidget_2.setHorizontalHeaderItem(6, item)
        item = PyQt5.QtWidgets.QTableWidgetItem()
        font = PyQt5.QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        brush = PyQt5.QtGui.QBrush(PyQt5.QtGui.QColor(0, 135, 203))
        brush.setStyle(PyQt5.QtCore.Qt.SolidPattern)
        item.setForeground(brush)
        self.tableWidget_2.setHorizontalHeaderItem(7, item)
        item = PyQt5.QtWidgets.QTableWidgetItem()
        font = PyQt5.QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        brush = PyQt5.QtGui.QBrush(PyQt5.QtGui.QColor(0, 135, 203))
        brush.setStyle(PyQt5.QtCore.Qt.SolidPattern)
        item.setForeground(brush)
        self.tableWidget_2.setHorizontalHeaderItem(8, item)
        item = PyQt5.QtWidgets.QTableWidgetItem()

        #######################################################################################################################
        row2=0
        for row in open('table.csv'):
            words=row.split(",")
            print(words)
            i=words[3]
            print("i="+i)
            print("sss"+words[3])
            for col in range (0,8):

                if col !=3:
                    item = PyQt5.QtWidgets.QTableWidgetItem()
                    item.setTextAlignment(PyQt5.QtCore.Qt.AlignCenter)
                    self.tableWidget_2.setItem(row2, col, item)
                    print("row2, col, item",row2, col, item)
                else:
                    if i=="on":
                        print(col)
                        item = PyQt5.QtWidgets.QTableWidgetItem()
                        item.setTextAlignment(PyQt5.QtCore.Qt.AlignCenter)
                        icon = PyQt5.QtGui.QIcon()
                        icon.addPixmap(PyQt5.QtGui.QPixmap("green_light.png"), PyQt5.QtGui.QIcon.Normal, PyQt5.QtGui.QIcon.On)
                        item.setIcon(icon)
                        self.tableWidget_2.setItem(row2, col, item)

                    else:
                        item = PyQt5.QtWidgets.QTableWidgetItem()
                        item.setTextAlignment(PyQt5.QtCore.Qt.AlignCenter)
                        icon = PyQt5.QtGui.QIcon()
                        icon.addPixmap(PyQt5.QtGui.QPixmap("red_light.png"), PyQt5.QtGui.QIcon.Normal, PyQt5.QtGui.QIcon.On)
                        item.setIcon(icon)
                        self.tableWidget_2.setItem(row2, col, item)


            row2+=1

        self.tableWidget_2.horizontalHeader().setDefaultSectionSize(180)
        self.tableWidget_2.verticalHeader().setVisible(False)
        ######################################################################## Other widget ########################################################################
        self.label_2 = PyQt5.QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(PyQt5.QtCore.QRect(360, 20, 81, 51))
        self.label_2.setStyleSheet("background-image: url(1.JPG);\n"
            "font: 75 20pt \"MS Shell Dlg 2\";\n""color: rgb(0, 170, 255);\n""")
        self.label_2.setObjectName("label_2")
        self.label_4 = PyQt5.QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(PyQt5.QtCore.QRect(60, 90, 271, 51))
        self.label_4.setStyleSheet("background-image: url(1.JPG);\n"
         "font: 75 20pt \"MS Shell Dlg 2\";\n"
         "color: rgb(0, 170, 255);")
        self.label_4.setObjectName("label_4")
        self.pushButton_2 = PyQt5.QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(PyQt5.QtCore.QRect(290, 540, 201, 61))
        self.pushButton_2.setStyleSheet("background-image: url(:/newPrefix/1.JPG);\n"
                                        "font: 75 22pt \"MS Shell Dlg 2\";\n"
                                        "color: rgb(0, 170, 255);\n"
                                        " border-radius: 25px;\n"
                                        "border: 3px solid #00AAFF;")
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.clicked.connect(self.refresh)
        #######################################################################################################################################################
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        PyQt5.QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = PyQt5.QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Govee"))
        self.tableWidget_2.setSortingEnabled(False)
        rowcount1=1
        for row in open("table.csv"):
            item = self.tableWidget_2.verticalHeaderItem(rowcount1)
            item.setText(_translate("MainWindow", "New Row"))
            rowcount1 += 1

        #######################################################################  Columns  ################################################
        item = self.tableWidget_2.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Name"))
        item = self.tableWidget_2.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Location"))
        item = self.tableWidget_2.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Code"))
        item = self.tableWidget_2.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Status"))
        #############################################################
        item = self.tableWidget_2.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "T Low"))
        item = self.tableWidget_2.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "T Upp"))
        item = self.tableWidget_2.horizontalHeaderItem(6)
        item.setText(_translate("MainWindow", "RH Low"))
        item = self.tableWidget_2.horizontalHeaderItem(7)
        item.setText(_translate("MainWindow", "RH upp"))
        #######################################################################################################################################
        __sortingEnabled = self.tableWidget_2.isSortingEnabled()
        self.tableWidget_2.setSortingEnabled(False)
        rowc=0
        for row in open("table.csv"):
            words = row.split(',')

            for col in range(0,8):
                item = self.tableWidget_2.item(rowc, col)
                item.setText(_translate("MainWindow", words[col]))
                print(rowc,col)
                print(words[col]+"jjjjjjjj")



            print(words[0])
            rowc=rowc+1

        self.tableWidget_2.setSortingEnabled(__sortingEnabled)
        self.label_2.setText(_translate("MainWindow", "Govee"))
        self.label_4.setText(_translate("MainWindow", "Device Information:"))

        self.pushButton_2.setText(_translate("MainWindow", "Refresh"))


if __name__ == "__main__":
    import sys
    app = PyQt5.QtWidgets.QApplication(sys.argv)
    MainWindow = PyQt5.QtWidgets.QMainWindow()
    ui = Ui_MainWindow2()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
