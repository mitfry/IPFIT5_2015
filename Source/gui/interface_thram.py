
#!/usr/bin/env python

# IPFIT5 imports
import sys
import time


sys.path.append(sys.path[0]+"/../functions")



import Hardware
import Software
# from source.functions import Software
# from source.functions import Hardware


# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Development\School\IPFIT5_2015\source\gui\gui_maken\interface_thram.ui'
#
# Created: Thu Jun 04 01:47:06 2015
#      by: PyQt4 UI code generator 4.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

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
        self.btn_Services = QtGui.QPushButton(self.centralwidget)
        self.btn_Services.setObjectName(_fromUtf8("btn_Services"))
        self.gridLayout_3.addWidget(self.btn_Services, 0, 2, 1, 1)
        self.pushButton_5 = QtGui.QPushButton(self.centralwidget)
        self.pushButton_5.setObjectName(_fromUtf8("pushButton_5"))
        self.gridLayout_3.addWidget(self.pushButton_5, 2, 1, 1, 1)
        self.btn_Progressbar = QtGui.QPushButton(self.centralwidget)
        self.btn_Progressbar.setObjectName(_fromUtf8("btn_Progressbar"))
        self.gridLayout_3.addWidget(self.btn_Progressbar, 2, 2, 1, 1)
        self.btn_Processen = QtGui.QPushButton(self.centralwidget)
        self.btn_Processen.setObjectName(_fromUtf8("btn_Processen"))
        self.gridLayout_3.addWidget(self.btn_Processen, 0, 1, 1, 1)
        self.btn_Test = QtGui.QPushButton(self.centralwidget)
        self.btn_Test.setObjectName(_fromUtf8("btn_Test"))
        self.gridLayout_3.addWidget(self.btn_Test, 0, 0, 1, 1)
        self.hash_Btn = QtGui.QPushButton(self.centralwidget)
        self.hash_Btn.setObjectName(_fromUtf8("hash_Btn"))
        self.gridLayout_3.addWidget(self.hash_Btn, 2, 0, 1, 1)
        self.scrollArea = QtGui.QScrollArea(self.centralwidget)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName(_fromUtf8("scrollArea"))
        self.scrollAreaWidgetContents = QtGui.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 540, 358))
        self.scrollAreaWidgetContents.setObjectName(_fromUtf8("scrollAreaWidgetContents"))
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.gridLayout_3.addWidget(self.scrollArea, 3, 0, 1, 1)
        self.progressBar = QtGui.QProgressBar(self.centralwidget)
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName(_fromUtf8("progressBar"))
        self.gridLayout_3.addWidget(self.progressBar, 3, 2, 1, 1, QtCore.Qt.AlignRight|QtCore.Qt.AlignBottom)
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
        self.btn_Services.setText(_translate("MainWindow", "Services", None))
        self.pushButton_5.setText(_translate("MainWindow", "PushButton", None))
        self.btn_Progressbar.setText(_translate("MainWindow", "Start", None))
        self.btn_Processen.setText(_translate("MainWindow", "Processen", None))
        self.btn_Test.setText(_translate("MainWindow", "Test mijn functie", None))
        self.hash_Btn.setText(_translate("MainWindow", "Hash...", None))
        self.menuBestand.setTitle(_translate("MainWindow", "Bestand", None))
        self.menuOpties.setTitle(_translate("MainWindow", "Opties", None))
        self.actionNieuw.setText(_translate("MainWindow", "Nieuw...", None))
        self.actionOpen.setText(_translate("MainWindow", "Open...", None))
        self.actionOpslaan.setText(_translate("MainWindow", "Opslaan...", None))
        self.actionFuncties.setText(_translate("MainWindow", "Functies", None))


       # IPFIT5 functions and other code
        self.btn_Test.clicked.connect(Hardware.printTekst)
        self.btn_Processen.clicked.connect(Software.processes)
        self.btn_Services.clicked.connect(Software.services)
        self.hash_Btn.clicked.connect(self.printTekst4)
        self.pushButton_5.clicked.connect(self.printTekst5)
        self.btn_Progressbar.clicked.connect(self.update_progress)

        self._active = False
    def update_progress(self):
        if not self._active:
            self._active = True
            self.btn_Progressbar.setText('Stop')
            if self.progressBar.value() == self.progressBar.maximum():
                self.progressBar.reset()
            QtCore.QTimer.singleShot(0, self.startLoop)
        else:
            self._active = False

    def closeEvent(self, event):
        self._active = False

    def startLoop(self):
        while True:
            time.sleep(0.05)
            value = self.progressBar.value() + 1
            self.progressBar.setValue(value)
            QtGui.qApp.processEvents()
            if (not self._active or
                value >= self.progressBar.maximum()):
                break
        self.btn_Progressbar.setText('Start')
        self._active = False

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

# IPFIT5 constructor
if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    ex = Ui_MainWindow()
    ex.show()
    sys.exit(app.exec_())
