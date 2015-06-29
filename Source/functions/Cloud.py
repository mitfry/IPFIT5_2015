__author__ = 'Tim Duysens'
"""
Last edited = 29-6-15
Deze classes zoeken naar sporen die duiden op het gebruik van Cloudgebruik.

Samenwerkende files: Software.py - Mitchell

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

Cloudlog houd bij in het logboek wat er gebeurd in het script,
geprogrammerde niveaus: debug, info
"""

import sys
import os.path
from Software import processes
import logging

cloudlog = logging.getLogger("THRAM - Cloud")
cloudlog.debug("Cloud search imported")

# Get homefolder of user
homefolder = os.path.expanduser("~")
programfiles = os.environ['PROGRAMFILES']
list_cloud_storage_services = [["Cloud Dienst", "Locatie", "Process", ""]]

cloudlog.debug("Vars init: " + homefolder + " " + programfiles + " " + str(list_cloud_storage_services))

def cloud():
    # Geeft aangemaakte lijst terug aan main
    cloudlog.debug("Return asked")
    cloudlog.info("Given list: " + str(list_cloud_storage_services))
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
        cloudlog.debug("Generated list inside module: " + str(list_cloud_storage_services))

        # Defs die zoeken naar standaard install mappen van clouddiensten, wordt teruggegeven aan lijst
    def csearch_dropbox(self):
        cloudlog.debug("Folder search Dropbox")
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
        dropboxresultaat.append(self.dropproc())

        list_cloud_storage_services.append([str(dropboxresultaat[0]), str(dropboxresultaat[1]), str(dropboxresultaat[2])])

        return dropboxresultaat

    def csearch_box(self):
        cloudlog.debug("Folder search Box")
        if os.path.exists("%s\\Box\\Box Sync" % programfiles):
            boxres = "Box installation found in the programfiles"
        else:
            boxres = "Box installation not found"

        if os.path.exists("%s\\Box Sync" % homefolder):
            boxres2 = "Box folder found in the userfolder"
        else:
            boxres2 = "Box folder not found"

        boxresultaat = []
        boxresultaat.append(boxres)
        boxresultaat.append(boxres2)
        boxresultaat.append(self.boxproc())

        list_cloud_storage_services.append([str(boxresultaat[0]), str(boxresultaat[1]), str(boxresultaat[2])])
        return boxresultaat

    def csearch_googled(self):
        cloudlog.debug("Folder search Google Drive")
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
        googleresultaat.append(self.googleproc())

        list_cloud_storage_services.append([str(googleresultaat[0]), str(googleresultaat[1]), str(googleresultaat[2])])
        return googleresultaat

    def csearch_oned(self):
        cloudlog.debug("Folder search One Drive")
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
        oneresultaat.append(self.oneproc())

        list_cloud_storage_services.append([str(oneresultaat[0]), str(oneresultaat[1]), str(oneresultaat[2])])
        return oneresultaat

    def csearch_spidero(self):
        cloudlog.debug("Folder search SpiderOak")
        if os.path.exists("%s\\SpiderOak" % programfiles):
            spires = "SpideOak installation found in the programfiles"
        else:
            spires = "SpiderOak installation not found"

        if os.path.exists("%s\Documents\SpiderOak Hive" % homefolder):
            spires2 = "SpiderOak folder found in the userfolder"
        else:
            spires2 = "SpiderOak folder not found"

        spiderresultaat = []
        spiderresultaat.append(spires)
        spiderresultaat.append(spires2)
        spiderresultaat.append(self.spiderproc())

        list_cloud_storage_services.append([str(spiderresultaat[0]), str(spiderresultaat[1]), str(spiderresultaat[2])])
        return spiderresultaat

    def csearch_mega(self):
        cloudlog.debug("Folder search MEGA")
        if os.path.exists("%s\\AppData\\Local\\MEGAsync" % homefolder):
            meres = "Mega installation found in the AppData local folder"
        else:
            meres = "Mega installation not found"

        if os.path.exists("%s\\Desktop\\MEGAsync.lnk" % homefolder):
            meres2 = "Mega folder found on the desktop"
        else:
            meres2 = "Mega folder not found"

        megaresultaat = []
        megaresultaat.append(meres2)
        megaresultaat.append(meres)
        megaresultaat.append(self.megaproc())

        list_cloud_storage_services.append([str(megaresultaat[0]), str(megaresultaat[1]), str(megaresultaat[2])])
        return megaresultaat

    def csearch_copy(self):
        cloudlog.debug("Folder search COPY")
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
        copyresultaat.append(self.copyproc())

        list_cloud_storage_services.append([str(copyresultaat[0]), copyresultaat[1], str(copyresultaat[2])])
        return copyresultaat

    # Defs die zoeken in de processenlijst van de Software module
    def dropproc(self):
        cloudlog.debug("Process search Dropbox")
        for process in processes():
            for proc in process:
                if proc == 'Dropbox.exe':
                    dropprores = "Dropbox is active as process"
                else:
                    dropprores = "Dropbox process not found"
        return dropprores

    def boxproc(self):
        cloudlog.debug("Process search Box")
        for process in processes():
            for proc in process:
                if proc == "BoxSync.exe":
                    boxproc = "Box is active as process"
                else:
                    boxproc = "Box process not found"
        return boxproc

    def googleproc(self):
        cloudlog.debug("Process search Google Drive")
        for process in processes():
            for proc in process:
                if proc == "googledrivesync.exe":
                    googleproc = "Google Drive is active as process"
                else:
                    googleproc = "Google Drive processs not found"
        return googleproc

    def oneproc(self):
        cloudlog.debug("Process search One Drive")
        for process in processes():
            for proc in process:
                if proc == "OneDrive.exe" or proc == "SkyDrive.exe":
                    oneproc = "OneDrive and/or SkyDrive is active as process"
                else:
                    oneproc = "OneDrive and/or SkyDrive process not found"
        return oneproc

    def spiderproc(self):
        cloudlog.debug("Process search SpiderOak")
        for process in processes():
            for proc in process:
                if proc == "SpiderOak.exe":
                    spiderproc = "SpiderOak is active as process"
                else:
                    spiderproc = "SpiderOak process not found"
        return spiderproc

    def megaproc(self):
        cloudlog.debug("Process search MEGA")
        for process in processes():
            for proc in process:
                if proc == "MEGAsync.exe":
                    megaproc = "MEGA is active as process"
                else:
                    megaproc = "MEGA process not found"
        return megaproc

    def copyproc(self):
        cloudlog.debug("Process search COPY")
        for process in processes():
            for proc in process:
                if proc == "CopyAgent.exe":
                    copyproc = "Copy is active as process"
                else:
                    copyproc = "Copy process not found"
        return copyproc

