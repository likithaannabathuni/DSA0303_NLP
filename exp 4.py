import nltk
nltk.download('punkt')
from collections import Counter
from nltk import CFG
from nltk.parse import ChartParser

# -----------------------------
# UNSMOOTHED N-GRAM MODEL
# -----------------------------

corpus = """
I love NLP
I love Python
I study NLP
You love NLP
We study Python
I study Python
"""

tokens = corpus.lower().split()

print("Tokens:")
print(tokens)

# Unigram Counts
unigrams = Counter(tokens)

# Bigram Counts
bigrams = []
for i in range(len(tokens) - 1):
    bigrams.append((tokens[i], tokens[i + 1]))

bigram_counts = Counter(bigrams)

print("\nUnigram Frequency")
for word, count in unigrams.items():
    print(word, ":", count)

print("\nBigram Frequency")
for bg, count in bigram_counts.items():
    print(bg, ":", count)

print("\nUnigram Probabilities")
total = len(tokens)

for word in unigrams:
    print("P({}) = {:.4f}".format(word, unigrams[word] / total))

print("\nBigram Probabilities (MLE)")
for (w1, w2), count in bigram_counts.items():
    prob = count / unigrams[w1]
    print("P({}|{}) = {:.4f}".format(w2, w1, prob))

print("\nCheck Bigram")

w1 = input("Enter first word: ").lower()
w2 = input("Enter second word: ").lower()

if (w1, w2) in bigram_counts:
    prob = bigram_counts[(w1, w2)] / unigrams[w1]
    print("Bigram Exists")
    print("Probability =", round(prob, 4))
else:
    print("Bigram Does Not Exist")
    print("Probability = 0")

# -----------------------------
# CFG PARSE TREE
# -----------------------------

grammar = CFG.fromstring("""
S -> NP VP
NP -> Pronoun | ProperNoun
VP -> Verb NP
Pronoun -> 'i' | 'you' | 'we'
ProperNoun -> 'nlp' | 'python'
Verb -> 'love' | 'study'
""")

parser = ChartParser(grammar)

print("\nEnter a sentence for parsing")
sentence = input().lower().split()

print("\nParse Tree:")

found = False

for tree in parser.parse(sentence):
    print(tree)
    tree.pretty_print()
    found = True

if not found:
    print("No valid parse tree found.")
