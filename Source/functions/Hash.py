import hashlib, os

from PyQt4 import QtGui
import csv, time

def calculate_hash_from_multiplee_files():
    full_path = str(QtGui.QFileDialog.getExistingDirectory(None, 'Select a folder:', 'C:\\', QtGui.QFileDialog.ShowDirsOnly))
    count = 0
    outputfolder = open(QtGui.QFileDialog.getExistingDirectory(None, 'Select output folder', 'C:\\', QtGui.QFileDialog.ShowDirsOnly))
    outputlog = open(outputfolder+'log.txt', 'w')
    csvFile = open(outputfolder+'fileSystemReport.csv', 'wb')
    writer = csv.writer(csvFile, delimiter=',', quoting=csv.QUOTE_ALL)
    writer.writerow(('File', 'Size', 'Hashtype', 'Hash', 'Last Modified', 'Last Access', 'Created Time'))
    outputlog.write("The sha256 files of" + full_path + '  are:\n\n')
    for root, dirs, files in os.walk(full_path):
        for file_name in files:
            count += 1
            size = os.stat(file_name)
            (mode, ino, dev, nlink, uid, gid, size, atime,
                         mtime, ctime) = os.stat(file_name)
            filesize = str(size)
            line = str(str(count) + root + '/' + file_name + ' is       ' + hashlib.sha256(
                open(root + '/' + file_name, 'rb').read()).hexdigest() + '\n')
            outputlog.write(line)
            writer.writerow((root + '/' + file_name, filesize, 'sha256', hashlib.sha256(
                open(root + '/' + file_name, 'rb').read()).hexdigest() + '\n'), time.ctime(mtime), time.ctime(atime), time.ctime(ctime))
    csvFile.close()
    outputlog.close()

calculate_hash_from_multiplee_files()