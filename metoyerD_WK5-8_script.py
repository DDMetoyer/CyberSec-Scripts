'''
Devante Metoyer
02/23/25
Assignment #8
Assignment - Process a memory dump and extract all relevant strings

'''

import re
from prettytable import PrettyTable

# File Chunk Size
CHUNK_SIZE = 4096

# Regular expression pattern for continuous alphabetical strings (5-12 characters)
word_pattern = re.compile(r'[a-zA-Z]{5,12}')

# Dictionary to store the unique words and their occurrence counts
wordDict = {}

# Open the binary memory dump file (change filename as needed)
with open('memdump.bin', 'rb') as binaryFile:
    while True:
        chunk = binaryFile.read(CHUNK_SIZE)
        if not chunk:
            break
        
        # Decode the binary chunk into text; ignore any decoding errors
        text = chunk.decode('ascii', errors='ignore')
        
        # Find all matching words in the decoded text
        words = word_pattern.findall(text)
        
        for word in words:
            # Normalize to lowercase for consistent counting
            word = word.lower()
            if word in wordDict:
                wordDict[word] += 1
            else:
                wordDict[word] = 1

# Create a PrettyTable to display the results
table = PrettyTable(['Occurrences', 'Unique Word'])

for word, count in wordDict.items():
    table.add_row([count, word])

# Align the table to the left and print it sorted by Occurrences (highest first)
table.align = "l"
print(table.get_string(sortby="Occurrences", reversesort=True))
