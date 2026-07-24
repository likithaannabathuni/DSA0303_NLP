import re

text = input("Enter a sentence: ")
pattern = input("Enter a word to search: ")

match_result = re.match(pattern, text)

if match_result:
    print("Match found at the beginning of the text.")
else:
    print("No match at the beginning.")

search_result = re.search(pattern, text)

if search_result:
    print("Search successful!")
    print("Pattern found at position:", search_result.start())
else:
    print("Pattern not found.")
