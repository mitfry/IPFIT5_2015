
#!/usr/bin/env python

# IPFIT5 imports
# Built-in
import sys
import time

# Add folder "functions" to the locations to import from
sys.path.append(sys.path[0]+"/../functions")

# Custom
import Software
import Hardware

# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Development\School\IPFIT5_2015\source\gui\gui_maken\interface_thram.ui'
#
# Created: Fri Jun 05 19:23:43 2015
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
        MainWindow.resize(720, 567)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.gridLayout_3 = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout_3.setObjectName(_fromUtf8("gridLayout_3"))
        self.progressBar = QtGui.QProgressBar(self.centralwidget)
        self.progressBar.setMouseTracking(True)
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName(_fromUtf8("progressBar"))
        self.gridLayout_3.addWidget(self.progressBar, 1, 0, 1, 1)
        self.tab_Menu = QtGui.QTabWidget(self.centralwidget)
        self.tab_Menu.setObjectName(_fromUtf8("tab_Menu"))
        self.tab_Project = QtGui.QWidget()
        self.tab_Project.setObjectName(_fromUtf8("tab_Project"))
        self.gridLayout_6 = QtGui.QGridLayout(self.tab_Project)
        self.gridLayout_6.setObjectName(_fromUtf8("gridLayout_6"))
        self.btn_Test = QtGui.QPushButton(self.tab_Project)
        self.btn_Test.setObjectName(_fromUtf8("btn_Test"))
        self.gridLayout_6.addWidget(self.btn_Test, 0, 0, 1, 1)
        self.btn_Progressbar = QtGui.QPushButton(self.tab_Project)
        self.btn_Progressbar.setObjectName(_fromUtf8("btn_Progressbar"))
        self.gridLayout_6.addWidget(self.btn_Progressbar, 1, 0, 1, 1)
        self.tab_Menu.addTab(self.tab_Project, _fromUtf8(""))
        self.tab_System = QtGui.QWidget()
        self.tab_System.setObjectName(_fromUtf8("tab_System"))
        self.gridLayout_2 = QtGui.QGridLayout(self.tab_System)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.btn_Hardware = QtGui.QPushButton(self.tab_System)
        self.btn_Hardware.setObjectName(_fromUtf8("btn_Hardware"))
        self.gridLayout_2.addWidget(self.btn_Hardware, 0, 0, 1, 1)
        self.tab_Menu.addTab(self.tab_System, _fromUtf8(""))
        self.tab_Software = QtGui.QWidget()
        self.tab_Software.setObjectName(_fromUtf8("tab_Software"))
        self.gridLayout = QtGui.QGridLayout(self.tab_Software)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.btn_Processen = QtGui.QPushButton(self.tab_Software)
        self.btn_Processen.setObjectName(_fromUtf8("btn_Processen"))
        self.gridLayout.addWidget(self.btn_Processen, 0, 0, 1, 1)
        self.btn_Services = QtGui.QPushButton(self.tab_Software)
        self.btn_Services.setObjectName(_fromUtf8("btn_Services"))
        self.gridLayout.addWidget(self.btn_Services, 0, 1, 1, 1)
        self.btn_Software = QtGui.QPushButton(self.tab_Software)
        self.btn_Software.setObjectName(_fromUtf8("btn_Software"))
        self.gridLayout.addWidget(self.btn_Software, 0, 2, 1, 1)
        self.treeWidget = QtGui.QTreeWidget(self.tab_Software)
        self.treeWidget.setAlternatingRowColors(False)
        self.treeWidget.setObjectName(_fromUtf8("treeWidget"))
        self.gridLayout.addWidget(self.treeWidget, 1, 0, 1, 3)
        self.tab_Menu.addTab(self.tab_Software, _fromUtf8(""))
        self.tab_Internet = QtGui.QWidget()
        self.tab_Internet.setObjectName(_fromUtf8("tab_Internet"))
        self.gridLayout_5 = QtGui.QGridLayout(self.tab_Internet)
        self.gridLayout_5.setObjectName(_fromUtf8("gridLayout_5"))
        self.btn_Internet_History = QtGui.QPushButton(self.tab_Internet)
        self.btn_Internet_History.setObjectName(_fromUtf8("btn_Internet_History"))
        self.gridLayout_5.addWidget(self.btn_Internet_History, 0, 0, 1, 1)
        self.tab_Menu.addTab(self.tab_Internet, _fromUtf8(""))
        self.tab_Email = QtGui.QWidget()
        self.tab_Email.setObjectName(_fromUtf8("tab_Email"))
        self.gridLayout_4 = QtGui.QGridLayout(self.tab_Email)
        self.gridLayout_4.setObjectName(_fromUtf8("gridLayout_4"))
        self.btn_Email = QtGui.QPushButton(self.tab_Email)
        self.btn_Email.setObjectName(_fromUtf8("btn_Email"))
        self.gridLayout_4.addWidget(self.btn_Email, 0, 0, 1, 1)
        self.tab_Menu.addTab(self.tab_Email, _fromUtf8(""))
        self.tab_Files = QtGui.QWidget()
        self.tab_Files.setObjectName(_fromUtf8("tab_Files"))
        self.formLayout = QtGui.QFormLayout(self.tab_Files)
        self.formLayout.setFieldGrowthPolicy(QtGui.QFormLayout.AllNonFixedFieldsGrow)
        self.formLayout.setObjectName(_fromUtf8("formLayout"))
        self.lbl_Live_Search = QtGui.QLabel(self.tab_Files)
        self.lbl_Live_Search.setObjectName(_fromUtf8("lbl_Live_Search"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.FieldRole, self.lbl_Live_Search)
        self.txt_Live_Search = QtGui.QLineEdit(self.tab_Files)
        self.txt_Live_Search.setObjectName(_fromUtf8("txt_Live_Search"))
        self.formLayout.setWidget(3, QtGui.QFormLayout.FieldRole, self.txt_Live_Search)
        self.btn_Hash = QtGui.QPushButton(self.tab_Files)
        self.btn_Hash.setObjectName(_fromUtf8("btn_Hash"))
        self.formLayout.setWidget(4, QtGui.QFormLayout.FieldRole, self.btn_Hash)
        self.tab_Menu.addTab(self.tab_Files, _fromUtf8(""))
        self.gridLayout_3.addWidget(self.tab_Menu, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 720, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuBestand = QtGui.QMenu(self.menubar)
        self.menuBestand.setObjectName(_fromUtf8("menuBestand"))
        self.menuOpties = QtGui.QMenu(self.menubar)
        self.menuOpties.setObjectName(_fromUtf8("menuOpties"))
        self.menuHelp = QtGui.QMenu(self.menubar)
        self.menuHelp.setObjectName(_fromUtf8("menuHelp"))
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
        self.actionInfo = QtGui.QAction(MainWindow)
        self.actionInfo.setObjectName(_fromUtf8("actionInfo"))
        self.actionTechnical_manual = QtGui.QAction(MainWindow)
        self.actionTechnical_manual.setObjectName(_fromUtf8("actionTechnical_manual"))
        self.actionOver = QtGui.QAction(MainWindow)
        self.actionOver.setObjectName(_fromUtf8("actionOver"))
        self.menuBestand.addAction(self.actionNieuw)
        self.menuBestand.addAction(self.actionOpen)
        self.menuBestand.addAction(self.actionOpslaan)
        self.menuOpties.addAction(self.actionFuncties)
        self.menuHelp.addAction(self.actionInfo)
        self.menuHelp.addAction(self.actionTechnical_manual)
        self.menuHelp.addAction(self.actionOver)
        self.menubar.addAction(self.menuBestand.menuAction())
        self.menubar.addAction(self.menuOpties.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(MainWindow)
        self.tab_Menu.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.btn_Test.setText(_translate("MainWindow", "Test mijn functie", None))
        self.btn_Progressbar.setText(_translate("MainWindow", "Start", None))
        self.tab_Menu.setTabText(self.tab_Menu.indexOf(self.tab_Project), _translate("MainWindow", "Project", None))
        self.btn_Hardware.setText(_translate("MainWindow", "Hardware Info", None))
        self.tab_Menu.setTabText(self.tab_Menu.indexOf(self.tab_System), _translate("MainWindow", "Systeem", None))
        self.btn_Processen.setText(_translate("MainWindow", "Processen", None))
        self.btn_Services.setText(_translate("MainWindow", "Services", None))
        self.btn_Software.setText(_translate("MainWindow", "Software", None))
        self.treeWidget.headerItem().setText(0, _translate("MainWindow", "ProcesID", None))
        self.treeWidget.headerItem().setText(1, _translate("MainWindow", "Naam", None))
        self.tab_Menu.setTabText(self.tab_Menu.indexOf(self.tab_Software), _translate("MainWindow", "Software", None))
        self.btn_Internet_History.setText(_translate("MainWindow", "Internetgeschiedenis", None))
        self.tab_Menu.setTabText(self.tab_Menu.indexOf(self.tab_Internet), _translate("MainWindow", "Internet", None))
        self.btn_Email.setText(_translate("MainWindow", "E-mail", None))
        self.tab_Menu.setTabText(self.tab_Menu.indexOf(self.tab_Email), _translate("MainWindow", "E-mail", None))
        self.lbl_Live_Search.setText(_translate("MainWindow", "Live Search...", None))
        self.btn_Hash.setText(_translate("MainWindow", "Hash...", None))
        self.tab_Menu.setTabText(self.tab_Menu.indexOf(self.tab_Files), _translate("MainWindow", "Bestanden", None))
        self.menuBestand.setTitle(_translate("MainWindow", "Bestand", None))
        self.menuOpties.setTitle(_translate("MainWindow", "Opties", None))
        self.menuHelp.setTitle(_translate("MainWindow", "Help", None))
        self.actionNieuw.setText(_translate("MainWindow", "Nieuw...", None))
        self.actionOpen.setText(_translate("MainWindow", "Open...", None))
        self.actionOpslaan.setText(_translate("MainWindow", "Opslaan...", None))
        self.actionFuncties.setText(_translate("MainWindow", "Functies", None))
        self.actionInfo.setText(_translate("MainWindow", "Gebruikershandleiding", None))
        self.actionTechnical_manual.setText(_translate("MainWindow", "Technische handleiding", None))
        self.actionOver.setText(_translate("MainWindow", "Over", None))


       # IPFIT5 functions and other code
        self.btn_Test.clicked.connect(Hardware.printTekst)
        self.btn_Processen.clicked.connect(Software.processes)
        self.btn_Services.clicked.connect(Software.services)
        self.btn_Hash.clicked.connect(self.printTekst4)
        self.btn_Software.clicked.connect(Software.software_installed)
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
