__author__ = 'Hugo Faas'

# Imports
import sqlite3  # This library is used to read the history files.
from os.path import expanduser  # This library is used to find the location of the history files.
import os  # Used to create the path to the history files.
import csv  # Used to save the results as a csv file.

# SQL query's
sqlSelectChrome = """ SELECT datetime(last_visit_time/1000000-11644473600,'unixepoch','localtime'),
                        visit_count, url, title
                 FROM urls
                 ORDER BY last_visit_time DESC
             """

sqlSelectFirefox = """ SELECT datetime(last_visit_date/1000000-11644473600,'unixepoch','localtime'),
                        visit_count, url, title
                 FROM moz_places
                 ORDER BY last_visit_date DESC
             """

outputListSorted = []

# Loading all the history data into a list
def loadData(internetExplorer, firefox, chrome):

    pathPart1 = expanduser("~")  # Creating the first part of the path to the internet history.

    outputList = []  # List for the output. All history entries are stored in here.

    # Executing the SQL query and storing the results. Only importing the browsers that the user selected
    if chrome == 1:
        try:
            connectionChrome = sqlite3.connect(pathPart1 + '\AppData\Local\Google\Chrome\User Data\Default\history')
            cursorChrome = connectionChrome.cursor()
            for row in cursorChrome.execute(sqlSelectChrome):
                listT = ["Chrome", str(row[0]), row[1], str(row[2]), row[3]]  # Storing each result in a list.
                outputList.append(listT)  # Storing the list with results in the output list.
        except sqlite3.OperationalError:  #  If chrome is opened, the history can't be read. An exception is shown at
        # the top of the results list in the interface.
            listT = ["Chrome", "", "999999", "De Chrome geschiedenis database is in gebruik. Sluit Chrome en probeer"
                                             "het opnieuw.", ""]
            outputList.append(listT)

    if firefox == 1:
        firefoxFolder = os.listdir(pathPart1 + '/AppData/Roaming/Mozilla/Firefox/Profiles')
        connectionFirefox = sqlite3.connect(pathPart1 + '/AppData/Roaming/Mozilla/Firefox/Profiles/' + firefoxFolder[0]
                                            + '/places.sqlite')
        cursorFireFox = connectionFirefox.cursor()
        for row in cursorFireFox.execute(sqlSelectFirefox):
            listT = ["Firefox", str(row[0]), row[1], str(row[2]), row[3]]  # Storing each result in a list.
            outputList.append(listT)  # Storing the list with results in the output list.
    outputListSorted = sorted(outputList, key=lambda tup: tup[2], reverse=True)  # Sorting the list by date and storing
    # it.
    return outputListSorted

# Showing the most visited websites. The user specifies how many.
def showMostVisited(outputListSorted, numberOfResults):
    searchResults = []

    # numberOfResults contains the number of results that the user wants to see, entered through the interface.
    # 1 is subtracted for every result that is output and once it hits 0, it stops showing lines.
    for item in outputListSorted:
        if numberOfResults > 0:
            searchResults.append(item)
            numberOfResults -= 1
    return searchResults

# The user can enter a search word, which the program will search for in the urls and website titles. Case-sensitive.
def searchData(outputListSorted, searchWord):
    searchResults = []

    for searchResult in outputListSorted:
        try:
            if searchResult[4].find(searchWord) != -1:  # See it the word is in the title of the current result.
                searchResults.append(searchResult)
            elif searchResult[3].find(searchWord) != -1:  # See if the word is in the url of the current result.
                searchResults.append(searchResult)
        except AttributeError:
            pass  # It's possible for a field to be empty. This try statement makes the program skip that entry.
    return searchResults

def saveData(casusLocatie, browser, titel, aantal_keer, laatst_bezocht, url):

    outputfolder = str(casusLocatie)  # The case location is sent from interface_thram.py and contains the location
    # where all case related files should be saved.

    # Every time the user executes one of the 3 options, the results are saved to a file. The while loop below ensures
    # a new file is used for every user action.
    bestandNummer = 0
    while True:
        if os.path.isfile(outputfolder + '\ ' + "internetgeschiedenis" + str(bestandNummer) + ".csv"):
            bestandNummer += 1
        else:
            csvFile = open(outputfolder + '\ ' + "internetgeschiedenis" + str(bestandNummer) + ".csv", 'a')
            writer = csv.writer(csvFile, delimiter=',', quoting=csv.QUOTE_ALL)
            break

    # Lists containing the results are sent from interface_thram.py. These are written to the file selected above with
    # the code below.
    aantal = 0
    while aantal < len(browser):
        try:
            writer.writerow((browser[aantal], titel[aantal], aantal_keer[aantal], laatst_bezocht[aantal], url[aantal]))
        except UnicodeEncodeError:
            pass  # To ensure the program doesn't stop when this error comes up.
        aantal += 1
    csvFile.close()

