
'''
Devante Metoyer
02/01/25
Assignment 2
Week Two Assignment - File Processing
'''

'''
Complete the script below to do the following:
1) Add your name, date, and assignment number to the top of this script
2) Open the file redhat.txt 
   a) Iterate through each line of the file
   b) Split eachline into individual fields (hint str.split() method)
   c) Examine each field of the resulting field list
   d) If the word "worm" appears in the field then add the worm name to the set of worms
   e) Once you have processed all the lines in the file
      sort the set 
      iterate through the set of worm names
      print each unique worm name 
3) Submit
   NamingConvention: lastNameFirstInitial_Assignment_.ext
   for example:  alharthiD_WK2-1_script.py
                 alharthiD_WK2-2_screenshot.jpg
   A) Screenshot of the results in WingIDE
   B) Your Script
'''

import os

unique_worms = set()

with open("redhat.txt", 'r') as log_file:
    for each_line in log_file:
        print(each_line)
        ''' your code starts here '''
        fields = each_line.strip().split()
        for field in fields:
            if "worm" in field.lower():
                unique_worms.add(field)
print("#2e, Print each worm name")
sorted_worms = sorted(unique_worms)

print("Unique worms found:")
for worm in sorted_worms:
    print(worm)