__author__ = 'Mitchell'
# Generate python file from UI file
# pyuic4 -o interface_thram.py interface_thram.ui

# DO NOT TOUCH ANYTHING UNTIL LINE 30
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
__author__ = 'Mitchell'

# IPFIT5 imports
# Built-in
import sys
import time
from PyQt4.QtGui import QTreeWidgetItem

# Add folder "functions" to the locations to import from
sys.path.append(sys.path[0]+"/../functions")

# Custom
import Software
import Hardware
import Hash
import Cloud

'''

finalLines = '''
        # IPFIT5 Buttons, Methods and other code
        self.setWindowTitle(_translate("MainWindow", "THRAM" + u'\u2122' + "- The Ultimate Triage Solution", None))

        # Tab Project:
        self.btn_Test.clicked.connect(self.test_mijn_functie)
        self.btn_Progressbar.clicked.connect(self.update_progress)

        # Tab Systeem:

        # Tab Software:
        self.btn_Processen.clicked.connect(lambda: self.status_bar("Lijst vernieuwen...", 1000))
        self.btn_Processen.clicked.connect(lambda: self.fill_software_treewidget(Software.processes()))
        self.btn_Services.clicked.connect(lambda: self.status_bar("Lijst vernieuwen...", 1000))
        self.btn_Services.clicked.connect(lambda: self.fill_software_treewidget(Software.services()))
        self.btn_Software.clicked.connect(lambda: self.status_bar("Lijst vernieuwen...", 1000))
        self.btn_Software.clicked.connect(lambda: self.fill_software_treewidget(Software.software_installed()))
        self.btn_Software.clicked.connect(lambda: self.status_bar("Lijst vernieuwen...", 1000))
        self.btn_Cloud.clicked.connect(lambda: Cloud.CloudSearch())

        # Tab Internet:

        # Tab E-maail:

        # Tab Bestanden:
        self.btn_Search_From.clicked.connect(lambda: self.fill_searchbar(Hash.inputfolder()))
        self.btn_Hash.clicked.connect(
            lambda: self.fill_hash_treewidget(Hash.calculate_hash_from_multiplee_files(output_list)))

    def fill_software_treewidget(self, passed_list):
        self.treew_Software.clear()
        passed_list_number = 0

        for title in passed_list[0]:
            self.treew_Software.headerItem().setText(passed_list_number, _translate("MainWindow", title, None))
            passed_list_number += 1

        passed_list_number = 0
        for row in passed_list[1:]:
            item = QTreeWidgetItem()
            for row_nr in range(0, len(row)):
                item.setText(row_nr, unicode(row[row_nr]))

            self.treew_Software.insertTopLevelItem(passed_list_number, item)
            QtGui.qApp.processEvents()
            passed_list_number += 1

    def fill_searchbar(self, output):
        global output_list
        self.show_Search_From.clear()
        self.show_Search_From.insert(str(output))
        self.btn_Hash.setEnabled(True)
        output_list = output

    def fill_hash_treewidget(self, passed_list):
        self.treew_Bestanden.clear()
        for row in passed_list:
            row_number = 0
            item = QTreeWidgetItem()
            while row_number < 8:
                item.setText(row_number, unicode(row[row_number]))
                self.treew_Bestanden.insertTopLevelItem(row_number, item)
                row_number += 1
            QtGui.qApp.processEvents()

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

    # Het is niet te geloven dames!

    global x
    x = 0

    def status_bar(self, message, time_in_mills):
        self.statusbar.showMessage(message, time_in_mills)

    def test_mijn_functie(self):
        global x
        if x < 2:
            print "Pauper"
        elif x < 5:
            print "Pauperr!"
        elif x < 9:
            print "Wat klik je nou nog?!"
        elif x < 12:
            print "Noob alert: Application soon exiting..."
            for i in range(0, 5):
                i = 5 - i
                self.status_bar("Exiting in: " + str(i) + " seconds... =3", 0)
                time.sleep(1)

            print "Laatsnorr.."
            self.status_bar("Laatsnorr...", 0)
            time.sleep(1)
            sys.exit()
        x += 1

# IPFIT5 constructor
if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    ex = Ui_MainWindow()
    ex.show()

    # Starting threads for generating information
    Software.WorkerThread().start()

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
        self._active = False
        '''

f = open(sys.path[0] + "\interface_thram.py", 'w')
f.write(beginningLines)
f.write(parts[0])
f.write(constructorCode)
f.write(parts[1])
f.write(finalLines)
f.close()
