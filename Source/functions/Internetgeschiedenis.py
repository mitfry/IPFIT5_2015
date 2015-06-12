# Locaties
# Chrome historie: C:\Users\Gebruiker\AppData\Local\Google\Chrome\User Data\Default\history
# C:\Users\Gebruiker\AppData\Local\Google\Chrome\User Data\Default\GPUCache (Nog niet bekeken)

# Informatie over de chrome database
# http://lowmanio.co.uk/blog/entries/how-google-chrome-stores-web-history/
# Firefox
# http://lowmanio.co.uk/blog/entries/how-firefox-stores-web-history/
# Internet Explorer
# http://www.lowmanio.co.uk/blog/entries/how-internet-explorer-stores-web-history/

# Imports
import sqlite3  # This library is used to read the history files.
from os.path import expanduser  # This library is used to find the location of the history files.
import os

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

    pathPart1 = expanduser("~")

    firefoxFolder =  os.listdir(pathPart1 + '/AppData/Roaming/Mozilla/Firefox/Profiles')

    # Making the connection with the history database

    # connectionFirefox = sqlite3.connect("E:\Bibliotheken\python\Firefox\places.sqlite")


    # Setting the cursor. This is the variable we use to execute the SQL query.



    outputList = []  # List for the output. All history entries are stored in here.

    # Executing the SQL query and storing the results. Only importing the browsers that the user selected
    if chrome == 1:
        connectionChrome = sqlite3.connect(pathPart1 + '\AppData\Local\Google\Chrome\User Data\Default\history')
        cursorChrome = connectionChrome.cursor()
        for row in cursorChrome.execute(sqlSelectChrome):
            listT = ["Chrome", str(row[0]), row[1], str(row[2]), row[3]]  # Storing each result in a list.
            outputList.append(listT)  # Storing the list with results in the output list.
    if firefox == 1:
        connectionFirefox = sqlite3.connect(pathPart1 + '/AppData/Roaming/Mozilla/Firefox/Profiles/' + firefoxFolder[0] + '/places.sqlite')
        cursorFireFox = connectionFirefox.cursor()
        for row in cursorFireFox.execute(sqlSelectFirefox):
            listT = ["Firefox", str(row[0]), row[1], str(row[2]), row[3]]  # Storing each result in a list.
            outputList.append(listT)  # Storing the list with results in the output list.
    outputListSorted = sorted(outputList, key=lambda tup: tup[2], reverse=True)  # Sorting the list by date and storing it.
    return outputListSorted

# Showing the most visited websites. The user specifies how many.
def showMostVisited(outputListSorted, numberOfResults):
    searchResults = []
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
            if searchResult[4].find(searchWord) != -1:
                searchResults.append(searchResult)
            elif searchResult[3].find(searchWord) != -1:
                searchResults.append(searchResult)
        except AttributeError:
            pass  # It's possible for a field to be empty. This try statement makes the program skip the entry.
    return searchResults

