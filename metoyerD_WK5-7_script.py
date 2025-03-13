'''
Devante Metoyer
02/23/25
Assignment #7
Assignment - Extract e-mail address anf urls from the memory dump provided

'''

import re
from prettytable import PrettyTable

# File Chunk Size
CHUNK_SIZE = 4096

# Regular expression patterns (as byte strings)
emailPatt = re.compile(b'[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,4}')
urlPatt = re.compile(b'\w+:\/\/[\w@][\w.:@]+\/?[\w.\.?=%&=\-@$,]*')

# Create empty dictionaries to count occurrences
emailDict = {}
urlDict = {}

# Read in the binary file (change filename as needed: mem.raw, memdump.bin, or test.bin)
with open('mem.raw', 'rb') as binaryFile:
    while True:
        chunk = binaryFile.read(CHUNK_SIZE)
        if chunk:
            # Find all emails and URLs in the current chunk
            emails = emailPatt.findall(chunk)
            urls = urlPatt.findall(chunk)
            
            # Count email occurrences
            for eachEmail in emails:
                eachEmail = eachEmail.lower()
                try:
                    value = emailDict[eachEmail]
                    emailDict[eachEmail] = value + 1
                except KeyError:
                    emailDict[eachEmail] = 1
            
            # Count URL occurrences
            for eachURL in urls:
                eachURL = eachURL.lower()
                try:
                    value = urlDict[eachURL]
                    urlDict[eachURL] = value + 1
                except KeyError:
                    urlDict[eachURL] = 1
        else:
            break

# Build and display the email table
emailTable = PrettyTable(['Occurrences', 'E-Mail Address'])
for key, value in emailDict.items():
    emailTable.add_row([value, key.decode("ascii", "ignore")])

print("EMAILS: Sorted by Occurrence")
emailTable.align = "l"
print(emailTable.get_string(sortby="Occurrences", reversesort=True))
print("\n\n")

# Build and display the URL table
urlTable = PrettyTable(['Occurrences', 'URL'])
for key, value in urlDict.items():
    urlTable.add_row([value, key.decode("ascii", "ignore")])

print("URLS: Sorted by Occurrence")
urlTable.align = "l"
print(urlTable.get_string(sortby="Occurrences", reversesort=True))
