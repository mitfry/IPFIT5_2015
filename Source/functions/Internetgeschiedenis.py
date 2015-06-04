# Locaties
# Chrome historie: C:\Users\Gebruiker\AppData\Local\Google\Chrome\User Data\Default\history
# C:\Users\Gebruiker\AppData\Local\Google\Chrome\User Data\Default\GPUCache (Nog niet bekeken)

# Informatie over de chrome database
# http://lowmanio.co.uk/blog/entries/how-google-chrome-stores-web-history/

# Imports
import sqlite3

# Connectie maken met de database
conn = sqlite3.connect('E:\Bibliotheken\python\Internet_geschiedenis\History')

# Deze variable gebruik je verder
c = conn.cursor()

f = open('workfile.txt', 'w')
x = 0

# SQL query
sql_select = """ SELECT datetime(last_visit_time/1000000-11644473600,'unixepoch','localtime'),
                        visit_count, url
                 FROM urls
                 ORDER BY last_visit_time DESC
             """

urlList = []

# SQL query uitvoeren en resultaten opslaan in een list.
for row in c.execute(sql_select):
    if x < 1000:
        output = '[Tijd] ' + row[0] + ' [Aantal keer bezocht] ' + str(row[1]) + ' [URL] ' + row[2]
        # print(output)
        # f.write(output + '\n')
        listT = [str(row[0]), row[1], str(row[2])]
        urlList.append(listT)
    x += 1

sorted_by_second = sorted(urlList, key=lambda tup: tup[1], reverse=True)

y = 0

# List wegschrijven naar een txt bestand.
for item in sorted_by_second:
    if y < 100:
        output = '[Tijd] ' + item[0] + ' [Aantal keer bezocht] ' + str(item[1]) + ' [URL] ' + item[2]
        f.write(output + '\n')
        y += 1
f.close()
