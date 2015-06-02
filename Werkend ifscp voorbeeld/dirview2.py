#!/usr/bin/python
# -*- coding: utf-8 -*-
#@PydevCodeAnalysisIgnore

"""
Programma die een directory tree toont en de 
mogelijkheid geeft bestanden te kopieren

author: Tim Duysens
last edited: 01-06-2015
Done = nee
"""

import sip
sip.setapi('QString', 2)
sip.setapi('QVariant', 2)

from PyQt4 import QtCore 
from PyQt4 import QtGui
import sys
import os.path

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


class DirView(QtGui.QWidget):
    def __init__(self):
        QtGui.QWidget.__init__(self)
        self.setupUi(self)

    def setupUi(self, Form):
        """
        treewid = Treeview van de directories
        
        label = "Kopieren van"
        label_2 = Kopieren naar"
        
        lineEdit = Tekstvak "Kopieren van" - Readonly
        lineEdit_2 = Tekstvak "Kopieren naar" - Readonly
        
        pushButton = Kopieren naar
        pushButton_2 = Kopieren van 
        pushButton_3 = Kopieren maar
        
        """

        self.iconf = QtGui.QIcon('!.ico') 
        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(720, 600)
        
        Form.setWindowIcon(self.iconf)
        
        self.gridLayout_2 = QtGui.QGridLayout(Form)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        
        self.model = QtGui.QDirModel()
        
#         Treeview dir
        
        self.treewid = QtGui.QTreeView()
        self.treewid.setObjectName(_fromUtf8("treewid"))
        self.treewid.setModel(self.model)
        self.treewid.clicked.connect(self.on_treeView_clicked)
        self.treewid.setColumnWidth(0,300)
        self.fileName = ""
        self.filePath = ""
        
        self.gridLayout.addWidget(self.treewid, 0, 0, 1, 1)
        
        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)
        
        self.gridLayout_3 = QtGui.QGridLayout()
        self.gridLayout_3.setObjectName(_fromUtf8("gridLayout_3"))
        
#         Tekstvak kopieren van 

        self.lineEdit = QtGui.QLineEdit(Form)
        self.lineEdit.setReadOnly(True)
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        
        self.gridLayout_3.addWidget(self.lineEdit, 0, 1, 1, 1)
        
#         Label kopieren naar
        
        self.label_2 = QtGui.QLabel(Form)
        self.label_2.setObjectName(_fromUtf8("label_2"))
       
        self.gridLayout_3.addWidget(self.label_2, 1, 0, 1, 1)
        
#         Tekstvak kopieren naar
        
        self.lineEdit_2 = QtGui.QLineEdit(Form)
        self.lineEdit_2.setReadOnly(True)
        self.lineEdit_2.setObjectName(_fromUtf8("lineEdit_2"))
        self.gridLayout_3.addWidget(self.lineEdit_2, 1, 1, 1, 1)
        
#         Knop kopieren van

        self.pushButton_2 = QtGui.QPushButton(Form)
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.pushButton_2.clicked.connect(self.kopieren_van_click)
                
#         Knop kopieren naar

        self.gridLayout_3.addWidget(self.pushButton_2, 2, 1, 1, 1)
        self.pushButton = QtGui.QPushButton(Form)
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.pushButton.clicked.connect(self.kopieren_naar_click)        
        self.gridLayout_3.addWidget(self.pushButton, 3, 1, 1, 1)
        
#         Label kopieren van
        
        self.label = QtGui.QLabel(Form)
        self.label.setObjectName(_fromUtf8("label"))
        
        self.gridLayout_3.addWidget(self.label, 0, 0, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout_3, 1, 0, 1, 1)
        
#         Knop kopieren maar
        
        self.pushButton_3 = QtGui.QPushButton(Form)
        self.pushButton_3.setObjectName(_fromUtf8("pushButton_3"))
        self.gridLayout_2.addWidget(self.pushButton_3, 2, 0, 1, 1)
        self.pushButton_3.clicked.connect(self.kopieren_maar_click)
        
        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)
        
    @QtCore.pyqtSlot(QtCore.QModelIndex)
    def on_treeView_clicked(self, index):
        indexItem = self.model.index(index.row(), 0, index.parent())
    
        self.fileName = self.model.fileName(indexItem)
        self.filePath = self.model.filePath(indexItem)

    
    def kopieren_van_click(self):
        
        try:
            if self.filePath == "":
                 QtGui.QMessageBox.information(self, "Fout", "Je hebt geen bestand of map aangekikt, klik aub een bestand of map aan en probeer opnieuw")
            elif self.filePath == self.lineEdit_2.text():
                QtGui.QMessageBox.information(self, "Fout", "Je kan geen bestanden kopieren over hetzelfde bestand heen")
                
            else:
                self.lineEdit.setText(self.filePath)
                QtGui.QMessageBox.information(self, "Fout", "GG")
                
        except Exception, e:
            print e
            pass
            
    def kopieren_naar_click(self):
        try:
            if self.filePath == "":
                 QtGui.QMessageBox.information(self, "Fout", "Je hebt geen bestand of map aangekikt, klik aub een bestand of map aan en probeer opnieuw")
            elif self.filePath == self.lineEdit.text():
                QtGui.QMessageBox.information(self, "Fout", "Je kan geen bestanden kopieren over hetzelfde bestand heen")
                             
            else:
                self.lineEdit_2.setText(self.filePath)
                QtGui.QMessageBox.information(self, "Fout", "GG")
                
        except Exception, e:
            print e
            pass
               
    def kopieren_maar_click(self):
         
        print "knop 3"
       
        QtGui.QMessageBox.information(self, "Fout", "Er is iets mis gegaan, kijk uw opdracht na en probeer het opnieuw")

        sender = self.sender()
    
    """ 
     elif self.filePath != "C:\\":
       QtGui.QMessageBox.information(self, "Fout", "Je hele C schijf kopieren gaat hem nou net niet worden")
       self.filePath = ""
     """


    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Dir view", None))
        self.label_2.setText(_translate("Form", "Kopieer naar: ", None))
        
        self.pushButton_2.setText(_translate("Form", "Locatie kopieeren van", None))
        self.pushButton.setText(_translate("Form", "Locatie kopieeren naar", None))
        
        self.label.setText(_translate("Form", "Kopieer van: ", None))
        
        self.pushButton_3.setText(_translate("Form", "Kopieren maar", None))

if __name__ == '__main__':
    # QApplication created only here.
    app = QtGui.QApplication(sys.argv)
    ex = DirView()
    ex.show()
    sys.exit(app.exec_())

