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


class Ui_Dialog(QtGui.QDialog):
    def __init__(self, parent=None):
        super(Ui_Dialog, self).__init__(parent)
        self.setupUi(self)

    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(306, 237)
        self.gridLayout_3 = QtGui.QGridLayout(Dialog)
        self.gridLayout_3.setObjectName(_fromUtf8("gridLayout_3"))
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.chk_Cloud = QtGui.QCheckBox(Dialog)
        self.chk_Cloud.setObjectName(_fromUtf8("chk_Cloud"))
        self.verticalLayout.addWidget(self.chk_Cloud)
        self.chk_Email = QtGui.QCheckBox(Dialog)
        self.chk_Email.setObjectName(_fromUtf8("chk_Email"))
        self.verticalLayout.addWidget(self.chk_Email)
        self.chk_Hardware = QtGui.QCheckBox(Dialog)
        self.chk_Hardware.setObjectName(_fromUtf8("chk_Hardware"))
        self.verticalLayout.addWidget(self.chk_Hardware)
        self.chk_Hash = QtGui.QCheckBox(Dialog)
        self.chk_Hash.setObjectName(_fromUtf8("chk_Hash"))
        self.verticalLayout.addWidget(self.chk_Hash)
        self.chk_Internet_History = QtGui.QCheckBox(Dialog)
        self.chk_Internet_History.setObjectName(_fromUtf8("chk_Internet_History"))
        self.verticalLayout.addWidget(self.chk_Internet_History)
        self.chk_Software = QtGui.QCheckBox(Dialog)
        self.chk_Software.setObjectName(_fromUtf8("chk_Software"))
        self.verticalLayout.addWidget(self.chk_Software)
        self.gridLayout_3.addLayout(self.verticalLayout, 0, 0, 1, 1)
        self.Cancel_Button = QtGui.QPushButton(Dialog)
        self.Cancel_Button.setObjectName(_fromUtf8("Cancel_Button"))
        self.gridLayout_3.addWidget(self.Cancel_Button, 3, 2, 1, 1)
        self.Ok_Button = QtGui.QPushButton(Dialog)
        self.Ok_Button.setObjectName(_fromUtf8("Ok_Button"))
        self.gridLayout_3.addWidget(self.Ok_Button, 3, 1, 1, 1)

        self.retranslateUi(Dialog)
        QtCore.QObject.connect(self.Cancel_Button, QtCore.SIGNAL(_fromUtf8("clicked()")), Dialog.close)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Functions", None))
        self.chk_Cloud.setText(_translate("Dialog", "Cloud", None))
        self.chk_Email.setText(_translate("Dialog", "Email", None))
        self.chk_Hardware.setText(_translate("Dialog", "Hardware", None))
        self.chk_Hash.setText(_translate("Dialog", "Hash", None))
        self.chk_Internet_History.setText(_translate("Dialog", "Internetgeschiedenis", None))
        self.chk_Software.setText(_translate("Dialog", "Software", None))
        self.Cancel_Button.setText(_translate("Dialog", "Cancel", None))
        self.Ok_Button.setText(_translate("Dialog", "Ok", None))

def start():
    # QApplication created only here.
    global window
    window = Ui_Dialog()
    window.show()
    window.exec_()




