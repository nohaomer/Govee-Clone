import os
import shutil
import threading
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox, QWidget
import time
from table import Ui_MainWindow
from t import Ui_MainWindow2
class mythread1(threading.Thread):
    def __init__(self,m,n):
        self.m=m
        self.n=n

        threading.Thread.__init__(self)
    def run(self):
        from running import no
        print(self.n,self.m)
        x=no(self.m,self.n)
        x.yarb5()
        print("device 1")

class mythread2(threading.Thread):
    def __init__(self,m,n):
        threading.Thread.__init__(self)
        self.m = m
        self.n = n
    def run(self):
        from running import no
        x = no(self.m,self.n)
        x.yarb5()

class mythread3(threading.Thread):
    def __init__(self,m,n):
        threading.Thread.__init__(self)
        self.m = m
        self.n = n
    def run(self):
        from running import no
        x = no(self.m,self.n)
        x.yarb5()
class mythread4(threading.Thread):
    def __init__(self,m,n):
        threading.Thread.__init__(self)
        self.m = m
        self.n = n
    def run(self):
        from running import no
        x = no(self.m,self.n)
        x.yarb5()

class mythread5(threading.Thread):
    def __init__(self,m,n):
        threading.Thread.__init__(self)
        self.m = m
        self.n = n
    def run(self):
        # from run import fig2
        from running import no
        x = no(self.m,self.n)
        x.yarb5()


class mythread6(threading.Thread):
    def __init__(self,m,n):
        threading.Thread.__init__(self)
        self.m = m
        self.n = n
    def run(self):
        from running import no
        x = no(self.m,self.n)
        x.yarb5()

class mythread7(threading.Thread):
    def __init__(self,m,n):
        threading.Thread.__init__(self)
        self.m = m
        self.n = n
    def run(self):
        from running import no
        x = no(self.m,self.n)
        x.yarb5()


class mythread8(threading.Thread):
    def __init__(self,m,n):
        threading.Thread.__init__(self)
        self.m = m
        self.n = n
    def run(self):
        from running import no
        x = no(self.m,self.n)
        x.yarb5()

class mythread9(threading.Thread):
    def __init__(self,m,n):
        threading.Thread.__init__(self)
        self.m = m
        self.n = n
    def run(self):
        from running import no
        x = no(self.m,self.n)
        x.yarb5()

class mythread10(threading.Thread):
    def __init__(self,m,n):
        threading.Thread.__init__(self)
        self.m = m
        self.n = n
    def run(self):
        from running import no
        x = no(self.m,self.n)
        x.yarb5()

class mythread11(threading.Thread):
    def __init__(self,m,n):
        threading.Thread.__init__(self)
        self.m = m
        self.n = n
    def run(self):
        from running import no
        x = no(self.m,self.n)
        x.yarb5()

class mythread12(threading.Thread):
    def __init__(self,m,n):
        threading.Thread.__init__(self)
        self.m = m
        self.n = n
    def run(self):
        from running import no
        x = no(self.m,self.n)
        x.yarb5()

class mythread13(threading.Thread):
    def __init__(self,m,n):
        threading.Thread.__init__(self)
        self.m = m
        self.n = n
    def run(self):
        from running import no
        x = no(self.m,self.n)
        x.yarb5()
class mythread13(threading.Thread):
    def __init__(self,m,n):
        threading.Thread.__init__(self)
        self.m = m
        self.n = n
    def run(self):
        from running import no
        x = no(self.m,self.n)
        x.yarb5()
class mythread14(threading.Thread):
    def __init__(self,m,n):
        threading.Thread.__init__(self)
        self.m = m
        self.n = n
    def run(self):
        from running import no
        x = no(self.m,self.n)
        x.yarb5()

class mythread15(threading.Thread):
    def __init__(self,m,n):
        threading.Thread.__init__(self)
        self.m = m
        self.n = n
    def run(self):
        from running import no
        x = no(self.m,self.n)
        x.yarb5()
class mythread16(threading.Thread):
    def __init__(self,m,n):
        threading.Thread.__init__(self)
        self.m = m
        self.n = n
    def run(self):
        from running import no
        x = no(self.m,self.n)
        x.yarb5()
class mythread20(threading.Thread):
    def __init__(self,m,n):
        threading.Thread.__init__(self)
        self.m = m
        self.n = n
    def run(self):
        from running import no
        x = no(self.m,self.n)
        x.yarb5()

class mythread21(threading.Thread):
    def __init__(self,m,n):
        threading.Thread.__init__(self)
        self.m = m
        self.n = n
    def run(self):
        from running import no
        x = no(self.m,self.n)
        x.yarb5()

class mythread22(threading.Thread):
    def __init__(self,m,n):
        threading.Thread.__init__(self)
        self.m = m
        self.n = n
    def run(self):
        from running import no
        x = no(self.m,self.n)
        x.yarb5()

class mythread23(threading.Thread):
    def __init__(self,m,n):
        threading.Thread.__init__(self)
        self.m = m
        self.n = n
    def run(self):
        from running import no
        x = no(self.m,self.n)
        x.yarb5()

class mythread24(threading.Thread):
    def __init__(self,m,n):
        threading.Thread.__init__(self)
        self.m = m
        self.n = n
    def run(self):
        from running import no
        x = no(self.m,self.n)
        x.yarb5()

class mythread25(threading.Thread):
    def __init__(self,m,n):
        threading.Thread.__init__(self)
        self.m = m
        self.n = n
    def run(self):
        from running import no
        x = no(self.m,self.n)
        x.yarb5()

class mythread26(threading.Thread):
    def __init__(self,m,n):
        threading.Thread.__init__(self)
        self.m = m
        self.n = n
    def run(self):
        from running import no
        x = no(self.m,self.n)
        x.yarb5()

class mythread27(threading.Thread):
    def __init__(self,m,n):
        threading.Thread.__init__(self)
        self.m = m
        self.n = n
    def run(self):
        from running import no
        x = no(self.m,self.n)
        x.yarb5()

class mythread28(threading.Thread):
    def __init__(self,m,n):
        threading.Thread.__init__(self)
        self.m = m
        self.n = n
    def run(self):
        from running import no
        x = no(self.m,self.n)
        x.yarb5()

class mythread29(threading.Thread):
    def __init__(self,m,n):
        threading.Thread.__init__(self)
        self.m = m
        self.n = n
    def run(self):
        from running import no
        x = no(self.m,self.n)
        x.yarb5()

class mythread30(threading.Thread):
    def __init__(self,m,n):
        threading.Thread.__init__(self)
        self.m = m
        self.n = n
    def run(self):
        from running import no
        x = no(self.m,self.n)
        x.yarb5()

class mythread31(threading.Thread):
    def __init__(self,m,n):
        threading.Thread.__init__(self)
        self.m = m
        self.n = n
    def run(self):
        from running import no
        x = no(self.m,self.n)
        x.yarb5()

class mythread32(threading.Thread):
    def __init__(self,m,n):
        threading.Thread.__init__(self)
        self.m = m
        self.n = n
    def run(self):
        from running import no
        x = no(self.m,self.n)
        x.yarb5()

class mythread33(threading.Thread):
    def __init__(self,m,n):
        threading.Thread.__init__(self)
        self.m = m
        self.n = n
    def run(self):
        from running import no
        x = no(self.m,self.n)
        x.yarb5()

class mythread34(threading.Thread):
    def __init__(self,m,n):
        threading.Thread.__init__(self)
        self.m = m
        self.n = n
    def run(self):
        from running import no
        x = no(self.m,self.n)
        x.yarb5()

class mythread35(threading.Thread):
    def __init__(self,m,n):
        threading.Thread.__init__(self)
        self.m = m
        self.n = n
    def run(self):
        from running import no
        x = no(self.m,self.n)
        x.yarb5()


class mythread36(threading.Thread):
    def __init__(self,m,n):
        threading.Thread.__init__(self)
        self.m = m
        self.n = n
    def run(self):
        from running import no
        x = no(self.m,self.n)
        x.yarb5()

class mythread37(threading.Thread):
    def __init__(self,m,n):
        threading.Thread.__init__(self)
        self.m = m
        self.n = n
    def run(self):
        from running import no
        x = no(self.m,self.n)
        x.yarb5()

class mythread38(threading.Thread):
    def __init__(self,m,n):
        threading.Thread.__init__(self)
        self.m = m
        self.n = n
    def run(self):
        from running import no
        x = no(self.m,self.n)
        x.yarb5()

class mythread39(threading.Thread):
    def __init__(self,m,n):
        threading.Thread.__init__(self)
        self.m = m
        self.n = n
    def run(self):
        from running import no
        x = no(self.m,self.n)
        x.yarb5()

class mythread40(threading.Thread):
    def __init__(self,m,n):
        threading.Thread.__init__(self)
        self.m = m
        self.n = n
    def run(self):
        from running import no
        x = no(self.m,self.n)
        x.yarb5()
class mythread41(threading.Thread):
    def __init__(self,m,n):
        threading.Thread.__init__(self)
        self.m = m
        self.n = n
    def run(self):
        from running import no
        x = no(self.m,self.n)
        x.yarb5()
class mythread42(threading.Thread):
    def __init__(self,m,n):
        threading.Thread.__init__(self)
        self.m = m
        self.n = n
    def run(self):
        from running import no
        x = no(self.m,self.n)
        x.yarb5()
class mythread43(threading.Thread):
    def __init__(self,m,n):
        threading.Thread.__init__(self)
        self.m = m
        self.n = n
    def run(self):
        from running import no
        x = no(self.m,self.n)
        x.yarb5()

class mythread44(threading.Thread):
    def __init__(self,m,n):
        threading.Thread.__init__(self)
        self.m = m
        self.n = n
    def run(self):
        from running import no
        x = no(self.m,self.n)
        x.yarb5()

class mythread45(threading.Thread):
    def __init__(self,m,n):
        threading.Thread.__init__(self)
        self.m = m
        self.n = n
    def run(self):
        from running import no
        x = no(self.m,self.n)
        x.yarb5()

class mythread46(threading.Thread):
    def __init__(self,m,n):
        threading.Thread.__init__(self)
        self.m = m
        self.n = n
    def run(self):
        from running import no
        x = no(self.m,self.n)
        x.yarb5()

class mythread47(threading.Thread):
    def __init__(self,m,n):
        threading.Thread.__init__(self)
        self.m = m
        self.n = n
    def run(self):
        from running import no
        x = no(self.m,self.n)
        x.yarb5()

class mythread48(threading.Thread):
    def __init__(self,m,n):
        threading.Thread.__init__(self)
        self.m = m
        self.n = n
    def run(self):
        from running import no
        x = no(self.m,self.n)
        x.yarb5()

class mythread49(threading.Thread):
    def __init__(self,m,n):
        threading.Thread.__init__(self)
        self.m = m
        self.n = n
    def run(self):
        from running import no
        x = no(self.m,self.n)
        x.yarb5()

class mythread50(threading.Thread):
    def __init__(self,m,n):
        threading.Thread.__init__(self)
        self.m = m
        self.n = n
    def run(self):
        from running import no
        x = no(self.m,self.n)
        x.yarb5()

class mythread51(threading.Thread):
    def __init__(self,m,n):
        threading.Thread.__init__(self)
        self.m = m
        self.n = n
    def run(self):
        from running import no
        x = no(self.m,self.n)
        x.yarb5()

class mythread52(threading.Thread):
    def __init__(self,m,n):
        threading.Thread.__init__(self)
        self.m = m
        self.n = n
    def run(self):
        from running import no
        x = no(self.m,self.n)
        x.yarb5()

class mythread53(threading.Thread):
    def __init__(self,m,n):
        threading.Thread.__init__(self)
        self.m = m
        self.n = n
    def run(self):
        from running import no
        x = no(self.m,self.n)
        x.yarb5()

class mythread54(threading.Thread):
    def __init__(self,m,n):
        threading.Thread.__init__(self)
        self.m = m
        self.n = n
    def run(self):
        from running import no
        x = no(self.m,self.n)
        x.yarb5()
class mythread55(threading.Thread):
    def __init__(self,m,n):
        threading.Thread.__init__(self)
        self.m = m
        self.n = n
    def run(self):
        from running import no
        x = no(self.m,self.n)
        x.yarb5()
class mythread56(threading.Thread):
    def __init__(self,m,n):
        threading.Thread.__init__(self)
        self.m = m
        self.n = n
    def run(self):
        from running import no
        x = no(self.m,self.n)
        x.yarb5()
class mythread57(threading.Thread):
    def __init__(self,m,n):
        threading.Thread.__init__(self)
        self.m = m
        self.n = n
    def run(self):
        from running import no
        x = no(self.m,self.n)
        x.yarb5()

class mythread58(threading.Thread):
    def __init__(self,m,n):
        threading.Thread.__init__(self)
        self.m = m
        self.n = n
    def run(self):
        from running import no
        x = no(self.m,self.n)
        x.yarb5()

class mythread59(threading.Thread):
    def __init__(self,m,n):
        threading.Thread.__init__(self)
        self.m = m
        self.n = n
    def run(self):
        from running import no
        x = no(self.m,self.n)
        x.yarb5()

class mythread60(threading.Thread):
    def __init__(self,m,n):
        threading.Thread.__init__(self)
        self.m = m
        self.n = n
    def run(self):
        from running import no
        x = no(self.m,self.n)
        x.yarb5()

class mythread61(threading.Thread):
    def __init__(self,m,n):
        threading.Thread.__init__(self)
        self.m = m
        self.n = n
    def run(self):
        from running import no
        x = no(self.m,self.n)
        x.yarb5()

class mythread62(threading.Thread):
    def __init__(self,m,n):
        threading.Thread.__init__(self)
        self.m = m
        self.n = n
    def run(self):
        from running import no
        x = no(self.m,self.n)
        x.yarb5()

class mythread63(threading.Thread):
    def __init__(self,m,n):
        threading.Thread.__init__(self)
        self.m = m
        self.n = n
    def run(self):
        from running import no
        x = no(self.m,self.n)
        x.yarb5()

class mythread64(threading.Thread):
    def __init__(self,m,n):
        threading.Thread.__init__(self)
        self.m = m
        self.n = n
    def run(self):
        from running import no
        x = no(self.m,self.n)
        x.yarb5()

class mythread65(threading.Thread):
    def __init__(self,m,n):
        threading.Thread.__init__(self)
        self.m = m
        self.n = n
    def run(self):
        from running import no
        x = no(self.m,self.n)
        x.yarb5()


class mythread66(threading.Thread):
    def __init__(self,m,n):
        threading.Thread.__init__(self)
        self.m = m
        self.n = n
    def run(self):
        from running import no
        x = no(self.m,self.n)
        x.yarb5()

class mythread67(threading.Thread):
    def __init__(self,m,n):
        threading.Thread.__init__(self)
        self.m = m
        self.n = n
    def run(self):
        from running import no
        x = no(self.m,self.n)
        x.yarb5()

class mythread68(threading.Thread):
    def __init__(self,m,n):
        threading.Thread.__init__(self)
        self.m = m
        self.n = n
    def run(self):
        from running import no
        x = no(self.m,self.n)
        x.yarb5()

class mythread69(threading.Thread):
    def __init__(self,m,n):
        threading.Thread.__init__(self)
        self.m = m
        self.n = n
    def run(self):
        from running import no
        x = no(self.m,self.n)
        x.yarb5()
class mythread70(threading.Thread):
    def __init__(self,m,n):
        threading.Thread.__init__(self)
        self.m = m
        self.n = n
    def run(self):
        from running import no
        x = no(self.m,self.n)
        x.yarb5()
class mythread71(threading.Thread):
    def __init__(self,m,n):
        threading.Thread.__init__(self)
        self.m = m
        self.n = n
    def run(self):
        from running import no
        x = no(self.m,self.n)
        x.yarb5()
class mythread72(threading.Thread):
    def __init__(self,m,n):
        threading.Thread.__init__(self)
        self.m = m
        self.n = n
    def run(self):
        from running import no
        x = no(self.m,self.n)
        x.yarb5()
class mythread73(threading.Thread):
    def __init__(self,m,n):
        threading.Thread.__init__(self)
        self.m = m
        self.n = n
    def run(self):
        from running import no
        x = no(self.m,self.n)
        x.yarb5()
class mythread74(threading.Thread):
    def __init__(self,m,n):
        threading.Thread.__init__(self)
        self.m = m
        self.n = n
    def run(self):
        from running import no
        x = no(self.m,self.n)
        x.yarb5()
class mythread75(threading.Thread):
    def __init__(self,m,n):
        threading.Thread.__init__(self)
        self.m = m
        self.n = n
    def run(self):
        from running import no
        x = no(self.m,self.n)
        x.yarb5()
class mythread76(threading.Thread):
    def __init__(self,m,n):
        threading.Thread.__init__(self)
        self.m = m
        self.n = n
    def run(self):
        from running import no
        x = no(self.m,self.n)
        x.yarb5()
class mythread77(threading.Thread):
    def __init__(self,m,n):
        threading.Thread.__init__(self)
        self.m = m
        self.n = n
    def run(self):
        from running import no
        x = no(self.m,self.n)
        x.yarb5()
class mythread78(threading.Thread):
    def __init__(self,m,n):
        threading.Thread.__init__(self)
        self.m = m
        self.n = n
    def run(self):
        from running import no
        x = no(self.m,self.n)
        x.yarb5()
class mythread79(threading.Thread):
    def __init__(self,m,n):
        threading.Thread.__init__(self)
        self.m = m
        self.n = n
    def run(self):
        from running import no
        x = no(self.m,self.n)
        x.yarb5()
class Ui_second_window(QWidget):
    # m ====> number of device (m,n)
    # n ====> date 1=day , 2 = Week,3=Month ,4=year
    def table(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self.window)
        self.window.show()


    def message(self):
        src = 'C:/Users/noha.omar/Desktop/Govee1'
        trg = 'CC:/Users/noha.omar/Desktop/Govee Export/'

        # REMOVE DIR TO PREVENT OVERRIDE
        if os.path.exists(trg):
            shutil.rmtree(trg)
        # MAKE NEW DIR
        directory = "Govee Export"
        parent_dir = "C:/Users/noha.omar/Desktop/Desktop/"
        path = os.path.join(parent_dir, directory)
        os.mkdir(path)

        # COPY ALL FILES
        files = os.listdir(src)
        ren = os.listdir(trg)
        for fname in files:
            # copying the files to the
            # destination directory
            shutil.copy2(os.path.join(src, fname), trg)

        #
        for filename in os.listdir(trg):
            my_dest = filename.replace("yarb", "Device")
            my_source = trg + filename
            my_dest = trg + my_dest
            os.rename(my_source, my_dest)
        # print("hello")
        # time.sleep(7)
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setText("Data Export succssfully")
        msg.setWindowTitle("Export")
        msg.setWindowIcon(QtGui.QIcon('icon.png'))
        msg.setStandardButtons(QMessageBox.Ok )
        msg.exec_()
    def combobox(self):
        txt2=self.comboBox_2.currentText()
        print(txt2)
        txt=self.comboBox.currentText()
        if txt == "Device 1" and txt2 == "Day" :
            thread1 = mythread1(1,1)
            thread1.start()
        elif txt == "Device 1" and txt2 == "Week" :
            thread1 = mythread1(1,2)
            thread1.start()
        elif txt == "Device 1" and txt2 == "Month" :
            thread1 = mythread1(1,3)
            thread1.start()
        elif txt == "Device 1" and txt2 == "Year" :
            thread1 = mythread1(1,4)
            thread1.start()
        elif txt == "Device 2" and txt2 == "Day" :
            thread2 = mythread2(2,1)
            thread2.start()
        elif txt == "Device 2" and txt2 == "Week" :
            thread2 = mythread2(2,2)
            thread2.start()
        elif txt == "Device 2" and txt2 == "Month" :
            thread2 = mythread2(2,3)
            thread2.start()
        elif txt == "Device 2" and txt2 == "Year" :
            thread2 = mythread2(2,4)
            thread2.start()
        elif txt == "Device 3" and txt2 == "Day" :
            thread2 = mythread3(3,1)
            thread2.start()
        elif txt == "Device 3" and txt2 == "Week" :
            thread2 = mythread3(3,2)
            thread2.start()
        elif txt == "Device 3" and txt2 == "Month" :
            thread2 = mythread3(3,3)
            thread2.start()
        elif txt == "Device 3" and txt2 == "Year" :
            thread2 = mythread3(3,4)
            thread2.start()
        elif txt == "Device 4" and txt2 == "Day":
            thread2 = mythread4(4, 1)
            thread2.start()
        elif txt == "Device 4" and txt2 == "Week":
            thread2 = mythread4(4, 2)
            thread2.start()
        elif txt == "Device 4" and txt2 == "Month":
            thread2 = mythread4(4, 3)
            thread2.start()
        elif txt == "Device 4" and txt2 == "Year":
            thread2 = mythread4(4, 4)
            thread2.start()
        elif txt == "Device 5" and txt2 == "Day":
            thread2 = mythread5(5, 1)
            thread2.start()
        elif txt == "Device 5" and txt2 == "Week":
            thread2 = mythread5(5, 2)
            thread2.start()
        elif txt == "Device 5" and txt2 == "Month":
            thread2 = mythread5(5, 3)
            thread2.start()
        elif txt == "Device 5" and txt2 == "Year":
            thread2 = mythread5(5, 4)
            thread2.start()
        elif txt == "Device 6" and txt2 == "Day":
            thread2 = mythread5(6, 1)
            thread2.start()
        elif txt == "Device 6" and txt2 == "Week":
            thread2 = mythread6(6, 2)
            thread2.start()
        elif txt == "Device 6" and txt2 == "Month":
            thread2 = mythread6(6, 3)
            thread2.start()
        elif txt == "Device 6" and txt2 == "Year":
            thread2 = mythread6(6, 4)
            thread2.start()
        elif txt == "Device 7" and txt2 == "Day":
            thread2 = mythread7(7, 1)
            thread2.start()
        elif txt == "Device 7" and txt2 == "Week":
            thread2 = mythread7(7, 2)
            thread2.start()
        elif txt == "Device 7" and txt2 == "Month":
            thread2 = mythread7(7, 3)
            thread2.start()
        elif txt == "Device 7" and txt2 == "Year":
            thread2 = mythread7(7, 4)
            thread2.start()
        elif txt == "Device 8" and txt2 == "Day":
            thread2 = mythread8(8, 1)
            thread2.start()
        elif txt == "Device 8" and txt2 == "Week":
            thread2 = mythread8(8, 2)
            thread2.start()
        elif txt == "Device 8" and txt2 == "Month":
            thread2 = mythread8(8, 3)
            thread2.start()
        elif txt == "Device 8" and txt2 == "Year":
            thread2 = mythread8(8, 4)
            thread2.start()
        elif txt == "Device 9" and txt2 == "Day":
            thread2 = mythread9(9, 1)
            thread2.start()
        elif txt == "Device 9" and txt2 == "Week":
            thread2 = mythread9(9, 2)
            thread2.start()
        elif txt == "Device 9" and txt2 == "Month":
            thread2 = mythread9(9, 3)
            thread2.start()
        elif txt == "Device 9" and txt2 == "Year":
            thread2 = mythread9(9, 4)
            thread2.start()
        elif txt == "Device 10" and txt2 == "Day":
            thread2 = mythread10(10, 1)
            thread2.start()
        elif txt == "Device 10" and txt2 == "Week":
            thread2 = mythread10(10, 2)
            thread2.start()
        elif txt == "Device 10" and txt2 == "Month":
            thread2 = mythread10(10, 3)
            thread2.start()
        elif txt == "Device 10" and txt2 == "Year":
            thread2 = mythread10(10, 4)
            thread2.start()
        elif txt == "Device 11" and txt2 == "Day":
            thread2 = mythread10(11, 1)
            thread2.start()
        elif txt == "Device 11" and txt2 == "Week":
            thread2 = mythread10(11, 2)
            thread2.start()
        elif txt == "Device 11" and txt2 == "Month":
            thread2 = mythread10(11, 3)
            thread2.start()
        elif txt == "Device 11" and txt2 == "Year":
            thread2 = mythread10(11, 4)
            thread2.start()
        elif txt == "Device 12" and txt2 == "Day":
            thread2 = mythread10(12, 1)
            thread2.start()
        elif txt == "Device 12" and txt2 == "Week":
            thread2 = mythread10(12, 2)
            thread2.start()
        elif txt == "Device 12" and txt2 == "Month":
            thread2 = mythread10(12, 3)
            thread2.start()
        elif txt == "Device 12" and txt2 == "Year":
            thread2 = mythread10(12, 4)
            thread2.start()
        elif txt == "Device 13" and txt2 == "Day":
            thread2 = mythread10(13, 1)
            thread2.start()
        elif txt == "Device 13" and txt2 == "Week":
            thread2 = mythread10(13, 2)
            thread2.start()
        elif txt == "Device 13" and txt2 == "Month":
            thread2 = mythread10(13, 3)
            thread2.start()
        elif txt == "Device 13" and txt2 == "Year":
            thread2 = mythread10(13, 4)
            thread2.start()

        elif txt == "Device 14" and txt2 == "Day":
            thread2 = mythread10(14, 1)
            thread2.start()
        elif txt == "Device 14" and txt2 == "Week":
            thread2 = mythread10(14, 2)
            thread2.start()
        elif txt == "Device 14" and txt2 == "Month":
            thread2 = mythread10(14, 3)
            thread2.start()
        elif txt == "Device 14" and txt2 == "Year":
            thread2 = mythread10(14, 4)
            thread2.start()
        elif txt == "Device 15" and txt2 == "Day":
            thread2 = mythread10(15, 1)
            thread2.start()
        elif txt == "Device 15" and txt2 == "Week":
            thread2 = mythread10(15, 2)
            thread2.start()
        elif txt == "Device 15" and txt2 == "Month":
            thread2 = mythread10(15, 3)
            thread2.start()
        elif txt == "Device 15" and txt2 == "Year":
            thread2 = mythread10(15, 4)
            thread2.start()
        elif txt == "Device 16" and txt2 == "Day":
            thread2 = mythread16(16, 1)
            thread2.start()
        elif txt == "Device 16" and txt2 == "Week":
            thread2 = mythread16(16, 2)
            thread2.start()
        elif txt == "Device 16" and txt2 == "Month":
            thread2 = mythread16(16, 3)
            thread2.start()
        elif txt == "Device 16" and txt2 == "Year":
            thread2 = mythread16(16, 4)
            thread2.start()

        elif txt == "Device 20" and txt2 == "Day":
            thread2 = mythread10(20, 1)
            thread2.start()
        elif txt == "Device 20" and txt2 == "Week":
            thread2 = mythread10(20, 2)
            thread2.start()
        elif txt == "Device 20" and txt2 == "Month":
            thread2 = mythread10(20, 3)
            thread2.start()
        elif txt == "Device 20" and txt2 == "Year":
            thread2 = mythread10(20, 4)
            thread2.start()

        elif txt == "Device 21" and txt2 == "Day":
            thread2 = mythread10(21, 1)
            thread2.start()
        elif txt == "Device 21" and txt2 == "Week":
            thread2 = mythread10(21, 2)
            thread2.start()

        elif txt == "Device 21" and txt2 == "Month":
            thread2 = mythread10(21, 3)
            thread2.start()
        elif txt == "Device 21" and txt2 == "Year":
            thread2 = mythread10(21, 4)
            thread2.start()

        elif txt == "Device 22" and txt2 == "Day":
            thread2 = mythread10(22, 1)
            thread2.start()
        elif txt == "Device 22" and txt2 == "Week":
            thread2 = mythread10(22, 2)
            thread2.start()

        elif txt == "Device 22" and txt2 == "Month":
            thread2 = mythread10(22, 3)
            thread2.start()
        elif txt == "Device 22" and txt2 == "Year":
            thread2 = mythread10(22, 4)
            thread2.start()

        elif txt == "Device 23" and txt2 == "Day":
            thread2 = mythread10(23, 1)
            thread2.start()
        elif txt == "Device 23" and txt2 == "Week":
            thread2 = mythread10(23, 2)
            thread2.start()

        elif txt == "Device 23" and txt2 == "Month":
            thread2 = mythread10(23, 3)
            thread2.start()
        elif txt == "Device 23" and txt2 == "Year":
            thread2 = mythread10(23, 4)
            thread2.start()

        elif txt == "Device 24" and txt2 == "Day":
            thread2 = mythread10(24, 1)
            thread2.start()
        elif txt == "Device 24" and txt2 == "Week":
            thread2 = mythread10(24, 2)
            thread2.start()

        elif txt == "Device 24" and txt2 == "Month":
            thread2 = mythread10(24, 3)
            thread2.start()
        elif txt == "Device 24" and txt2 == "Year":
            thread2 = mythread10(24, 4)
            thread2.start()

        elif txt == "Device 25" and txt2 == "Day":
            thread2 = mythread10(25, 1)
            thread2.start()
        elif txt == "Device 25" and txt2 == "Week":
            thread2 = mythread10(25, 2)
            thread2.start()

        elif txt == "Device 25" and txt2 == "Month":
            thread2 = mythread10(25, 3)
            thread2.start()
        elif txt == "Device 25" and txt2 == "Year":
            thread2 = mythread10(25, 4)
            thread2.start()

        elif txt == "Device 26" and txt2 == "Day":
            thread2 = mythread10(26, 1)
            thread2.start()
        elif txt == "Device 26" and txt2 == "Week":
            thread2 = mythread10(26, 2)
            thread2.start()

        elif txt == "Device 26" and txt2 == "Month":
            thread2 = mythread10(26, 3)
            thread2.start()
        elif txt == "Device 26" and txt2 == "Year":
            thread2 = mythread10(26, 4)
            thread2.start()

        elif txt == "Device 27" and txt2 == "Day":
            thread2 = mythread10(27, 1)
            thread2.start()
        elif txt == "Device 27" and txt2 == "Week":
            thread2 = mythread10(27, 2)
            thread2.start()

        elif txt == "Device 27" and txt2 == "Month":
            thread2 = mythread10(27, 3)
            thread2.start()
        elif txt == "Device 27" and txt2 == "Year":
            thread2 = mythread10(27, 4)
            thread2.start()

        elif txt == "Device 28" and txt2 == "Day":
            thread2 = mythread10(28, 1)
            thread2.start()
        elif txt == "Device 28" and txt2 == "Week":
            thread2 = mythread10(28, 2)
            thread2.start()

        elif txt == "Device 28" and txt2 == "Month":
            thread2 = mythread10(28, 3)
            thread2.start()
        elif txt == "Device 28" and txt2 == "Year":
            thread2 = mythread10(28, 4)
            thread2.start()

        elif txt == "Device 29" and txt2 == "Day":
            thread2 = mythread10(29, 1)
            thread2.start()
        elif txt == "Device 29" and txt2 == "Week":
            thread2 = mythread10(29, 2)
            thread2.start()

        elif txt == "Device 29" and txt2 == "Month":
            thread2 = mythread10(29, 3)
            thread2.start()
        elif txt == "Device 29" and txt2 == "Year":
            thread2 = mythread10(29, 4)
            thread2.start()

        elif txt == "Device 30" and txt2 == "Day":
            thread2 = mythread10(30, 1)
            thread2.start()
        elif txt == "Device 30" and txt2 == "Week":
            thread2 = mythread10(30, 2)
            thread2.start()

        elif txt == "Device 30" and txt2 == "Month":
            thread2 = mythread10(30, 3)
            thread2.start()
        elif txt == "Device 30" and txt2 == "Year":
            thread2 = mythread10(30, 4)
            thread2.start()

        elif txt == "Device 31" and txt2 == "Day":
            thread2 = mythread10(31, 1)
            thread2.start()
        elif txt == "Device 31" and txt2 == "Week":
            thread2 = mythread10(31, 2)
            thread2.start()

        elif txt == "Device 31" and txt2 == "Month":
            thread2 = mythread10(31, 3)
            thread2.start()
        elif txt == "Device 31" and txt2 == "Year":
            thread2 = mythread10(31, 4)
            thread2.start()

        elif txt == "Device 32" and txt2 == "Day":
            thread2 = mythread10(32, 1)
            thread2.start()
        elif txt == "Device 32" and txt2 == "Week":
            thread2 = mythread10(32, 2)
            thread2.start()

        elif txt == "Device 32" and txt2 == "Month":
            thread2 = mythread10(32, 3)
            thread2.start()
        elif txt == "Device 32" and txt2 == "Year":
            thread2 = mythread10(32, 4)
            thread2.start()

        elif txt == "Device 33" and txt2 == "Day":
            thread2 = mythread10(33, 1)
            thread2.start()
        elif txt == "Device 33" and txt2 == "Week":
            thread2 = mythread10(33, 2)
            thread2.start()

        elif txt == "Device 33" and txt2 == "Month":
            thread2 = mythread10(33, 3)
            thread2.start()
        elif txt == "Device 33" and txt2 == "Year":
            thread2 = mythread10(33, 4)
            thread2.start()
        elif txt == "Device 34" and txt2 == "Day":
            thread2 = mythread10(34, 1)
            thread2.start()
        elif txt == "Device 34" and txt2 == "Week":
            thread2 = mythread10(34, 2)
            thread2.start()

        elif txt == "Device 34" and txt2 == "Month":
            thread2 = mythread10(34, 3)
            thread2.start()
        elif txt == "Device 34" and txt2 == "Year":
            thread2 = mythread10(34, 4)
            thread2.start()

        elif txt == "Device 35" and txt2 == "Day":
            thread2 = mythread10(35, 1)
            thread2.start()
        elif txt == "Device 35" and txt2 == "Week":
            thread2 = mythread10(35, 2)
            thread2.start()

        elif txt == "Device 35" and txt2 == "Month":
            thread2 = mythread10(35, 3)
            thread2.start()
        elif txt == "Device 35" and txt2 == "Year":
            thread2 = mythread10(35, 4)
            thread2.start()

        elif txt == "Device 36" and txt2 == "Day":
            thread2 = mythread10(36, 1)
            thread2.start()
        elif txt == "Device 36" and txt2 == "Week":
            thread2 = mythread10(36, 2)
            thread2.start()

        elif txt == "Device 36" and txt2 == "Month":
            thread2 = mythread10(36, 3)
            thread2.start()
        elif txt == "Device 36" and txt2 == "Year":
            thread2 = mythread10(36, 4)
            thread2.start()

        elif txt == "Device 37" and txt2 == "Day":
            thread2 = mythread10(37, 1)
            thread2.start()
        elif txt == "Device 37" and txt2 == "Week":
            thread2 = mythread10(37, 2)
            thread2.start()

        elif txt == "Device 37" and txt2 == "Month":
            thread2 = mythread10(37, 3)
            thread2.start()
        elif txt == "Device 37" and txt2 == "Year":
            thread2 = mythread10(37, 4)
            thread2.start()

        elif txt == "Device 38" and txt2 == "Day":
            thread2 = mythread10(38, 1)
            thread2.start()
        elif txt == "Device 38" and txt2 == "Week":
            thread2 = mythread10(38, 2)
            thread2.start()

        elif txt == "Device 38" and txt2 == "Month":
            thread2 = mythread10(38, 3)
            thread2.start()
        elif txt == "Device 38" and txt2 == "Year":
            thread2 = mythread10(38, 4)
            thread2.start()

        elif txt == "Device 39" and txt2 == "Day":
            thread2 = mythread10(39, 1)
            thread2.start()
        elif txt == "Device 39" and txt2 == "Week":
            thread2 = mythread10(39, 2)
            thread2.start()

        elif txt == "Device 39" and txt2 == "Month":
            thread2 = mythread10(39, 3)
            thread2.start()
        elif txt == "Device 39" and txt2 == "Year":
            thread2 = mythread10(39, 4)
            thread2.start()

        elif txt == "Device 40" and txt2 == "Day":
            thread2 = mythread10(40, 1)
            thread2.start()
        elif txt == "Device 40" and txt2 == "Week":
            thread2 = mythread10(40, 2)
            thread2.start()

        elif txt == "Device 40" and txt2 == "Month":
            thread2 = mythread10(40, 3)
            thread2.start()
        elif txt == "Device 40" and txt2 == "Year":
            thread2 = mythread10(40, 4)
            thread2.start()

        elif txt == "Device 41" and txt2 == "Day":
            thread2 = mythread10(41, 1)
            thread2.start()
        elif txt == "Device 41" and txt2 == "Week":
            thread2 = mythread10(41, 2)
            thread2.start()

        elif txt == "Device 41" and txt2 == "Month":
            thread2 = mythread10(41, 3)
            thread2.start()
        elif txt == "Device 41" and txt2 == "Year":
            thread2 = mythread10(41, 4)
            thread2.start()

        elif txt == "Device 42" and txt2 == "Day":
            thread2 = mythread10(42, 1)
            thread2.start()
        elif txt == "Device 42" and txt2 == "Week":
            thread2 = mythread10(42, 2)
            thread2.start()

        elif txt == "Device 42" and txt2 == "Month":
            thread2 = mythread10(42, 3)
            thread2.start()
        elif txt == "Device 42" and txt2 == "Year":
            thread2 = mythread10(42, 4)
            thread2.start()

        elif txt == "Device 43" and txt2 == "Day":
            thread2 = mythread10(43, 1)
            thread2.start()
        elif txt == "Device 43" and txt2 == "Week":
            thread2 = mythread10(43, 2)
            thread2.start()

        elif txt == "Device 43" and txt2 == "Month":
            thread2 = mythread10(43, 3)
            thread2.start()
        elif txt == "Device 43" and txt2 == "Year":
            thread2 = mythread10(43, 4)
            thread2.start()

        elif txt == "Device 44" and txt2 == "Day":
            thread2 = mythread10(44, 1)
            thread2.start()
        elif txt == "Device 44" and txt2 == "Week":
            thread2 = mythread10(44, 2)
            thread2.start()

        elif txt == "Device 44" and txt2 == "Month":
            thread2 = mythread10(44, 3)
            thread2.start()
        elif txt == "Device 44" and txt2 == "Year":
            thread2 = mythread10(44, 4)
            thread2.start()

        elif txt == "Device 45" and txt2 == "Day":
            thread2 = mythread10(45, 1)
            thread2.start()
        elif txt == "Device 45" and txt2 == "Week":
            thread2 = mythread10(45, 2)
            thread2.start()

        elif txt == "Device 45" and txt2 == "Month":
            thread2 = mythread10(45, 3)
            thread2.start()
        elif txt == "Device 45" and txt2 == "Year":
            thread2 = mythread10(45, 4)
            thread2.start()

        elif txt == "Device 46" and txt2 == "Day":
            thread2 = mythread10(46, 1)
            thread2.start()
        elif txt == "Device 46" and txt2 == "Week":
            thread2 = mythread10(46, 2)
            thread2.start()

        elif txt == "Device 46" and txt2 == "Month":
            thread2 = mythread10(46, 3)
            thread2.start()
        elif txt == "Device 46" and txt2 == "Year":
            thread2 = mythread10(46, 4)
            thread2.start()
        elif txt == "Device 47" and txt2 == "Day":
            thread2 = mythread10(47, 1)
            thread2.start()
        elif txt == "Device 47" and txt2 == "Week":
            thread2 = mythread10(47, 2)
            thread2.start()

        elif txt == "Device 47" and txt2 == "Month":
            thread2 = mythread10(47, 3)
            thread2.start()
        elif txt == "Device 47" and txt2 == "Year":
            thread2 = mythread10(47, 4)
            thread2.start()

        elif txt == "Device 48" and txt2 == "Day":
            thread2 = mythread10(48, 1)
            thread2.start()
        elif txt == "Device 48" and txt2 == "Week":
            thread2 = mythread10(48, 2)
            thread2.start()

        elif txt == "Device 48" and txt2 == "Month":
            thread2 = mythread10(48, 3)
            thread2.start()
        elif txt == "Device 48" and txt2 == "Year":
            thread2 = mythread10(48, 4)
            thread2.start()

        elif txt == "Device 49" and txt2 == "Day":
            thread2 = mythread10(49, 1)
            thread2.start()
        elif txt == "Device 49" and txt2 == "Week":
            thread2 = mythread10(49, 2)
            thread2.start()

        elif txt == "Device 49" and txt2 == "Month":
            thread2 = mythread10(49, 3)
            thread2.start()
        elif txt == "Device 49" and txt2 == "Year":
            thread2 = mythread10(49, 4)
            thread2.start()

        elif txt == "Device 50" and txt2 == "Day":
            thread2 = mythread10(50, 1)
            thread2.start()
        elif txt == "Device 50" and txt2 == "Week":
            thread2 = mythread10(50, 2)
            thread2.start()

        elif txt == "Device 50" and txt2 == "Month":
            thread2 = mythread10(50, 3)
            thread2.start()
        elif txt == "Device 50" and txt2 == "Year":
            thread2 = mythread10(50, 4)
            thread2.start()

        elif txt == "Device 51" and txt2 == "Day":
            thread2 = mythread10(51, 1)
            thread2.start()
        elif txt == "Device 51" and txt2 == "Week":
            thread2 = mythread10(51, 2)
            thread2.start()

        elif txt == "Device 51" and txt2 == "Month":
            thread2 = mythread10(51, 3)
            thread2.start()
        elif txt == "Device 51" and txt2 == "Year":
            thread2 = mythread10(51, 4)
            thread2.start()

        elif txt == "Device 52" and txt2 == "Day":
            thread2 = mythread10(52, 1)
            thread2.start()
        elif txt == "Device 52" and txt2 == "Week":
            thread2 = mythread10(52, 2)
            thread2.start()

        elif txt == "Device 52" and txt2 == "Month":
            thread2 = mythread10(52, 3)
            thread2.start()
        elif txt == "Device 52" and txt2 == "Year":
            thread2 = mythread10(52, 4)
            thread2.start()

        elif txt == "Device 53" and txt2 == "Day":
            thread2 = mythread10(53, 1)
            thread2.start()
        elif txt == "Device 53" and txt2 == "Week":
            thread2 = mythread10(53, 2)
            thread2.start()

        elif txt == "Device 53" and txt2 == "Month":
            thread2 = mythread10(53, 3)
            thread2.start()
        elif txt == "Device 53" and txt2 == "Year":
            thread2 = mythread10(53, 4)
            thread2.start()

        elif txt == "Device 54" and txt2 == "Day":
            thread2 = mythread10(54, 1)
            thread2.start()
        elif txt == "Device 54" and txt2 == "Week":
            thread2 = mythread10(54, 2)
            thread2.start()

        elif txt == "Device 54" and txt2 == "Month":
            thread2 = mythread10(54, 3)
            thread2.start()
        elif txt == "Device 54" and txt2 == "Year":
            thread2 = mythread10(54, 4)
            thread2.start()
        elif txt == "Device 55" and txt2 == "Day":
            thread2 = mythread10(55, 1)
            thread2.start()
        elif txt == "Device 55" and txt2 == "Week":
            thread2 = mythread10(55, 2)
            thread2.start()

        elif txt == "Device 55" and txt2 == "Month":
            thread2 = mythread10(55, 3)
            thread2.start()
        elif txt == "Device 55" and txt2 == "Year":
            thread2 = mythread10(55, 4)
            thread2.start()


        elif txt == "Device 56" and txt2 == "Day":
            thread2 = mythread10(56, 1)
            thread2.start()
        elif txt == "Device 56" and txt2 == "Week":
            thread2 = mythread10(56, 2)
            thread2.start()

        elif txt == "Device 56" and txt2 == "Month":
            thread2 = mythread10(56, 3)
            thread2.start()
        elif txt == "Device 56" and txt2 == "Year":
            thread2 = mythread10(56, 4)
            thread2.start()

        elif txt == "Device 57" and txt2 == "Day":
            thread2 = mythread10(57, 1)
            thread2.start()
        elif txt == "Device 57" and txt2 == "Week":
            thread2 = mythread10(57, 2)
            thread2.start()

        elif txt == "Device 57" and txt2 == "Month":
            thread2 = mythread10(57, 3)
            thread2.start()
        elif txt == "Device 57" and txt2 == "Year":
            thread2 = mythread10(57, 4)
            thread2.start()
        elif txt == "Device 58" and txt2 == "Day":
            thread2 = mythread10(58, 1)
            thread2.start()
        elif txt == "Device 58" and txt2 == "Week":
            thread2 = mythread10(58, 2)
            thread2.start()

        elif txt == "Device 58" and txt2 == "Month":
            thread2 = mythread10(58, 3)
            thread2.start()
        elif txt == "Device 58" and txt2 == "Year":
            thread2 = mythread10(58, 4)
            thread2.start()

        elif txt == "Device 59" and txt2 == "Day":
            thread2 = mythread10(59, 1)
            thread2.start()
        elif txt == "Device 59" and txt2 == "Week":
            thread2 = mythread10(59, 2)
            thread2.start()

        elif txt == "Device 59" and txt2 == "Month":
            thread2 = mythread10(59, 3)
            thread2.start()
        elif txt == "Device 59" and txt2 == "Year":
            thread2 = mythread10(59, 4)
            thread2.start()

        elif txt == "Device 60" and txt2 == "Day":
            thread2 = mythread10(60, 1)
            thread2.start()
        elif txt == "Device 60" and txt2 == "Week":
            thread2 = mythread10(60, 2)
            thread2.start()

        elif txt == "Device 60" and txt2 == "Month":
            thread2 = mythread10(60, 3)
            thread2.start()
        elif txt == "Device 60" and txt2 == "Year":
            thread2 = mythread10(60, 4)
            thread2.start()

        elif txt == "Device 61" and txt2 == "Day":
            thread2 = mythread10(61, 1)
            thread2.start()
        elif txt == "Device 61" and txt2 == "Week":
            thread2 = mythread10(61, 2)
            thread2.start()

        elif txt == "Device 61" and txt2 == "Month":
            thread2 = mythread10(61, 3)
            thread2.start()
        elif txt == "Device 61" and txt2 == "Year":
            thread2 = mythread10(61, 4)
            thread2.start()

        elif txt == "Device 62" and txt2 == "Day":
            thread2 = mythread10(62, 1)
            thread2.start()
        elif txt == "Device 62" and txt2 == "Week":
            thread2 = mythread10(62, 2)
            thread2.start()

        elif txt == "Device 62" and txt2 == "Month":
            thread2 = mythread10(62, 3)
            thread2.start()
        elif txt == "Device 62" and txt2 == "Year":
            thread2 = mythread10(62, 4)
            thread2.start()

        elif txt == "Device 63" and txt2 == "Day":
            thread2 = mythread10(63, 1)
            thread2.start()
        elif txt == "Device 63" and txt2 == "Week":
            thread2 = mythread10(63, 2)
            thread2.start()

        elif txt == "Device 63" and txt2 == "Month":
            thread2 = mythread10(63, 3)
            thread2.start()
        elif txt == "Device 63" and txt2 == "Year":
            thread2 = mythread10(63, 4)
            thread2.start()

        elif txt == "Device 64" and txt2 == "Day":
            thread2 = mythread10(64, 1)
            thread2.start()
        elif txt == "Device 64" and txt2 == "Week":
            thread2 = mythread10(64, 2)
            thread2.start()

        elif txt == "Device 64" and txt2 == "Month":
            thread2 = mythread10(64, 3)
            thread2.start()
        elif txt == "Device 64" and txt2 == "Year":
            thread2 = mythread10(64, 4)
            thread2.start()

        elif txt == "Device 65" and txt2 == "Day":
            thread2 = mythread10(65, 1)
            thread2.start()
        elif txt == "Device 65" and txt2 == "Week":
            thread2 = mythread10(65, 2)
            thread2.start()

        elif txt == "Device 65" and txt2 == "Month":
            thread2 = mythread10(65, 3)
            thread2.start()
        elif txt == "Device 65" and txt2 == "Year":
            thread2 = mythread10(65, 4)
            thread2.start()

        elif txt == "Device 66" and txt2 == "Day":
            thread2 = mythread10(66, 1)
            thread2.start()
        elif txt == "Device 66" and txt2 == "Week":
            thread2 = mythread10(66, 2)
            thread2.start()

        elif txt == "Device 66" and txt2 == "Month":
            thread2 = mythread10(66, 3)
            thread2.start()
        elif txt == "Device 66" and txt2 == "Year":
            thread2 = mythread10(66, 4)
            thread2.start()

        elif txt == "Device 67" and txt2 == "Day":
            thread2 = mythread10(67, 1)
            thread2.start()
        elif txt == "Device 67" and txt2 == "Week":
            thread2 = mythread10(67, 2)
            thread2.start()

        elif txt == "Device 67" and txt2 == "Month":
            thread2 = mythread10(67, 3)
            thread2.start()
        elif txt == "Device 67" and txt2 == "Year":
            thread2 = mythread10(67, 4)
            thread2.start()

        elif txt == "Device 68" and txt2 == "Day":
            thread2 = mythread10(68, 1)
            thread2.start()
        elif txt == "Device 68" and txt2 == "Week":
            thread2 = mythread10(68, 2)
            thread2.start()

        elif txt == "Device 68" and txt2 == "Month":
            thread2 = mythread10(68, 3)
            thread2.start()
        elif txt == "Device 68" and txt2 == "Year":
            thread2 = mythread10(68, 4)
            thread2.start()


        elif txt == "Device 69" and txt2 == "Day":
            thread2 = mythread10(69, 1)
            thread2.start()
        elif txt == "Device 69" and txt2 == "Week":
            thread2 = mythread10(69, 2)
            thread2.start()

        elif txt == "Device 69" and txt2 == "Month":
            thread2 = mythread10(69, 3)
            thread2.start()
        elif txt == "Device 69" and txt2 == "Year":
            thread2 = mythread10(69, 4)
            thread2.start()
        elif txt == "Device 70" and txt2 == "Day":
            thread2 = mythread10(70, 1)
            thread2.start()
        elif txt == "Device 70" and txt2 == "Week":
            thread2 = mythread10(70, 2)
            thread2.start()

        elif txt == "Device 70" and txt2 == "Month":
            thread2 = mythread10(70, 3)
            thread2.start()
        elif txt == "Device 70" and txt2 == "Year":
            thread2 = mythread10(70, 4)
            thread2.start()


        elif txt == "Device 71" and txt2 == "Day":
            thread2 = mythread10(71, 1)
            thread2.start()
        elif txt == "Device 71" and txt2 == "Week":
            thread2 = mythread10(71, 2)
            thread2.start()

        elif txt == "Device 71" and txt2 == "Month":
            thread2 = mythread10(71, 3)
            thread2.start()
        elif txt == "Device 71" and txt2 == "Year":
            thread2 = mythread10(71, 4)
            thread2.start()
        elif txt == "Device 72" and txt2 == "Day":
            thread2 = mythread10(72, 1)
            thread2.start()
        elif txt == "Device 72" and txt2 == "Week":
            thread2 = mythread10(72, 2)
            thread2.start()

        elif txt == "Device 72" and txt2 == "Month":
            thread2 = mythread10(72, 3)
            thread2.start()
        elif txt == "Device 72" and txt2 == "Year":
            thread2 = mythread10(72, 4)
            thread2.start()

        elif txt == "Device 73" and txt2 == "Day":
            thread2 = mythread10(73, 1)
            thread2.start()
        elif txt == "Device 73" and txt2 == "Week":
            thread2 = mythread10(73, 2)
            thread2.start()

        elif txt == "Device 73" and txt2 == "Month":
            thread2 = mythread10(73, 3)
            thread2.start()
        elif txt == "Device 73" and txt2 == "Year":
            thread2 = mythread10(73, 4)
            thread2.start()

        elif txt == "Device 74" and txt2 == "Day":
            thread2 = mythread10(74, 1)
            thread2.start()
        elif txt == "Device 74" and txt2 == "Week":
            thread2 = mythread10(74, 2)
            thread2.start()

        elif txt == "Device 74" and txt2 == "Month":
            thread2 = mythread10(74, 3)
            thread2.start()
        elif txt == "Device 74" and txt2 == "Year":
            thread2 = mythread10(74, 4)
            thread2.start()

        elif txt == "Device 74" and txt2 == "Day":
            thread2 = mythread10(74, 1)
            thread2.start()
        elif txt == "Device 74" and txt2 == "Week":
            thread2 = mythread10(74, 2)
            thread2.start()

        elif txt == "Device 74" and txt2 == "Month":
            thread2 = mythread10(74, 3)
            thread2.start()
        elif txt == "Device 74" and txt2 == "Year":
            thread2 = mythread10(74, 4)
            thread2.start()

        elif txt == "Device 75" and txt2 == "Day":
            thread2 = mythread10(75, 1)
            thread2.start()
        elif txt == "Device 75" and txt2 == "Week":
            thread2 = mythread10(75, 2)
            thread2.start()

        elif txt == "Device 75" and txt2 == "Month":
            thread2 = mythread10(75, 3)
            thread2.start()
        elif txt == "Device 75" and txt2 == "Year":
            thread2 = mythread10(75, 4)
            thread2.start()

        elif txt == "Device 76" and txt2 == "Day":
            thread2 = mythread10(76, 1)
            thread2.start()
        elif txt == "Device 76" and txt2 == "Week":
            thread2 = mythread10(76, 2)
            thread2.start()

        elif txt == "Device 76" and txt2 == "Month":
            thread2 = mythread10(76, 3)
            thread2.start()
        elif txt == "Device 76" and txt2 == "Year":
            thread2 = mythread10(76, 4)
            thread2.start()

        elif txt == "Device 77" and txt2 == "Day":
            thread2 = mythread10(77, 1)
            thread2.start()
        elif txt == "Device 77" and txt2 == "Week":
            thread2 = mythread10(77, 2)
            thread2.start()

        elif txt == "Device 77" and txt2 == "Month":
            thread2 = mythread10(77, 3)
            thread2.start()
        elif txt == "Device 77" and txt2 == "Year":
            thread2 = mythread10(77, 4)
            thread2.start()
        elif txt == "Device 78" and txt2 == "Day":
            thread2 = mythread78(78, 1)
            thread2.start()
        elif txt == "Device 78" and txt2 == "Week":
            thread2 = mythread78(78, 2)
            thread2.start()

        elif txt == "Device 78" and txt2 == "Month":
            thread2 = mythread78(78, 3)
            thread2.start()
        elif txt == "Device 78" and txt2 == "Year":
            thread2 = mythread78(78, 4)
            thread2.start()

        elif txt == "Device 79" and txt2 == "Day":
            thread2 = mythread79(79, 1)
            thread2.start()
        elif txt == "Device 79" and txt2 == "Week":
            thread2 = mythread79(79, 2)
            thread2.start()

        elif txt == "Device 79" and txt2 == "Month":
            thread2 = mythread79(79, 3)
            thread2.start()
        elif txt == "Device 79" and txt2 == "Year":
            thread2 = mythread79(79, 4)
            thread2.start()
        elif txt == "Device 80" and txt2 == "Day":
            thread2 = mythread10(80, 1)
            thread2.start()
        elif txt == "Device 80" and txt2 == "Week":
            thread2 = mythread10(80, 2)
            thread2.start()

        elif txt == "Device 80" and txt2 == "Month":
            thread2 = mythread10(80, 3)
            thread2.start()
        elif txt == "Device 80" and txt2 == "Year":
            thread2 = mythread10(80, 4)
            thread2.start()
        elif txt == "Device 81" and txt2 == "Day":
            thread2 = mythread10(81, 1)
            thread2.start()
        elif txt == "Device 81" and txt2 == "Week":
            thread2 = mythread10(81, 2)
            thread2.start()

        elif txt == "Device 81" and txt2 == "Month":
            thread2 = mythread10(81, 3)
            thread2.start()
        elif txt == "Device 81" and txt2 == "Year":
            thread2 = mythread10(81, 4)
            thread2.start()

        elif txt == "Device 82" and txt2 == "Day":
            thread2 = mythread10(82, 1)
            thread2.start()
        elif txt == "Device 82" and txt2 == "Week":
            thread2 = mythread10(82, 2)
            thread2.start()

        elif txt == "Device 82" and txt2 == "Month":
            thread2 = mythread10(82, 3)
            thread2.start()
        elif txt == "Device 82" and txt2 == "Year":
            thread2 = mythread10(82, 4)
            thread2.start()

        elif txt == "Device 83" and txt2 == "Day":
            thread2 = mythread10(83, 1)
            thread2.start()
        elif txt == "Device 83" and txt2 == "Week":
            thread2 = mythread10(83, 2)
            thread2.start()

        elif txt == "Device 83" and txt2 == "Month":
            thread2 = mythread10(83, 3)
            thread2.start()
        elif txt == "Device 83" and txt2 == "Year":
            thread2 = mythread10(83, 4)
            thread2.start()

        elif txt == "Device 84" and txt2 == "Day":
            thread2 = mythread10(84, 1)
            thread2.start()
        elif txt == "Device 84" and txt2 == "Week":
            thread2 = mythread10(84, 2)
            thread2.start()

        elif txt == "Device 84" and txt2 == "Month":
            thread2 = mythread10(84, 3)
            thread2.start()
        elif txt == "Device 84" and txt2 == "Year":
            thread2 = mythread10(84, 4)
            thread2.start()

        elif txt == "Device 85" and txt2 == "Day":
            thread2 = mythread10(85, 1)
            thread2.start()
        elif txt == "Device 85" and txt2 == "Week":
            thread2 = mythread10(85, 2)
            thread2.start()

        elif txt == "Device 85" and txt2 == "Month":
            thread2 = mythread10(85, 3)
            thread2.start()
        elif txt == "Device 85" and txt2 == "Year":
            thread2 = mythread10(85, 4)
            thread2.start()
        elif txt == "Device 86" and txt2 == "Day":
            thread2 = mythread10(86, 1)
            thread2.start()
        elif txt == "Device 86" and txt2 == "Week":
            thread2 = mythread10(86, 2)
            thread2.start()

        elif txt == "Device 86" and txt2 == "Month":
            thread2 = mythread10(86, 3)
            thread2.start()
        elif txt == "Device 86" and txt2 == "Year":
            thread2 = mythread10(86, 4)
            thread2.start()

        elif txt == "Device 87" and txt2 == "Day":
            thread2 = mythread10(87, 1)
            thread2.start()
        elif txt == "Device 87" and txt2 == "Week":
            thread2 = mythread10(87, 2)
            thread2.start()

        elif txt == "Device 87" and txt2 == "Month":
            thread2 = mythread10(87, 3)
            thread2.start()
        elif txt == "Device 87" and txt2 == "Year":
            thread2 = mythread10(87, 4)
            thread2.start()
        elif txt == "Device 88" and txt2 == "Day":
            thread2 = mythread10(88, 1)
            thread2.start()
        elif txt == "Device 88" and txt2 == "Week":
            thread2 = mythread10(88, 2)
            thread2.start()

        elif txt == "Device 88" and txt2 == "Month":
            thread2 = mythread10(88, 3)
            thread2.start()
        elif txt == "Device 88" and txt2 == "Year":
            thread2 = mythread10(88, 4)
            thread2.start()
        elif txt == "Device 89" and txt2 == "Day":
            thread2 = mythread10(89, 1)
            thread2.start()
        elif txt == "Device 89" and txt2 == "Week":
            thread2 = mythread10(89, 2)
            thread2.start()

        elif txt == "Device 89" and txt2 == "Month":
            thread2 = mythread10(89, 3)
            thread2.start()
        elif txt == "Device 89" and txt2 == "Year":
            thread2 = mythread10(89, 4)
            thread2.start()
        elif txt == "Device 90" and txt2 == "Day":
            thread2 = mythread10(90, 1)
            thread2.start()
        elif txt == "Device 90" and txt2 == "Week":
            thread2 = mythread10(90, 2)
            thread2.start()

        elif txt == "Device 90" and txt2 == "Month":
            thread2 = mythread10(90, 3)
            thread2.start()
        elif txt == "Device 90" and txt2 == "Year":
            thread2 = mythread10(90, 4)
            thread2.start()
        elif txt == "Device 91" and txt2 == "Day":
            thread2 = mythread10(91, 1)
            thread2.start()
        elif txt == "Device 91" and txt2 == "Week":
            thread2 = mythread10(91, 2)
            thread2.start()

        elif txt == "Device 91" and txt2 == "Month":
            thread2 = mythread10(91, 3)
            thread2.start()
        elif txt == "Device 91" and txt2 == "Year":
            thread2 = mythread10(91, 4)
            thread2.start()
        elif txt == "Device 92" and txt2 == "Day":
            thread2 = mythread10(92, 1)
            thread2.start()
        elif txt == "Device 92" and txt2 == "Week":
            thread2 = mythread10(92, 2)
            thread2.start()

        elif txt == "Device 92" and txt2 == "Month":
            thread2 = mythread10(92, 3)
            thread2.start()
        elif txt == "Device 92" and txt2 == "Year":
            thread2 = mythread10(92, 4)
            thread2.start()
        elif txt == "Device 93" and txt2 == "Day":
            thread2 = mythread10(93, 1)
            thread2.start()
        elif txt == "Device 93" and txt2 == "Week":
            thread2 = mythread10(93, 2)
            thread2.start()

        elif txt == "Device 93" and txt2 == "Month":
            thread2 = mythread10(93, 3)
            thread2.start()
        elif txt == "Device 93" and txt2 == "Year":
            thread2 = mythread10(93, 4)
            thread2.start()

        elif txt == "Device 94" and txt2 == "Day":
            thread2 = mythread10(94, 1)
            thread2.start()
        elif txt == "Device 94" and txt2 == "Week":
            thread2 = mythread10(94, 2)
            thread2.start()

        elif txt == "Device 94" and txt2 == "Month":
            thread2 = mythread10(94, 3)
            thread2.start()
        elif txt == "Device 94" and txt2 == "Year":
            thread2 = mythread10(94, 4)
            thread2.start()
        elif txt == "Device 95" and txt2 == "Day":
            thread2 = mythread10(95, 1)
            thread2.start()
        elif txt == "Device 95" and txt2 == "Week":
            thread2 = mythread10(95, 2)
            thread2.start()

        elif txt == "Device 95" and txt2 == "Month":
            thread2 = mythread10(95, 3)
            thread2.start()
        elif txt == "Device 95" and txt2 == "Year":
            thread2 = mythread10(95, 4)
            thread2.start()
        elif txt == "Device 96" and txt2 == "Day":
            thread2 = mythread10(96, 1)
            thread2.start()
        elif txt == "Device 96" and txt2 == "Week":
            thread2 = mythread10(96, 2)
            thread2.start()

        elif txt == "Device 96" and txt2 == "Month":
            thread2 = mythread10(96, 3)
            thread2.start()
        elif txt == "Device 96" and txt2 == "Year":
            thread2 = mythread10(96, 4)
            thread2.start()
        elif txt == "Device 97" and txt2 == "Day":
            thread2 = mythread10(97, 1)
            thread2.start()
        elif txt == "Device 97" and txt2 == "Week":
            thread2 = mythread10(97, 2)
            thread2.start()

        elif txt == "Device 97" and txt2 == "Month":
            thread2 = mythread10(97, 3)
            thread2.start()
        elif txt == "Device 97" and txt2 == "Year":
            thread2 = mythread10(97, 4)
            thread2.start()
        elif txt == "Device 98" and txt2 == "Day":
            thread2 = mythread10(98, 1)
            thread2.start()
        elif txt == "Device 98" and txt2 == "Week":
            thread2 = mythread10(98, 2)
            thread2.start()

        elif txt == "Device 98" and txt2 == "Month":
            thread2 = mythread10(98, 3)
            thread2.start()
        elif txt == "Device 98" and txt2 == "Year":
            thread2 = mythread10(98, 4)
            thread2.start()

        else:
            print("Wrong data")

    def status(self):
        os.system("python t.py")
        # self.window = QtWidgets.QMainWindow()
        # self.ui = Ui_MainWindow2()
        # self.ui.setupUi(self.window)
        # self.window.show()


    def setupUi(self, second_window):
        second_window.setObjectName("second_window")
        second_window.resize(1208, 677)
        second_window.setWindowIcon(QtGui.QIcon('icon.png'))
        second_window.setStyleSheet("background-image: url(2.png);")
        self.centralwidget = QtWidgets.QWidget(second_window)
        self.centralwidget.setObjectName("centralwidget")
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(820, 220, 201, 41))
        self.comboBox.setStyleSheet("font: 75 14pt \"MS Shell Dlg 2\";\n"
                                    "background-image: url(1.JPG);\n"
                                    "color: rgb(0, 170, 255);\n"
                                    "")
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")


        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(570, 210, 381, 51))
        self.label.setStyleSheet("background-image: url(:/newPrefix/1.JPG);\n"
                                 "font: 75 20pt \"MS Shell Dlg 2\";\n"
                                 "")
        self.label.setObjectName("label")

        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(860, 50, 231, 51))
        self.label_2.setStyleSheet("background-image: url(:/newPrefix/1.JPG);\n"
                                   "font: 75 20pt \"MS Shell Dlg 2\";\n"
                                   "color: rgb(0, 170, 255);")
        self.label_2.setObjectName("label_2")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(950, 490, 201, 61))
        self.pushButton.setStyleSheet("background-image: url(:/newPrefix/1.JPG);\n"
                                      "font: 75 22pt \"MS Shell Dlg 2\";\n"
                                      "color: rgb(0, 170, 255);\n"
                                      " border-radius: 25px;\n"
                                      "border: 3px solid #00AAFF;")
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.combobox)
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(510, 490, 201, 61))
        self.pushButton_2.setStyleSheet("background-image: url(:/newPrefix/1.JPG);\n"
                                        "font: 75 22pt \"MS Shell Dlg 2\";\n"
                                        "color: rgb(0, 170, 255);\n"
                                        " border-radius: 25px;\n"
                                        "border: 3px solid #00AAFF;")
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.clicked.connect(self.message)
        self.comboBox_2 = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_2.setGeometry(QtCore.QRect(820, 320, 201, 41))
        self.comboBox_2.setStyleSheet("font: 75 14pt \"MS Shell Dlg 2\";\n"
                                      "background-image: url(:/newPrefix/1.JPG);\n"
                                      "color: rgb(0, 170, 255);\n"
                                      "")
        self.comboBox_2.setObjectName("comboBox_2")

        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(570, 310, 211, 51))
        self.label_3.setStyleSheet("background-image: url(:/newPrefix/1.JPG);\n"
                                   "font: 75 20pt \"MS Shell Dlg 2\";\n"
                                   "")
        self.label_3.setObjectName("label_3")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(740, 550, 201, 61))
        self.pushButton_3.setStyleSheet("background-image: url(:/newPrefix/1.JPG);\n"
                                        "font: 75 22pt \"MS Shell Dlg 2\";\n"
                                        "color: rgb(0, 170, 255);\n"
                                        " border-radius: 25px;\n"
                                        "border: 3px solid #00AAFF;")
        self.pushButton_3.setObjectName("pushButton_3")

        self.pushButton_3.clicked.connect(self.table)

        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(730, 440, 201, 61))
        self.pushButton_4.setStyleSheet("background-image: url(:/newPrefix/1.JPG);\n"
                                        "font: 75 22pt \"MS Shell Dlg 2\";\n"
                                        "color: rgb(0, 170, 255);\n"
                                        " border-radius: 25px;\n"
                                        "border: 3px solid #00AAFF;")
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_4.clicked.connect(self.status)

        second_window.setCentralWidget(self.centralwidget)

        self.retranslateUi(second_window)
        QtCore.QMetaObject.connectSlotsByName(second_window)

    def retranslateUi(self, second_window):
        _translate = QtCore.QCoreApplication.translate
        second_window.setWindowTitle(_translate("second_window", "Govee Enterprise"))
        self.comboBox.setItemText(0, _translate("second_window", "Device 1"))
        self.comboBox.setItemText(1, _translate("second_window", "Device 2"))
        self.comboBox.setItemText(2, _translate("second_window", "Device 3"))
        self.comboBox.setItemText(3, _translate("second_window", "Device 4"))
        self.comboBox.setItemText(4, _translate("second_window", "Device 5"))
        self.comboBox.setItemText(5, _translate("second_window", "Device 6"))
        self.comboBox.setItemText(6, _translate("second_window", "Device 7"))
        self.comboBox.setItemText(7, _translate("second_window", "Device 8"))
        self.comboBox.setItemText(8, _translate("second_window", "Device 9"))
        self.comboBox.setItemText(9, _translate("second_window", "Device 10"))
        self.comboBox.setItemText(10, _translate("second_window", "Device 11"))
        self.comboBox.setItemText(11, _translate("second_window", "Device 12"))
        self.comboBox.setItemText(12, _translate("second_window", "Device 13"))
        self.comboBox.setItemText(13, _translate("second_window", "Device 14"))
        self.comboBox.setItemText(14, _translate("second_window", "Device 15"))
        self.comboBox.setItemText(15, _translate("second_window", "Device 16"))
        self.comboBox.setItemText(16, _translate("second_window", "Device 20"))
        self.comboBox.setItemText(17, _translate("second_window", "Device 21"))
        self.comboBox.setItemText(18, _translate("second_window", "Device 22"))
        self.comboBox.setItemText(19, _translate("second_window", "Device 23"))
        self.comboBox.setItemText(20, _translate("second_window", "Device 24"))
        self.comboBox.setItemText(21, _translate("second_window", "Device 25"))
        self.comboBox.setItemText(22, _translate("second_window", "Device 26"))
        self.comboBox.setItemText(23, _translate("second_window", "Device 27"))
        self.comboBox.setItemText(24, _translate("second_window", "Device 28"))
        self.comboBox.setItemText(25, _translate("second_window", "Device 29"))
        self.comboBox.setItemText(26, _translate("second_window", "Device 30"))
        self.comboBox.setItemText(27, _translate("second_window", "Device 31"))
        self.comboBox.setItemText(28, _translate("second_window", "Device 32"))
        self.comboBox.setItemText(29, _translate("second_window", "Device 33"))
        self.comboBox.setItemText(30, _translate("second_window", "Device 34"))
        self.comboBox.setItemText(31, _translate("second_window", "Device 35"))
        self.comboBox.setItemText(32, _translate("second_window", "Device 36"))
        self.comboBox.setItemText(33, _translate("second_window", "Device 37"))
        self.comboBox.setItemText(34, _translate("second_window", "Device 38"))
        self.comboBox.setItemText(35, _translate("second_window", "Device 39"))
        self.comboBox.setItemText(36, _translate("second_window", "Device 40"))
        self.comboBox.setItemText(37, _translate("second_window", "Device 41"))
        self.comboBox.setItemText(38, _translate("second_window", "Device 42"))
        self.comboBox.setItemText(39, _translate("second_window", "Device 43"))
        self.comboBox.setItemText(40, _translate("second_window", "Device 44"))
        self.comboBox.setItemText(41, _translate("second_window", "Device 45"))
        self.comboBox.setItemText(42, _translate("second_window", "Device 46"))
        self.comboBox.setItemText(43, _translate("second_window", "Device 47"))
        self.comboBox.setItemText(44, _translate("second_window", "Device 48"))
        self.comboBox.setItemText(45, _translate("second_window", "Device 49"))
        self.comboBox.setItemText(46, _translate("second_window", "Device 50"))
        self.comboBox.setItemText(47, _translate("second_window", "Device 51"))
        self.comboBox.setItemText(48, _translate("second_window", "Device 52"))
        self.comboBox.setItemText(49, _translate("second_window", "Device 53"))
        self.comboBox.setItemText(50, _translate("second_window", "Device 54"))
        self.comboBox.setItemText(51, _translate("second_window", "Device 55"))
        self.comboBox.setItemText(52, _translate("second_window", "Device 56"))
        self.comboBox.setItemText(53, _translate("second_window", "Device 57"))
        self.comboBox.setItemText(54, _translate("second_window", "Device 58"))
        self.comboBox.setItemText(55, _translate("second_window", "Device 59"))
        self.comboBox.setItemText(56, _translate("second_window", "Device 60"))
        self.comboBox.setItemText(57, _translate("second_window", "Device 61"))
        self.comboBox.setItemText(58, _translate("second_window", "Device 62"))
        self.comboBox.setItemText(59, _translate("second_window", "Device 63"))
        self.comboBox.setItemText(60, _translate("second_window", "Device 64"))
        self.comboBox.setItemText(61, _translate("second_window", "Device 65"))
        self.comboBox.setItemText(62, _translate("second_window", "Device 66"))
        self.comboBox.setItemText(63, _translate("second_window", "Device 67"))
        self.comboBox.setItemText(64, _translate("second_window", "Device 68"))
        self.comboBox.setItemText(65, _translate("second_window", "Device 69"))
        self.comboBox.setItemText(66, _translate("second_window", "Device 70"))
        self.comboBox.setItemText(67, _translate("second_window", "Device 71"))
        self.comboBox.setItemText(68, _translate("second_window", "Device 72"))
        self.comboBox.setItemText(69, _translate("second_window", "Device 73"))
        self.comboBox.setItemText(70, _translate("second_window", "Device 74"))
        self.comboBox.setItemText(71, _translate("second_window", "Device 75"))
        self.comboBox.setItemText(72, _translate("second_window", "Device 76"))
        self.comboBox.setItemText(73, _translate("second_window", "Device 77"))
        self.comboBox.setItemText(74, _translate("second_window", "Device 78"))
        self.comboBox.setItemText(75, _translate("second_window", "Device 79"))
        self.comboBox.setItemText(76, _translate("second_window", "Device 80"))
        self.comboBox.setItemText(77, _translate("second_window", "Device 81"))
        self.comboBox.setItemText(78, _translate("second_window", "Device 82"))
        self.comboBox.setItemText(79, _translate("second_window", "Device 83"))
        self.comboBox.setItemText(80, _translate("second_window", "Device 84"))
        self.comboBox.setItemText(81, _translate("second_window", "Device 85"))
        self.comboBox.setItemText(82, _translate("second_window", "Device 86"))
        self.comboBox.setItemText(83, _translate("second_window", "Device 87"))
        self.comboBox.setItemText(84, _translate("second_window", "Device 88"))
        self.comboBox.setItemText(84, _translate("second_window", "Device 89"))
        self.comboBox.setItemText(85, _translate("second_window", "Device 90"))
        self.comboBox.setItemText(86, _translate("second_window", "Device 91"))
        self.comboBox.setItemText(87, _translate("second_window", "Device 92"))
        self.comboBox.setItemText(88, _translate("second_window", "Device 93"))
        self.comboBox.setItemText(89, _translate("second_window", "Device 94"))
        self.comboBox.setItemText(90, _translate("second_window", "Device 95"))
        self.comboBox.setItemText(91, _translate("second_window", "Device 96"))
        self.comboBox.setItemText(92, _translate("second_window", "Device 97"))
        self.comboBox.setItemText(93, _translate("second_window", "Device 98"))


        self.label.setText(_translate("second_window", "Select Device  :"))
        self.label_2.setText(_translate("second_window", "Govee "))

        self.pushButton.setText(_translate("second_window", "Show"))
        self.pushButton_2.setText(_translate("second_window", "Export"))

        self.comboBox_2.setItemText(0, _translate("second_window", "Day"))
        self.comboBox_2.setItemText(1, _translate("second_window", "Week"))
        self.comboBox_2.setItemText(2, _translate("second_window", "Month"))
        self.comboBox_2.setItemText(3, _translate("second_window", "Year"))
        self.label_3.setText(_translate("second_window", "Select Date     :"))
        self.pushButton_3.setText(_translate("second_window", "Alarms"))
        self.pushButton_4.setText(_translate("second_window", "Status"))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    second_window = QtWidgets.QMainWindow()
    ui = Ui_second_window()
    ui.setupUi(second_window)
    second_window.show()
    sys.exit(app.exec_())
