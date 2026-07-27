'''from nltk.stem import PorterStemmer

ps = PorterStemmer()

words = input("Enter words separated by space: ").split()

print("\nOriginal Word\tStem Word")
print("-" * 30)

for word in words:
    print(word, "\t\t", ps.stem(word))'''


'''from nltk.stem import PorterStemmer

ps = PorterStemmer()

words = ["caresses", "ponies", "running", "studies",
         "relational", "happiness", "connected"]

print("Original Word\tStem Word")
print("-" * 35)

for word in words:
    stem = ps.stem(word)
    print(word, "\t", stem)'''

from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer
import nltk

nltk.download('punkt')

ps = PorterStemmer()

file = open("sample.txt", "r")
text = file.read()
file.close()

words = word_tokenize(text)

print("Original Words")
print(words)

print("\nStemmed Words")

for word in words:
    print(word, "->", ps.stem(word))

