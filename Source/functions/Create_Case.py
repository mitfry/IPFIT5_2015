__author__ = 'Roland'

import os

# def write():

print 'Creating a new case'

# providing name for the file to be created
case_file = open(raw_input("Type a name for the Case File: ")+'.txt', 'w')  # a will append, w will over-write

# providing the content for the file

case_name = raw_input("Enter Case Name: ")
investigator = raw_input("Enter investigator's name: ")
organization = raw_input("Enter organization: ")
contact = raw_input("Enter contact Details: ")
print "\n"

# writing the entered content to the file we just created

case_file.write("Case Name:     " + case_name)
case_file.write("\n")
case_file.write("Investigator:  " + investigator)
case_file.write("\n")
case_file.write("Organization:  " + organization)
case_file.write("\n")
case_file.write("Contact:       " + contact)
case_file.write("\n")

case_file.close()

# Here do I make a folder named "The given case_file name" & Show the path where this is made.
# path = os.path.join(os.path.expanduser('~'), 'Documents', 'Cases', case_file)  # Cr. path to the folder for any user
# os.makedirs(path)  # Make the folder
# print (path)  # Show the folder path

# write()

