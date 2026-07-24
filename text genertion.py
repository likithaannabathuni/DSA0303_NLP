text = "I love NLP I love Python I love AI"

words = text.split()

bigrams = {}

for i in range(len(words) - 1):
    bigrams[words[i]] = words[i + 1]

word = "I"

print(word, end=" ")

for i in range(5):
    if word in bigrams:
        word = bigrams[word]
        print(word, end=" ")
