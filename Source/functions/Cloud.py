__author__ = 'Tim Duysens'
"""
Last edited = 9-6-15
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
from Software import processes



# Get homefolder of user
homefolder = os.path.expanduser("~")
programfiles = os.environ['PROGRAMFILES']
list_cloud_storage_services = [["Cloud Dienst", "Locatie", "", ""]]


def cloud():
    return list_cloud_storage_services


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
            dropboxres = "Dropbox installation found in the programfiles"
        elif os.path.exists("%s\\AppData\\Roaming\\Dropbox" % homefolder):
            dropboxres = "Dropbox installation found in the AppData Roaming folder"
        else:
            dropboxres = "Dropbox installation not found"

        if os.path.exists("%s\\Dropbox" % homefolder):
            dropboxres2 = "Dropbox folder found in the userfolder"
        else:
            dropboxres2 = "Dropbox folder not found"

        dropboxresultaat = []
        dropboxresultaat.append(dropboxres)
        dropboxresultaat.append(dropboxres2)
        list_cloud_storage_services.append([str(dropboxresultaat[0]), str(dropboxresultaat[1])])
        return dropboxresultaat

    def csearch_box(self):
        if os.path.exists("%s\\Box\\Box Sync" % programfiles):
            boxres = "Box installation found in the programfiles"
        else:
            boxres = "Box installation not found"

        if os.path.exists("%s\\Box Sync" % homefolder):
            boxres2 = "Box folder found in the userfolder"
        else:
            boxres2 = "Box folder found"

        boxresultaat = []
        boxresultaat.append(boxres)
        boxresultaat.append(boxres2)

        return boxresultaat

    def csearch_googled(self):
        if os.path.exists("%s\\Google\\Drive" % programfiles):
            gores = "Google Drive installation found in the programfiles"
        else:
            gores = "Google Drive installation not found"

        if os.path.exists("%s\\Google Drive" % homefolder):
            gores2 = "Google Drive folder found in the userfolder"
        else:
            gores2 = "Google Drive folder not found"

        googleresultaat = []
        googleresultaat.append(gores)
        googleresultaat.append(gores2)

        return googleresultaat

    def csearch_oned(self):
        if os.path.exists("%s\\Microsoft OneDrive" % programfiles):
            oneres = "OneDrive installation found in the programfiles"
        else:
            oneres = "OneDrive installation not found"

        if os.path.exists("%s\\OneDrive" % homefolder):
            oneres2 = "OneDrive folder found in the userfolder"
        else:
            oneres2 = "OneDrive folder not found"

        oneresultaat = []
        oneresultaat.append(oneres)
        oneresultaat.append(oneres2)

        return oneresultaat

    def csearch_spidero(self):
        if os.path.exists("%s\\SpiderOak" % programfiles):
            spires = "SpideOak installation found in the programfiles"
        else:
            spires = "SpiderOak installation not found"

        if os.path.exists("%s\\Desktop\\SpiderOak Hive.*" % homefolder):
            spires2 = "SpiderOak folder found in the userfolder"
        else:
            spires2 = "SpiderOak folder not found"

        spiderresultaat = []
        spiderresultaat.append(spires)
        spiderresultaat.append(spires2)

        return spiderresultaat

    def csearch_mega(self):
        if os.path.exists("%s\\AppData\\Local\\MEGAsync" % homefolder):
            meres = "Mega installation found in the AppData local folder"
        else:
            meres = "Mega installation not found"

        if os.path.exists("%s\\Desktop\\MEGAsync.*" % homefolder):
            meres2 = "Mega folder found on the desktop"
        else:
            meres2 = "Mega folder not found"

        megaresultaat = []
        megaresultaat.append(meres2)
        megaresultaat.append(meres)

        return megaresultaat

    def csearch_copy(self):
        if os.path.exists("%s\\AppData\\Roaming\\Copy" % homefolder):
            cores = "Copy installation found in the AppData roaming folder"
        else:
            cores = "Copy installation not found"

        if os.path.exists("%s\\Copy" % homefolder):
            cores2 = "Copy folder found in the userfolder"
        else:
            cores2 = "Copy folder not found"

        copyresultaat = []
        copyresultaat.append(cores)
        copyresultaat.append(cores2)

        return copyresultaat

    def process_search(self):
        for process in processes():
            for proc in process:
                if proc == 'Dropbox.exe':
                    print "Dropbox is active as process"

                elif proc == "BoxSync.exe":
                    print "Box is active as process"

                elif proc == "googledrivesync.exe":
                    print "Google Drive is active as process"

                elif proc == "OneDrive.exe" or proc == "SkyDrive.exe":
                    print "OneDrive and/or SkyDrive is active as process"

                elif proc == "SpiderOak.exe":
                    print "SpiderOak is active as process"

                elif proc == "MEGAsync.exe":
                    print "Mega is active as process"

                elif proc == "CopyAgent.exe":
                    print "Copy is active as process"

                    # print homefolder
                    # print programfiles


CloudSearch()
