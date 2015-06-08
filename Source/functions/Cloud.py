__author__ = 'Tim Duysens'
"""
Last edited = 4-6-15
Deze classes zoeken naar sporen die duiden op het gebruik van Cloudgebruik.

Samenwerkende files: Software.py - Mitchell*

Global return = cloud_found

Specific returns =
-
-cfound_box
cfound_googled
cfound_oned
cfound_spidero
cfound_mega
cfound_copy

Het zal zoeken naar de volgende diensten:

-Dropbox
-Box
-Google Drive
-One Drive
-SpiderOak
-Mega
-Copy
"""

import sys
import os.path

sys.path.append(sys.path[0]+"/../modules")

import wmi

w = wmi.WMI(".")

# Get homefolder of user
homefolder = os.path.expanduser("~")
programfiles = os.environ['PROGRAMFILES']

class CloudSearch():
    def __init__(self):

        self.csearch_dropbox()
        self.csearch_box()
        self.csearch_googled()
        self.csearch_oned()
        self.csearch_spidero()
        self.csearch_mega()
        self.csearch_copy()
        self.process_search()

    def csearch_dropbox(self):
        if os.path.exists("%s\\Dropbox" % programfiles):
            dropboxres = "Dropbox installation found"
        elif os.path.exists("%s\\AppData\\Roaming\\Dropbox" % homefolder):
            dropboxres = "Dropbox installation found"
        else:
            dropboxres = "Dropbox installation not found"

        if os.path.exists("%s\\Dropbox" % homefolder):
            dropboxres2 = "Dropbox folder found"
        else:
            dropboxres2 = "Dpr[bpx fp;der mpt found"

        dropboxresultaat = []
        dropboxresultaat[0] = dropboxres
        dropboxresultaat[1] = dropboxres2
        return dropboxresultaat

    def csearch_box(self):
        if os.path.exists("%s\\Box\\Box Sync" % programfiles):
            boxres = "Box installation found"
        else:
            boxres = "Box installation not found"

        if os.path.exists("%s\\Box Sync" % homefolder):
            boxres2 = "Box folder found"
        else:
            boxres2 = "Box folder found"

        boxresultaat = []
        boxresultaat[0] = boxres
        boxresultaat[1] = boxres2

        return boxresultaat

    def csearch_googled(self):
       if os.path.exists("%s\\Google\\Drive" % programfiles):
            gores = "Google Drive installation found"
       else:
           gores = "Google Drive installation not found"

       if os.path.exists("%s\\Google Drive" % homefolder):
            gores2 = "Google Drive folder found"
       else:
           gores2 = "Google Drive folder not found"

       googleresultaat = []
       googleresultaat[0] = gores
       googleresultaat[1] = gores2

       return googleresultaat

    def csearch_oned(self):
        if os.path.exists("%s\\Microsoft OneDrive" % programfiles):
            oneres = "OneDrive installation found"
        else:
            oneres = "OneDrive installation not found"

        if os.path.exists("%s\\OneDrive" % homefolder):
            oneres2 = "OneDrive folder found"
        else:
            oneres2 = "OneDrive folder not found"

        oneresultaat = []
        oneresultaat.append()[0] = oneres
        oneresultaat[1] = oneres2

        return oneresultaat

    def csearch_spidero(self):
        if os.path.exists("%s\\SpiderOak" % programfiles):
            spires = "SpideOak installation found"
        else:
            spires = "SpiderOak installation not found"

        if os.path.exists("%s\\Desktop\\SpiderOak Hive.*" % homefolder):
            spires2 = "SpiderOak folder found"
        else:
            spires2 = "SpiderOak folder not found"

        spiderresultaat = []
        spiderresultaat[0] = spires
        spiderresultaat[1] = spires2

        return spiderresultaat

    def csearch_mega(self):
        if os.path.exists("%s\\AppData\\Local\\MEGAsync" % homefolder):
            meres = "Mega installation found"
        else:
            meres = "Mega installation not found"

        if os.path.exists("%s\\Desktop\\MEGAsync.*" % homefolder):
            meres2 = "Mega folder found"
        else:
            meres2 = "Mega folder not found"

        megaresultaat = []
        megaresultaat[0] = meres2
        megaresultaat[1] = meres

        return megaresultaat

    def csearch_copy(self):
        if os.path.exists("%s\\AppData\\Roaming\\Copy" % homefolder):
            cores = "Copy installation found"
        else:
            cores = "Copy installation not found"

        if os.path.exists("%s\\Copy" % homefolder):
            cores2 = "Copy folder found"
        else:
            cores2 = "Copy folder not found"

        copyresultaat = []
        copyresultaat[0] = cores
        copyresultaat[1] = cores2

        return copyresultaat

    def process_search(self):
        w = wmi.WMI(".")
        for process in w.Win32_Process():
            if process.Name == "Dropbox.exe":
                print "Dropbox is active as process"

            elif process.Name == "BoxSync.exe":
                print "Box is active as process"

            elif process.Name == "googledrivesync.exe":
                print "Google Drive is active as process"

            elif process.Name == "OneDrive.exe":
                print "OneDrive is active as process"

            elif process.Name == "SpiderOak.exe":
                print "SpiderOak is active as process"

            elif process.Name == "MEGAsync.exe":
                print "Mega is active as process"

            elif process.Name == "CopyAgent.exe":
                print "Copy is active as process"

            else:
                pass

if __name__ == '__main__':
    CloudSearch()
    print homefolder
    print programfiles
