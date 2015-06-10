import sys
import os.path

#!/usr/local/bin/python
#Root folder van user
sys.path.append(sys.path[0]+"/../modules")

rootfolder = os.path.expanduser("~")
programfiles = os.environ['PROGRAMFILES']

class email:
    def email():
        '''if os.path.exists("%s\\Dropbox" % programfiles):
                print "Dropbox installation found"
            elif os.path.exists("%s\\AppData\\Roaming\\Dropbox" % homefolder):
                print "Dropbox installation found"
            else:
                pass

            if os.path.exists("%s\\Dropbox" % homefolder):
                print "Dropbox folder found"
            else:
                pass


if __name__ == '__main__':
    CloudSearch()
    print homefolder
    print programfiles'''
