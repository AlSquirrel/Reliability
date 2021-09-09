# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Hot_sparing.ui'
#
# Created by: PyQt5 UI code generator 5.7
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
import math
import numpy as np

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setWindowIcon(QtGui.QIcon('icon.png'))
        MainWindow.resize(511, 464)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(20, 20, 471, 411))
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.doubleSpinBox_7 = QtWidgets.QDoubleSpinBox(self.tab)
        self.doubleSpinBox_7.setGeometry(QtCore.QRect(50, 60, 91, 22))
        self.doubleSpinBox_7.setAlignment(QtCore.Qt.AlignCenter)
        self.doubleSpinBox_7.setDecimals(0)
        self.doubleSpinBox_7.setMaximum(10000000000.0)
        self.doubleSpinBox_7.setProperty("value", 40000.0)
        self.doubleSpinBox_7.setObjectName("doubleSpinBox_7")
        self.doubleSpinBox_8 = QtWidgets.QDoubleSpinBox(self.tab)
        self.doubleSpinBox_8.setGeometry(QtCore.QRect(50, 130, 91, 22))
        self.doubleSpinBox_8.setAlignment(QtCore.Qt.AlignCenter)
        self.doubleSpinBox_8.setDecimals(1)
        self.doubleSpinBox_8.setMaximum(5000.0)
        self.doubleSpinBox_8.setProperty("value", 1440.0)
        self.doubleSpinBox_8.setObjectName("doubleSpinBox_8")
        self.doubleSpinBox_9 = QtWidgets.QDoubleSpinBox(self.tab)
        self.doubleSpinBox_9.setGeometry(QtCore.QRect(50, 200, 91, 22))
        self.doubleSpinBox_9.setAlignment(QtCore.Qt.AlignCenter)
        self.doubleSpinBox_9.setDecimals(0)
        self.doubleSpinBox_9.setProperty("value", 10.0)
        self.doubleSpinBox_9.setObjectName("doubleSpinBox_9")
        self.doubleSpinBox_10 = QtWidgets.QDoubleSpinBox(self.tab)
        self.doubleSpinBox_10.setGeometry(QtCore.QRect(50, 270, 91, 22))
        self.doubleSpinBox_10.setAlignment(QtCore.Qt.AlignCenter)
        self.doubleSpinBox_10.setDecimals(0)
        self.doubleSpinBox_10.setProperty("value", 1.0)
        self.doubleSpinBox_10.setObjectName("doubleSpinBox_10")
        self.pushButton_2 = QtWidgets.QPushButton(self.tab)
        self.pushButton_2.setGeometry(QtCore.QRect(180, 160, 101, 23))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.clicked.connect(self.on_clicked_red)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.tab)
        self.lineEdit_2.setGeometry(QtCore.QRect(310, 90, 113, 20))
        self.lineEdit_2.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.tab)
        self.lineEdit_3.setGeometry(QtCore.QRect(310, 160, 113, 20))
        self.lineEdit_3.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.lineEdit_4 = QtWidgets.QLineEdit(self.tab)
        self.lineEdit_4.setGeometry(QtCore.QRect(310, 230, 113, 20))
        self.lineEdit_4.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.label = QtWidgets.QLabel(self.tab)
        self.label.setGeometry(QtCore.QRect(30, 30, 131, 31))
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.tab)
        self.label_2.setGeometry(QtCore.QRect(30, 100, 131, 31))
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.tab)
        self.label_3.setGeometry(QtCore.QRect(30, 170, 131, 31))
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.tab)
        self.label_4.setGeometry(QtCore.QRect(30, 240, 131, 31))
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.tab)
        self.label_5.setGeometry(QtCore.QRect(300, 60, 131, 31))
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.tab)
        self.label_6.setGeometry(QtCore.QRect(300, 130, 131, 31))
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.tab)
        self.label_7.setGeometry(QtCore.QRect(300, 200, 131, 31))
        self.label_7.setAlignment(QtCore.Qt.AlignCenter)
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.tab)
        self.label_8.setGeometry(QtCore.QRect(280, 20, 171, 31))
        self.label_8.setAlignment(QtCore.Qt.AlignCenter)
        self.label_8.setObjectName("label_8")
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.doubleSpinBox = QtWidgets.QDoubleSpinBox(self.tab_2)
        self.doubleSpinBox.setGeometry(QtCore.QRect(65, 40, 111, 22))
        self.doubleSpinBox.setAlignment(QtCore.Qt.AlignCenter)
        self.doubleSpinBox.setDecimals(0)
        self.doubleSpinBox.setMaximum(10000000000.0)
        self.doubleSpinBox.setSingleStep(10.0)
        self.doubleSpinBox.setProperty("value", 40000.0)
        self.doubleSpinBox.setObjectName("doubleSpinBox")
        self.doubleSpinBox_22 = QtWidgets.QDoubleSpinBox(self.tab_2)
        self.doubleSpinBox_22.setGeometry(QtCore.QRect(65, 100, 111, 22))
        self.doubleSpinBox_22.setAlignment(QtCore.Qt.AlignCenter)
        self.doubleSpinBox_22.setDecimals(1)
        self.doubleSpinBox_22.setMaximum(100.0)
        self.doubleSpinBox_22.setSingleStep(0.5)
        self.doubleSpinBox_22.setProperty("value", 0.5)
        self.doubleSpinBox_22.setObjectName("doubleSpinBox_22")
        self.doubleSpinBox_33 = QtWidgets.QDoubleSpinBox(self.tab_2)
        self.doubleSpinBox_33.setGeometry(QtCore.QRect(65, 160, 111, 22))
        self.doubleSpinBox_33.setAlignment(QtCore.Qt.AlignCenter)
        self.doubleSpinBox_33.setDecimals(8)
        self.doubleSpinBox_33.setMaximum(1.0)
        self.doubleSpinBox_33.setSingleStep(0.001)
        self.doubleSpinBox_33.setProperty("value", 2.5e-05)
        self.doubleSpinBox_33.setObjectName("doubleSpinBox_33")
        self.doubleSpinBox_44 = QtWidgets.QDoubleSpinBox(self.tab_2)
        self.doubleSpinBox_44.setGeometry(QtCore.QRect(65, 220, 111, 22))
        self.doubleSpinBox_44.setAlignment(QtCore.Qt.AlignCenter)
        self.doubleSpinBox_44.setDecimals(0)
        self.doubleSpinBox_44.setMinimum(1.0)
        self.doubleSpinBox_44.setMaximum(200.0)
        self.doubleSpinBox_44.setProperty("value", 2.0)
        self.doubleSpinBox_44.setObjectName("doubleSpinBox_44")
        self.doubleSpinBox_55 = QtWidgets.QDoubleSpinBox(self.tab_2)
        self.doubleSpinBox_55.setGeometry(QtCore.QRect(65, 280, 111, 22))
        self.doubleSpinBox_55.setAlignment(QtCore.Qt.AlignCenter)
        self.doubleSpinBox_55.setDecimals(0)
        self.doubleSpinBox_55.setMaximum(4500.0)
        self.doubleSpinBox_55.setProperty("value", 1440.0)
        self.doubleSpinBox_55.setObjectName("doubleSpinBox_55")
        self.doubleSpinBox_66 = QtWidgets.QDoubleSpinBox(self.tab_2)
        self.doubleSpinBox_66.setGeometry(QtCore.QRect(65, 340, 111, 22))
        self.doubleSpinBox_66.setAlignment(QtCore.Qt.AlignCenter)
        self.doubleSpinBox_66.setDecimals(0)
        self.doubleSpinBox_66.setMinimum(1.0)
        self.doubleSpinBox_66.setProperty("value", 1.0)
        self.doubleSpinBox_66.setObjectName("doubleSpinBox_66")
        self.doubleSpinBox_77 = QtWidgets.QDoubleSpinBox(self.tab_2)
        self.doubleSpinBox_77.setGeometry(QtCore.QRect(290, 40, 111, 22))
        self.doubleSpinBox_77.setAlignment(QtCore.Qt.AlignCenter)
        self.doubleSpinBox_77.setDecimals(0)
        self.doubleSpinBox_77.setMaximum(20.0)
        self.doubleSpinBox_77.setSingleStep(1.0)
        self.doubleSpinBox_77.setProperty("value", 1)
        self.doubleSpinBox_77.setObjectName("doubleSpinBox_77")
        self.doubleSpinBox_88 = QtWidgets.QDoubleSpinBox(self.tab_2)
        self.doubleSpinBox_88.setGeometry(QtCore.QRect(290, 100, 111, 22))
        self.doubleSpinBox_88.setAlignment(QtCore.Qt.AlignCenter)
        self.doubleSpinBox_88.setDecimals(0)
        self.doubleSpinBox_88.setMaximum(100)
        self.doubleSpinBox_88.setSingleStep(1.0)
        self.doubleSpinBox_88.setProperty("value", 1)
        self.doubleSpinBox_88.setObjectName("doubleSpinBox_88")
        self.lineEdit = QtWidgets.QLineEdit(self.tab_2)
        self.lineEdit.setGeometry(QtCore.QRect(290, 190, 113, 20))
        self.lineEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit.setObjectName("lineEdit")
        self.pushButtonZ = QtWidgets.QPushButton(self.tab_2)
        self.pushButtonZ.setGeometry(QtCore.QRect(290, 300, 111, 22))
        self.pushButtonZ.setObjectName("pushButtonZ")
        self.pushButtonZ.clicked.connect(self.on_clicked_rep)
        self.pushButtonZ.setCheckable(True)
        self.label_9 = QtWidgets.QLabel(self.tab_2)
        self.label_9.setGeometry(QtCore.QRect(20, 10, 201, 31))
        self.label_9.setAlignment(QtCore.Qt.AlignCenter)
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(self.tab_2)
        self.label_10.setGeometry(QtCore.QRect(20, 70, 201, 31))
        self.label_10.setAlignment(QtCore.Qt.AlignCenter)
        self.label_10.setObjectName("label_10")
        self.label_11 = QtWidgets.QLabel(self.tab_2)
        self.label_11.setGeometry(QtCore.QRect(20, 130, 201, 31))
        self.label_11.setAlignment(QtCore.Qt.AlignCenter)
        self.label_11.setObjectName("label_11")
        self.label_12 = QtWidgets.QLabel(self.tab_2)
        self.label_12.setGeometry(QtCore.QRect(20, 190, 201, 31))
        self.label_12.setAlignment(QtCore.Qt.AlignCenter)
        self.label_12.setObjectName("label_12")
        self.label_13 = QtWidgets.QLabel(self.tab_2)
        self.label_13.setGeometry(QtCore.QRect(20, 250, 201, 31))
        self.label_13.setAlignment(QtCore.Qt.AlignCenter)
        self.label_13.setObjectName("label_13")
        self.label_14 = QtWidgets.QLabel(self.tab_2)
        self.label_14.setGeometry(QtCore.QRect(20, 310, 201, 31))
        self.label_14.setAlignment(QtCore.Qt.AlignCenter)
        self.label_14.setObjectName("label_14")
        self.label_15 = QtWidgets.QLabel(self.tab_2)
        self.label_15.setGeometry(QtCore.QRect(250, 160, 191, 31))
        self.label_15.setAlignment(QtCore.Qt.AlignCenter)
        self.label_15.setObjectName("label_15")
        self.label_16 = QtWidgets.QLabel(self.tab_2)
        self.label_16.setGeometry(QtCore.QRect(250, 10, 181, 31))
        self.label_16.setAlignment(QtCore.Qt.AlignCenter)
        self.label_16.setObjectName("label_16")
        self.label_17 = QtWidgets.QLabel(self.tab_2)
        self.label_17.setGeometry(QtCore.QRect(250, 70, 181, 31))
        self.label_17.setAlignment(QtCore.Qt.AlignCenter)
        self.label_17.setObjectName("label_17")
        self.label_pic = QtWidgets.QLabel(self.tab_2)
        self.label_pic.setGeometry(QtCore.QRect(240, 250, 220, 65))
        self.label_pic.setObjectName("label_pic")
        pixmap = QtGui.QPixmap('Label_mini.png')
        self.label_pic.setPixmap(pixmap)
        self.label_pic.show()
        self.tabWidget.addTab(self.tab_2, "")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Надёжность при горячем резервировании"))
        self.pushButton_2.setText(_translate("MainWindow", "РАССЧИТАТЬ"))
        self.label.setText(_translate("MainWindow", "Наработка \n"
"до отказа, час"))
        self.label_2.setText(_translate("MainWindow", "Время\n"
"восстановления, час"))
        self.label_3.setText(_translate("MainWindow", "Количество\n"
"рабочих единиц"))
        self.label_4.setText(_translate("MainWindow", "Количество\n"
"резервных единиц"))
        self.label_5.setText(_translate("MainWindow", "Наработка \n"
"до отказа, час"))
        self.label_6.setText(_translate("MainWindow", "Время \n"
"восстановления, час"))
        self.label_7.setText(_translate("MainWindow", "Показатель гамма"))
        self.label_8.setText(_translate("MainWindow", "ХАРАКТЕРИСТИКИ НАДЕЖНОСТИ \n"
"ГРУППЫ"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Резервирование с горячим резервом"))
        self.pushButtonZ.setText(_translate("MainWindow", "РАССЧИТАТЬ"))
        self.label_9.setText(_translate("MainWindow", "Средняя наработка на отказ\n"
" устройства в резервной группе, час"))
        self.label_10.setText(_translate("MainWindow", "Среднее время восстановления\n"
"(замены)элемента при наличии ЗИП,час"))
        self.label_11.setText(_translate("MainWindow", "Средняя интенсивность отказов\n"
" элементов в рабочем режиме, 1/час"))
        self.label_12.setText(_translate("MainWindow", "Количество восстанавливаемых\n"
" элементов в группе"))
        self.label_13.setText(_translate("MainWindow", "Среднее время восстановления\n"
" элемента, час"))
        self.label_14.setText(_translate("MainWindow", "Количество запасных элементов"))
        self.label_15.setText(_translate("MainWindow", "Коэффициент готовности\n"
" ЗИП по данному элементу"))
        self.label_16.setText(_translate("MainWindow", "Количество резервных элементов\n"
"в резервированной группе"))
        self.label_17.setText(_translate("MainWindow", "Количество одинаковых\n"
"резервированных групп"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "ЗИП с горячим резервом"))


    def on_clicked_red(self):
        mttr = self.doubleSpinBox_8.value()
        mtbf = self.doubleSpinBox_7.value()
        k = self.doubleSpinBox_9.value()
        n = self.doubleSpinBox_10.value()
        g, T, tau = hot_reserv(mttr,mtbf,k,n+k)
        s = "%.6g"%T
        self.lineEdit_2.setText(s)
        s = "%.3g"%tau
        self.lineEdit_3.setText(s)
        s = "%.4g"%g
        self.lineEdit_4.setText(s)

    def on_clicked_rep(self):
        T_o = self.doubleSpinBox.value()
        T_v = self.doubleSpinBox_22.value()
        l = self.doubleSpinBox_33.value()
        m = self.doubleSpinBox_44.value()
        t_v = self.doubleSpinBox_55.value()
        n = self.doubleSpinBox_66.value()
        sigma = T_v/T_o
        redund = self.doubleSpinBox_77.value()
        NGr = self.doubleSpinBox_88.value()
        k = m-redund
##        alfa = sigma**2*(k+1)*(k+2)+sigma*(k+2)+1
##        beta = sigma**3*k*(k+1)*(k+2)
        gamma = gamma_arbitrarily(k,redund,sigma)
        ##        gamma = k*sigma*(k+1)*(sigma+k*sigma+2)/(sigma+k*sigma+1)/((k**2+k)*sigma**2+(k+1)*sigma+1)# 1 резервный
        #gamma = beta*(alfa+sigma*(k+2)+2)/sigma/(alfa+beta)/alfa # k рабочих и 2 резервных
        P = l*t_v*func_q(m,l,t_v,n)*NGr*gamma*1
        print(func_q(m,l,t_v,n))
        s = "%.16g"%(1-P)
        print(s)
        self.lineEdit.setText(s)

def gamma_arbitrarily(work,redund,sigma):
    product = [1]
    s1, s2 = 0, 0
    for i in range(1,int(redund)+2):
        product.append(product[-1]*(work+i-1))
        s1 = s1 + i/product[-1]/(sigma**i)
        s2 = s2 + 1/product[-1]/(sigma**i)
    return s1/sigma/(s2+1)/s2

def hot_reserv(mttr,mtbf,k,N):
    from math import factorial
    g_el = mttr/mtbf
    N = round(N); k = round(k);
    n = N-k
    CN_n = factorial(N)//factorial(n+1)//factorial(N-n-1)
    s = 0
    for i in range(n+1):
        s += factorial(N)//factorial(i)//factorial(N-i)*g_el**i
    g = CN_n*(g_el**(n+1))/s
    CN_k = factorial(N)//factorial(k)//factorial(N-k)
    T = mtbf/k/CN_k/(g_el**n)*s
    tau = 1/(n+1)*mttr
    return g, T, tau

def func_q(m,l,t_v,n):
    ss = 0
    p = np.arange(0,n+1)
    for i in p:
        ss = ss+(m*l*t_v)**i/math.factorial(i)
    if (ss == 0) or ((m*l*t_v)**n/ss/math.factorial(n) > 1):
        q = 1
    else:
        q = (m*l*t_v)**n/ss/math.factorial(n)
    return q


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

