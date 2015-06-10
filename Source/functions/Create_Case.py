__author__ = 'Roland'

import sys, os

def write():

    #providing name for the file to be created
    Case_File = raw_input("Give name for the Case File: ")
    target = open (Case_File, 'a') ## a will append, w will over-write

    #providing the content for the file
    print "Fill in the following information for the New Case"
    print ""
    Case_Name = raw_input("Enter Case Name: ");
    Investigator = raw_input("Enter Investigator's name: ");
    Organization = raw_input("Enter Organization: ");
    Contact = raw_input("Enter Contact Details: ");
    print ""

    #writing the entered content to the file we just created

    target.write(Case_Name)
    target.write(" ")
    target.write(Investigator)
    target.write(" ")
    target.write(Organization)
    target.write(" ")
    target.write(Contact)
    target.write(" ")

    target.close()

     # Here do I make a folder named "The given Case_File name" & Show the path where this is made.
    path = os.path.join(os.path.expanduser('~'), 'Documents', 'Cases', Case_File)+'.txt' # Path to the folder for any user / +'.txt' Name of text file coerced with +.txt
    os.makedirs(path) # Make the folder
    print (path) # Show the folder path

write()


'''print "New Case"

print "Case_Name: ", Case_Name
print "Investigator: ", Investigator
print "Organization: ", Organization
print "Contact Details: ", Contact




mode = 'a' if os.path.exists(writepath) else 'w'
with open(writepath, mode) as f:
    f.write('Hello, world!\n')


def write():
    print('Creating new text file')

    name = input('Enter name of text file: ')+'.txt'  # Name of text file coerced with +.txt

    try:
        file = open(name,'a')   # Trying to create a new file or open one
        file.close()

    except:
        print('Something went wrong! Can\'t tell what?')
        sys.exit(0) # quit Python

write()'''