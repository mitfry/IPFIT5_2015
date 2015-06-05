import hashlib, os

from PyQt4 import QtGui

def calculate_hash_from_multiplee_files(self):
    full_path = str(QtGui.QFileDialog.getExistingDirectory(None, 'Select a folder:', 'C:\\', QtGui.QFileDialog.ShowDirsOnly))
    count = 0
    output = open(QtGui.QFileDialog.getSaveFileName(None, 'Save output file as', 'C:\\', filter='*.txt'), 'w')
    output.write("The sha256 files of" + full_path + '  are:\n\n')
    for root, dirs, files in os.walk(full_path):
        for file_name in files:
            count += 1
            line = str(str(count) + root + '/' + file_name + ' is       ' + hashlib.sha256(
                open(root + '/' + file_name, 'rb').read()).hexdigest() + '\n')
            output.write(line)
    output.close()