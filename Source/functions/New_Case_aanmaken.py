# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'New_Case.ui'
#
# Created: Mon Jun 29 12:11:11 2015
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

class Ui_Newcase(QtGui.QDialog):
    def __init__(self):
        QtGui.QDialog.__init__(self)
        self.setupUi(self)

    def setupUi(self, Newcase):
        Newcase.setObjectName(_fromUtf8("Newcase"))
        Newcase.resize(521, 336)
        self.gridLayout_5 = QtGui.QGridLayout(Newcase)
        self.gridLayout_5.setObjectName(_fromUtf8("gridLayout_5"))
        self.Casename = QtGui.QLabel(Newcase)
        self.Casename.setObjectName(_fromUtf8("Casename"))
        self.gridLayout_5.addWidget(self.Casename, 0, 0, 1, 1)
        self.lineEdit_Casename = QtGui.QLineEdit(Newcase)
        self.lineEdit_Casename.setObjectName(_fromUtf8("lineEdit_Casename"))
        self.gridLayout_5.addWidget(self.lineEdit_Casename, 0, 1, 1, 2)
        self.Investigator = QtGui.QLabel(Newcase)
        self.Investigator.setObjectName(_fromUtf8("Investigator"))
        self.gridLayout_5.addWidget(self.Investigator, 1, 0, 1, 1)
        self.lineEdit_Investigator = QtGui.QLineEdit(Newcase)
        self.lineEdit_Investigator.setObjectName(_fromUtf8("lineEdit_Investigator"))
        self.gridLayout_5.addWidget(self.lineEdit_Investigator, 1, 1, 1, 2)
        self.Organization = QtGui.QLabel(Newcase)
        self.Organization.setObjectName(_fromUtf8("Organization"))
        self.gridLayout_5.addWidget(self.Organization, 2, 0, 1, 1)
        self.lineEdit_Organization = QtGui.QLineEdit(Newcase)
        self.lineEdit_Organization.setObjectName(_fromUtf8("lineEdit_Organization"))
        self.gridLayout_5.addWidget(self.lineEdit_Organization, 2, 1, 1, 2)
        self.Contactdetails = QtGui.QLabel(Newcase)
        self.Contactdetails.setObjectName(_fromUtf8("Contactdetails"))
        self.gridLayout_5.addWidget(self.Contactdetails, 3, 0, 1, 1)
        self.lineEdit_ContactDetails = QtGui.QLineEdit(Newcase)
        self.lineEdit_ContactDetails.setObjectName(_fromUtf8("lineEdit_ContactDetails"))
        self.gridLayout_5.addWidget(self.lineEdit_ContactDetails, 3, 1, 1, 2)
        self.Timezone = QtGui.QLabel(Newcase)
        self.Timezone.setObjectName(_fromUtf8("Timezone"))
        self.gridLayout_5.addWidget(self.Timezone, 4, 0, 1, 1)
        self.comboBox_Timezone = QtGui.QComboBox(Newcase)
        self.comboBox_Timezone.setObjectName(_fromUtf8("comboBox_Timezone"))
        self.gridLayout_5.addWidget(self.comboBox_Timezone, 4, 1, 1, 2)
        self.Drive = QtGui.QLabel(Newcase)
        self.Drive.setObjectName(_fromUtf8("Drive"))
        self.gridLayout_5.addWidget(self.Drive, 5, 0, 1, 1)
        self.comboBox_Drive = QtGui.QComboBox(Newcase)
        self.comboBox_Drive.setObjectName(_fromUtf8("comboBox_Drive"))
        self.gridLayout_5.addWidget(self.comboBox_Drive, 5, 1, 1, 2)
        self.Casefolder = QtGui.QLabel(Newcase)
        self.Casefolder.setObjectName(_fromUtf8("Casefolder"))
        self.gridLayout_5.addWidget(self.Casefolder, 6, 0, 1, 1)
        self.radioButton_Default = QtGui.QRadioButton(Newcase)
        self.radioButton_Default.setObjectName(_fromUtf8("radioButton_Default"))
        self.gridLayout_5.addWidget(self.radioButton_Default, 6, 1, 1, 1)
        self.radioButton_Custom = QtGui.QRadioButton(Newcase)
        self.radioButton_Custom.setObjectName(_fromUtf8("radioButton_Custom"))
        self.gridLayout_5.addWidget(self.radioButton_Custom, 6, 2, 1, 1)
        self.lineEdit_Browse = QtGui.QLineEdit(Newcase)
        self.lineEdit_Browse.setObjectName(_fromUtf8("lineEdit_Browse"))
        self.gridLayout_5.addWidget(self.lineEdit_Browse, 7, 0, 1, 3)
        self.Browse = QtGui.QPushButton(Newcase)
        self.Browse.setObjectName(_fromUtf8("Browse"))
        self.gridLayout_5.addWidget(self.Browse, 7, 3, 1, 1)
        self.Ok = QtGui.QPushButton(Newcase)
        self.Ok.setObjectName(_fromUtf8("Ok"))
        self.gridLayout_5.addWidget(self.Ok, 8, 3, 1, 1)
        self.Cancel = QtGui.QPushButton(Newcase)
        self.Cancel.setObjectName(_fromUtf8("Cancel"))
        self.gridLayout_5.addWidget(self.Cancel, 8, 4, 1, 1)

        self.retranslateUi(Newcase)
        QtCore.QObject.connect(self.Ok, QtCore.SIGNAL(_fromUtf8("clicked()")), Newcase.accept)
        QtCore.QObject.connect(self.Cancel, QtCore.SIGNAL(_fromUtf8("clicked()")), Newcase.close)
        QtCore.QMetaObject.connectSlotsByName(Newcase)

    def retranslateUi(self, Newcase):
        Newcase.setWindowTitle(_translate("Newcase", "New Case", None))
        self.Casename.setText(_translate("Newcase", "Case Name:", None))
        self.Investigator.setText(_translate("Newcase", "Investigator:", None))
        self.Organization.setText(_translate("Newcase", "Organization:", None))
        self.Contactdetails.setText(_translate("Newcase", "Contact Details:", None))
        self.Timezone.setText(_translate("Newcase", "Timezone:", None))
        self.Drive.setText(_translate("Newcase", "Drive:", None))
        self.Casefolder.setText(_translate("Newcase", "Case Folder: ", None))
        self.radioButton_Default.setText(_translate("Newcase", "Default Location", None))
        self.radioButton_Custom.setText(_translate("Newcase", "Custom Location", None))
        self.Browse.setText(_translate("Newcase", "Browse", None))
        self.Ok.setText(_translate("Newcase", "Ok", None))
        self.Cancel.setText(_translate("Newcase", "Cancel", None))

def start():
    # QApplication created only here.
    global window
    window = Ui_Newcase()
    window.show()
    window.exec_()

'''if name == "__main__":
    # QApplication created only here.
    global name
    name = Ui_Newcase()
    name.show()
    name.exec_()'''

