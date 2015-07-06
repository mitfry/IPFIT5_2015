__author__ = 'Andre'

import os

from PyQt4 import QtGui

def outputfolder():
    #Hier wordt er geselecteerd waar het project opgeslagen mag worden.
    outputfolder = str(
        QtGui.QFileDialog.getExistingDirectory(None, 'Sla project op in: ', 'C:\\', QtGui.QFileDialog.ShowDirsOnly))
    return str(outputfolder)

def save_project(locatie, project, onderzoeker, datum):
    #Deze functie slaat het project daadwerkelijk op. Er wordt een bestand aangemaakt met de gegevens over het project zelf.
    #Er wordt een if/else statement gebruikt omdat het programma mogelijk errors geeft als de opgegeven map al bestaat.
    if os.path.exists(locatie):
        outputlog = open(locatie + '\Projectgegevens.txt', 'w')
        outputlog.write("Projectnaam: " + project + "\n" + "Onderzoeker: "+ onderzoeker + "\n" + "datum aangemaakt: " +datum)
        outputlog.close()

    else:
        os.makedirs(locatie)
        outputlog = open(locatie + '\Projectgegevens.txt', 'w')
        outputlog.write("Projectnaam: " + project + "\n" + "Onderzoeker: "+ onderzoeker + "\n" + "datum aangemaakt: " +datum)
        outputlog.close()

def save_casus(locatie2, casus, identiteit, tijd):
    if os.path.exists(locatie2):
        outputlog = open(locatie2 + '\Casusgegevens.txt', 'w')
        print type(tijd)
        outputlog.write("Casusnaam: " + casus + "\n" + "Identificatienummer apparaat: "+ identiteit + "\n" + "Tijd aangemaakt: " + tijd)
        outputlog.close()
    else:
        os.makedirs(locatie2)
        outputlog = open(locatie2 + '\Casusgegevens.txt', 'w')
        print type(tijd)
        outputlog.write("Casusnaam: " + casus + "\n" + "Identificatienummer apparaat: "+ identiteit + "\n" + "Tijd aangemaakt: " + tijd)
        outputlog.close()
    return



