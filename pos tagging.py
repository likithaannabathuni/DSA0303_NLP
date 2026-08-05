import nltk
from nltk.tokenize import word_tokenize
from nltk import pos_tag

# Download required resources (run only once)
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')

# Input sentence
sentence = input("Enter a sentence: ")

# Tokenize the sentence
tokens = word_tokenize(sentence)

# Perform POS tagging
tagged = pos_tag(tokens)

# Display tokens
print("\nTokens:")
print(tokens)

# Display POS tags
print("\nPOS Tags:")
for word, tag in tagged:
    print(f"{word} --> {tag}")
