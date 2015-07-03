__author__ = 'Andre'

import hashlib, os

from PyQt4 import QtGui
import csv, time
import sys
sys.path.append(sys.path[0]+"/../gui")

def inputfolder():
    full_path = str(
        QtGui.QFileDialog.getExistingDirectory(None, 'Kies de te doorzoeken map:', '../\\', QtGui.QFileDialog.ShowDirsOnly))
    return str(full_path)

def calculate_hash_from_multiplee_files(full_path):
    full_path = str(full_path)
    count = 0
    outputfolder = str(
        QtGui.QFileDialog.getExistingDirectory(None, 'Select output folder', 'C:\\', QtGui.QFileDialog.ShowDirsOnly))
    outputlog = open(outputfolder + '\log.txt', 'w')
    csvFile = open(outputfolder + '\ ' + "fileSystemReport.csv", 'wb')
    writer = csv.writer(csvFile, delimiter=',', quoting=csv.QUOTE_ALL)
    writer.writerow(('Bestand', 'Locatie', 'Hashvorm', 'Hashwaarde', 'Bestandsgrootte in KB', 'Laatst aangepast', 'Laatst geopend',
                     'Creatiedatum'))
    outputlog.write("The md5 files of" + full_path + '  are:\n\n')
    list_hashes = []
    for root, dirs, files in os.walk(full_path):
        for file_name in files:
            count += 1
            print count, file_name
            size = os.stat(root + '/' + file_name)
            (mode, ino, dev, nlink, uid, gid, size, atime,
             mtime, ctime) = os.stat(root + '/' + file_name)
            filesize = str(size/1024)
            list_hashes.append([file_name, root + '\ ', 'md5', hashlib.md5(
                open(root + '/' + file_name, 'rb').read()).hexdigest(), filesize, time.ctime(mtime), time.ctime(atime),
                                time.ctime(ctime)])
            line = str(str(count) + root + '/' + file_name + ' is       ' + hashlib.md5(
                open(root + '/' + file_name, 'rb').read()).hexdigest() + '\n')
            outputlog.write(line)
            writer.writerow((file_name, root + '/', 'md5', hashlib.md5(
                open(root + '/' + file_name, 'rb').read()).hexdigest(), filesize, time.ctime(mtime), time.ctime(atime),
                             time.ctime(ctime)))
    csvFile.close()
    outputlog.close()
    return list_hashes
