import nltk

text = "The cat is sleeping"

words = nltk.word_tokenize(text)
tags = nltk.pos_tag(words)

print(tags)
