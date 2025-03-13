
'''
Devante Metoyer
02/01/25
Assignment 3
Assignment - File Hashing
'''

'''
Complete the script below to do the following:
1) Add your name, date, assignment number to the top of this script
2) Using the os library and the os.walk() method 
   a) Create a list of all files
   b) Create an empty dictionary named fileHashes 
   c) Iterate through the list of files and
      - calculate the md5 hash of each file
      - create a dictionary entry where:
        key   = md5 hash
        value = filepath
    d) Iterate through the dictionary
       - print out each key, value pair in a PrettyTable format
    
3) Submit
   NamingConvention: lastNameFirstInitial_Assignment_.ext
   for example:  alharthiD_WK1_script.py
                 alharthiD_WK1_screenshot.jpg
   A) Screenshot of the results in WingIDE
   B) Your Script
'''

import os
import hashlib
# Import PrettyTable for output formatting
from prettytable import PrettyTable 

directory = "." 

file_list   = []
file_hashes = {}

# Walk the path from top to bottom.
# For each file obtain the filename
for root, dirs, files in os.walk(directory):
    for file_name in files:
        path = os.path.join(root, file_name)
        full_path = os.path.abspath(path)
        
        # Calculate MD5 hash
        hasher = hashlib.md5()
        try:
            with open(full_path, "rb") as f:
                while chunk := f.read(4096):
                    hasher.update(chunk)
            file_hash = hasher.hexdigest()
            file_hashes[file_hash] = full_path  # Store hash as key, file path as value
        except Exception as e:
            print(f"Error hashing {full_path}: {e}")

# Display results in a PrettyTable format
table = PrettyTable(["MD5 Hash", "File Path"])
for hash_key, file_path in file_hashes.items():
    table.add_row([hash_key, file_path])

print(table)
