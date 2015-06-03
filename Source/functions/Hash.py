import hashlib
import os


def calculate_hash_from_multiplee_files():
    full_path = raw_input("In welke map moeten de sha256 hashes berekend worden? > ")
    count = 0
    output = open(raw_input("Where would you like to store the hashes?\n> "), 'w')
    output.write("The sha256 files of" + full_path + '  are:\n\n')
    for root, dirs, files in os.walk(full_path):
        for file_name in files:
            count += 1
            line = str(str(count) + root + '/' + file_name + ' is       ' + hashlib.sha256(
                open(root + '/' + file_name, 'rb').read()).hexdigest() + '\n')
            output.write(line)
    output.close()


calculate_hash_from_multiplee_files()
