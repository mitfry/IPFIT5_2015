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
            print "Dropbox installation found"
        elif os.path.exists("%s\\AppData\\Roaming\\Dropbox" % homefolder):
            print "Dropbox installation found"
        else:
            pass

        if os.path.exists("%s\\Dropbox" % homefolder):
            print "Dropbox folder found"
        else:
            pass

    def csearch_box(self):
        if os.path.exists("%s\\Box\\Box Sync" % programfiles):
            print "Box installation found"
        else:
            pass

        if os.path.exists("%s\\Box Sync" % homefolder):
            print "Box folder found"
        else:
            pass

    def csearch_googled(self):
       if os.path.exists("%s\\Google\\Drive" % programfiles):
            print "Google Drive installation found"
       else:
           pass

       if os.path.exists("%s\\Google Drive" % homefolder):
            print "Google Drive folder found"
       else:
            pass

    def csearch_oned(self):
        if os.path.exists("%s\\Microsoft OneDrive" % programfiles):
            print "OneDrive installation found"
        else:
            pass

        if os.path.exists("%s\\OneDrive" % homefolder):
            print "OneDrive folder found"
        else:
            pass

    def csearch_spidero(self):
        if os.path.exists("%s\\SpiderOak" % programfiles):
            print "SpideOak installation found"
        else:
            pass

        if os.path.exists("%s\\Desktop\\SpiderOak Hive.*" % homefolder):
            print "SpiderOak folder found"
        else:
            pass

    def csearch_mega(self):
        if os.path.exists("%s\\AppData\\Local\\MEGAsync" % homefolder):
            print "Mega installation found"
        else:
            pass

        if os.path.exists("%s\\Desktop\\MEGAsync.*" % homefolder):
            print "Mega folder found"
        else:
            pass

    def csearch_copy(self):
        if os.path.exists("%s\\AppData\\Roaming\\Copy" % homefolder):
            print "Copy installation found"
        else:
            pass

        if os.path.exists("%s\\Copy" % homefolder):
            print "Copy folder found"
        else:
            pass

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
