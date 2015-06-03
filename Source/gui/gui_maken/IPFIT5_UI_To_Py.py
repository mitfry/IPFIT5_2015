# Generate python file from UI file
# pyuic4 -o interface_thram.py interface_thram.ui

import sys
import os.path
import time

count = 0
while count < 1:
    count += 1
    time.sleep(1)

    if os.path.isfile(sys.path[0] + "\interface_thram.ui"):
        os.system("cd " + sys.path[0])
        os.system("pyuic4 -o " + sys.path[0] + "\interface_thram.py " + sys.path[0] + "\interface_thram.ui")
        print "Succesfully created interface_thram.py"
    else:
        print "interface_thram.ui is could not be found. Newb."

# !/usr/bin/env python

beginningLines = '''
#!/usr/bin/env python

# IPFIT5 imports
import sys
import time
from source.functions import Software
from source.functions import Hardware

'''

finalLines = '''
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
'''

sourceFile = open(sys.path[0] + "\interface_thram.py", 'r')
lines = sourceFile.read()
sourceFile.close()

parts = lines.split('class Ui_MainWindow(object):')

constructorCode = '''
class Ui_MainWindow(QtGui.QMainWindow):
    def __init__(self):
        QtGui.QMainWindow.__init__(self)
        self.setupUi(self)
        '''

f = open(sys.path[0] + "\interface_thram.py", 'w')
f.write(beginningLines)
f.write(parts[0])
f.write(constructorCode)
f.write(parts[1])
f.write(finalLines)
f.close()
