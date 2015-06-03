# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'interface_thram.ui'
#
# Created: Mon Jun 01 22:14:14 2015
#      by: PyQt4 UI code generator 4.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
import sys

from source.functions import Software
from source.functions import Hardware

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8

    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)


class Ui_MainWindow(QtGui.QMainWindow):
    def __init__(self):
        QtGui.QMainWindow.__init__(self)
        self.setupUi(self)

    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(755, 477)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.gridLayout_3 = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout_3.setObjectName(_fromUtf8("gridLayout_3"))
        self.pushButton_2 = QtGui.QPushButton(self.centralwidget)
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.gridLayout_3.addWidget(self.pushButton_2, 0, 1, 1, 1)
        self.pushButton = QtGui.QPushButton(self.centralwidget)
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.gridLayout_3.addWidget(self.pushButton, 0, 0, 1, 1)
        self.pushButton_4 = QtGui.QPushButton(self.centralwidget)
        self.pushButton_4.setObjectName(_fromUtf8("pushButton_4"))
        self.gridLayout_3.addWidget(self.pushButton_4, 2, 0, 1, 1)
        self.pushButton_3 = QtGui.QPushButton(self.centralwidget)
        self.pushButton_3.setObjectName(_fromUtf8("pushButton_3"))
        self.gridLayout_3.addWidget(self.pushButton_3, 0, 2, 1, 1)
        self.pushButton_5 = QtGui.QPushButton(self.centralwidget)
        self.pushButton_5.setObjectName(_fromUtf8("pushButton_5"))
        self.gridLayout_3.addWidget(self.pushButton_5, 2, 1, 1, 1)
        self.pushButton_6 = QtGui.QPushButton(self.centralwidget)
        self.pushButton_6.setObjectName(_fromUtf8("pushButton_6"))
        self.gridLayout_3.addWidget(self.pushButton_6, 2, 2, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 755, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuBestand = QtGui.QMenu(self.menubar)
        self.menuBestand.setObjectName(_fromUtf8("menuBestand"))
        self.menuOpties = QtGui.QMenu(self.menubar)
        self.menuOpties.setObjectName(_fromUtf8("menuOpties"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        self.actionNieuw = QtGui.QAction(MainWindow)
        self.actionNieuw.setObjectName(_fromUtf8("actionNieuw"))
        self.actionOpen = QtGui.QAction(MainWindow)
        self.actionOpen.setObjectName(_fromUtf8("actionOpen"))
        self.actionOpslaan = QtGui.QAction(MainWindow)
        self.actionOpslaan.setObjectName(_fromUtf8("actionOpslaan"))
        self.actionFuncties = QtGui.QAction(MainWindow)
        self.actionFuncties.setObjectName(_fromUtf8("actionFuncties"))
        self.menuBestand.addAction(self.actionNieuw)
        self.menuBestand.addAction(self.actionOpen)
        self.menuBestand.addAction(self.actionOpslaan)
        self.menuOpties.addAction(self.actionFuncties)
        self.menubar.addAction(self.menuBestand.menuAction())
        self.menubar.addAction(self.menuOpties.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.pushButton.setText(_translate("MainWindow", "PushButton", None))
        self.pushButton_2.setText(_translate("MainWindow", "Tim", None))
        self.pushButton_4.setText(_translate("MainWindow", "Hugo", None))
        self.pushButton_3.setText(_translate("MainWindow", "Roland", None))
        self.pushButton_5.setText(_translate("MainWindow", "Andre", None))
        self.pushButton_6.setText(_translate("MainWindow", "Mitchell", None))
        self.menuBestand.setTitle(_translate("MainWindow", "Bestand", None))
        self.menuOpties.setTitle(_translate("MainWindow", "Opties", None))
        self.actionNieuw.setText(_translate("MainWindow", "Nieuw...", None))
        self.actionOpen.setText(_translate("MainWindow", "Open...", None))
        self.actionOpslaan.setText(_translate("MainWindow", "Opslaan...", None))
        self.actionFuncties.setText(_translate("MainWindow", "Functies", None))

        # Eigen functies
        self.pushButton.clicked.connect(Hardware.printTekst)
        self.pushButton_2.clicked.connect(Software.test)
        self.pushButton_3.clicked.connect(self.printTekst3)
        self.pushButton_4.clicked.connect(self.printTekst4)
        self.pushButton_5.clicked.connect(self.printTekst5)
        self.pushButton_6.clicked.connect(self.printTekst6)

    def printTekst2(self):
        print "Hallo Tim?!"

    def printTekst3(self):
        print "Hallo Roland?!"

    def printTekst4(self):
        print "Hallo Hugo?!"

    def printTekst5(self):
        print "Hallo Andre?!"

    def printTekst6(self):
        print "Hallo Mitchell?!"

        # Het is niet te geloven dames!


if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    ex = Ui_MainWindow()
    ex.show()
    sys.exit(app.exec_())
