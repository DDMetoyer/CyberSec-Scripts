'''
Simple String Searching:
1) Convert the string to all lower case
2) Count the number characters in the string
3) Count the number of words in the string
4) Sort the words in alphabetical order
5) Search the excerpt variable given below
   For the following and report how many occurances of each are found
   scandal
   arrested
   er
   good
   tomorrow
'''

excerpt = " Another one got caught today, it's all over the papers. Teenager Arrested in Computer Crime Scandal, Hacker Arrested after Bank Tampering kids. They're all alike"

''' Your work starts here '''

print("#2, Convert the string to all lower case")
print(excerpt.lower())

print("#3, Count the number characters in the string")
print(len(excerpt))

print("#4, Count the number of words in the string")
words = excerpt.split()
word_count = len(words)
print(f"The sentence has {word_count} words.")

print("#5, Sort the words in alphabetical order")
alphabetical_order = sorted(words, key=str.lower)
print("Words in alphabetical order", alphabetical_order)

print("#6, Search the excerpt variable given")
words_to_search = ["scandal", "arrested", "er", "good", "tomorrow"]
search = excerpt.lower().replace(',', '')
new = search.split()
occurrence = {word: 0 for word in words_to_search}
for word in new:
    if word in occurrence:
        occurrence[word] += 1
for word in words_to_search:
    print(f"'{word}': {occurrence[word]} times")
