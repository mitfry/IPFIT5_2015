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

    if os.path.isfile(sys.path[0] + "\interface_thram.ui"):
        os.system("cd " + sys.path[0])
        os.system("pyuic4 -o " + sys.path[0] + "\interface_thram.py " + sys.path[0] + "\interface_thram.ui")
        print "interface_thram.ui has been found and was converted to interface_thram.py"
    else:
        print "interface_thram.ui is could not be found. Newb."

time.sleep(1)
print "Gathering all custom code from this script..."


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
import Hash
import Cloud
import Internetgeschiedenis
import Select_functions
import Create_Case

'''

finalLines = '''
        # Mitchell
        # The code below is used to connect methods to the buttons off the interface

        # IPFIT5 Buttons, Methods and other code
        self.setWindowTitle(_translate("MainWindow", "THRAM" + u'\u2122' + "- The Ultimate Triage Solution", None))

        # Tab Project:
        self.pushProject.clicked.connect(lambda: self.project_location(Create_Case.outputfolder()))
        self.projectOpslaan.clicked.connect(lambda: self.save_project())
        self.pushCasus.clicked.connect(lambda: self.maakCasus())
        self.casusOpslaan.clicked.connect(lambda : self.save_casus())

        # Tab Systeem:
        self.tab_System.setEnabled(False)


        # Tab Software:
        self.tab_Software.setEnabled(False)
        self.btn_Processen.clicked.connect(lambda: self.status_bar("Lijst vernieuwen...", 2000))
        self.btn_Processen.clicked.connect(lambda: self.fill_software_treewidget(Software.processes()))
        self.btn_Services.clicked.connect(lambda: self.status_bar("Lijst vernieuwen...", 2000))
        self.btn_Services.clicked.connect(lambda: self.fill_software_treewidget(Software.services()))
        self.btn_Software.clicked.connect(lambda: self.status_bar("Lijst vernieuwen...", 2000))
        self.btn_Software.clicked.connect(lambda: self.fill_software_treewidget(Software.software_installed()))
        self.btn_Cloud.clicked.connect(lambda: self.status_bar("Lijst vernieuwen...", 2000))
        self.btn_Cloud.clicked.connect(lambda: self.fill_software_treewidget(Cloud.cloud()))

        # Tab Internet:
        self.tab_Internet.setEnabled(False)
        self.btn_Load_Internet_History.clicked.connect(lambda: self.fillBrowserTreewidget())
        self.btn_Show_Internet_History.clicked.connect(lambda: self.zoekBrowser())
        self.btn_Search_Internet_History.clicked.connect(lambda: self.zoekWoord())

        # Tab E-mail:

        # Tab Bestanden:
        self.tab_Files.setEnabled(False)
        self.btn_Search_From.clicked.connect(lambda: self.fill_searchbar(Hash.inputfolder()))
        self.btn_Hash.clicked.connect(
            lambda: self.fill_hash_treewidget(Hash.calculate_hash_from_multiplee_files(output_list, casuslocatie)))

        # Menu Opties -> Functies
        self.actionFuncties.triggered.connect(lambda: Select_functions.start())

    # Mitchell
    # The method below fills the treeWidget on the software tab according to the button that is clicked.

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
            # self.treew_Software.resizeColumnToContents(passed_list_number)
            QtGui.qApp.processEvents()
            passed_list_number += 1

    # Hugo

    def fillBrowserTreewidget(self):

        getInternetExplorer = 0
        getFirefox = 0
        getChrome = 0

        if self.chk_Internet_Explorer.isChecked():
            getInternetExplorer = 1
        if self.chk_Mozilla_FireFox.isChecked():
            getFirefox = 1
        if self.chk_Google_Chrome.isChecked():
            getChrome = 1

        historyList = Internetgeschiedenis.loadData(getInternetExplorer, getFirefox, getChrome)

        self.browserTreeWidget.clear()
        rowNumber = 0
        for row in historyList:
            item = QTreeWidgetItem()
            item.setText(0, unicode(row[0]))
            item.setText(1, unicode(row[4]))
            item.setText(2, unicode(row[2]))
            item.setText(3, unicode(row[1]))
            item.setText(4, unicode(row[3]))
            self.browserTreeWidget.insertTopLevelItem(rowNumber, item)
            rowNumber += 1
            QtGui.qApp.processEvents()

    def zoekBrowser(self):

        getInternetExplorer = 0
        getFirefox = 0
        getChrome = 0

        if self.chk_Internet_Explorer.isChecked():
            getInternetExplorer = 1
        if self.chk_Mozilla_FireFox.isChecked():
            getFirefox = 1
        if self.chk_Google_Chrome.isChecked():
            getChrome = 1

        numberOfResults = int(self.txt_Internet_History_Amount.text())

        mostvisited = Internetgeschiedenis.showMostVisited(Internetgeschiedenis.loadData(getInternetExplorer, getFirefox, getChrome), numberOfResults)

        self.browserTreeWidget.clear()
        rowNumber = 0
        for row in mostvisited:
            item = QTreeWidgetItem()
            item.setText(0, unicode(row[0]))
            item.setText(1, unicode(row[4]))
            item.setText(2, unicode(row[2]))
            item.setText(3, unicode(row[1]))
            item.setText(4, unicode(row[3]))
            self.browserTreeWidget.insertTopLevelItem(rowNumber, item)
            rowNumber += 1
            QtGui.qApp.processEvents()

    def zoekWoord(self):

        getInternetExplorer = 0
        getFirefox = 0
        getChrome = 0

        searchWord = self.txt_Internet_History_Search.text()

        if self.chk_Internet_Explorer.isChecked():
            getInternetExplorer = 1
        if self.chk_Mozilla_FireFox.isChecked():
            getFirefox = 1
        if self.chk_Google_Chrome.isChecked():
            getChrome = 1
        if self.chk_Internet_History_Search_Capital_Letter.isChecked() == False:
            searchWord = str(searchWord).lower()

        searchResults = Internetgeschiedenis.searchData(Internetgeschiedenis.loadData(getInternetExplorer, getFirefox, getChrome), searchWord)

        self.browserTreeWidget.clear()
        rowNumber = 0
        for row in searchResults:
            item = QTreeWidgetItem()
            item.setText(0, unicode(row[0]))
            item.setText(1, unicode(row[4]))
            item.setText(2, unicode(row[2]))
            item.setText(3, unicode(row[1]))
            item.setText(4, unicode(row[3]))
            self.browserTreeWidget.insertTopLevelItem(rowNumber, item)
            rowNumber += 1
            QtGui.qApp.processEvents()

    # Andre

    # Andre
    def project_location(self, locatie):
        global location
        print self.ProjectNaam.text()
        self.getProject.setText(_translate("MainWindow", locatie + "\\\" + self.ProjectNaam.text(), None))
        location = str(locatie + "\\\" + self.ProjectNaam.text())
        print location
        return

    def save_project(self):
        naamOmderzoeker = self.naamOnderzoeker.text()
        projectNaam = self.ProjectNaam.text()
        projectDatum = self.ProjectDatum.text()
        print  location
        Create_Case.save_project(location, projectNaam, naamOmderzoeker, projectDatum)
        self.makeCasus.setEnabled(True)
        self.makeComputernaam.setEnabled(True)
        self.casusTijd.setEnabled(True)
        self.pushCasus.setEnabled(True)
        self.casusOpslaan.setEnabled(True)
        return

    def maakCasus(self):
        global casuslocatie
        global computernaam
        global casusnaam
        casusnaam = str(self.makeCasus.text())
        self.getCasus.setText(str(location) + "\\\" + str(casusnaam))
        casuslocatie = location + "\\\" + casusnaam
        self.getComputernaam.setText(self.makeComputernaam.text())
        computernaam = self.getComputernaam.text()
        print str(casuslocatie)

    def save_casus(self):
        print casuslocatie
        casustijd = str(self.casusTijd.text())
        Create_Case.save_casus(casuslocatie, casusnaam, computernaam, casustijd)
        self.tab_System.setEnabled(True)
        self.tab_Files.setEnabled(True)
        self.tab_Internet.setEnabled(True)
        self.tab_Software.setEnabled(True)
        return

    def fill_searchbar(self, output):
        global output_list
        self.show_Search_From.clear()
        self.show_Search_From.insert(str(output))
        self.btn_Hash.setEnabled(True)
        output_list = output

    def fill_hash_treewidget(self, passed_list):
        self.treew_Bestanden.clear()
        for row in reversed(passed_list):
            row_number = 0
            item = QTreeWidgetItem()
            while row_number < 8:
                item.setText(row_number, unicode(row[row_number]))
                self.treew_Bestanden.insertTopLevelItem(row_number, item)
                row_number += 1
            QtGui.qApp.processEvents()

    # Mitchell
    # The code below includes all methods required to start, pause, and stop the progress bar.

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

    # Mitchell
    # Below is a method that can edit the statusbar on the bottom of the window.
    # Use like this: status_bar("YOURTEXT", TIME_IN_MILLISECONDS)

    def status_bar(self, message, time_in_mills):
        self.statusbar.showMessage(message, time_in_mills)

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
print "Succesfully added all custom code to interface_thram.py\n"
time.sleep(1)
print "Interface_thram is ready for use!"
time.sleep(3)