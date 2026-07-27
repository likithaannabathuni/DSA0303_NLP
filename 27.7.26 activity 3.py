from collections import Counter

corpus = """
<s> I love NLP </s>
<s> I love Python </s>
<s> I study NLP </s>
<s> We study Python </s>
<s> You love NLP </s>
<s> We love AI </s>
<s> I study Machine Learning </s>
<s> Students learn NLP </s>
"""

tokens = corpus.lower().split()

unigram_counts = Counter(tokens)

bigrams = [(tokens[i], tokens[i + 1]) for i in range(len(tokens) - 1)]
bigram_counts = Counter(bigrams)

trigrams = [(tokens[i], tokens[i + 1], tokens[i + 2]) for i in range(len(tokens) - 2)]
trigram_counts = Counter(trigrams)

total_words = len(tokens)

print("Tokens:")
print(tokens)

print("\nTotal Words:", total_words)
print("Unique Unigrams:", len(unigram_counts))
print("Unique Bigrams:", len(bigram_counts))
print("Unique Trigrams:", len(trigram_counts))

print("\nUnigram Frequency Counts")
for word, count in unigram_counts.items():
    print(word, ":", count)

print("\nBigram Frequency Counts")
for bg, count in bigram_counts.items():
    print(bg, ":", count)

print("\nTrigram Frequency Counts")
for tg, count in trigram_counts.items():
    print(tg, ":", count)

print("\nUnigram Probabilities")
for word, count in unigram_counts.items():
    print(f"P({word}) = {count}/{total_words} = {count/total_words:.4f}")

print("\nBigram Probabilities (MLE)")
for (w1, w2), count in bigram_counts.items():
    prob = count / unigram_counts[w1]
    print(f"P({w2}|{w1}) = {count}/{unigram_counts[w1]} = {prob:.4f}")

first = input("\nEnter first word of bigram: ").lower()
second = input("Enter second word of bigram: ").lower()

if (first, second) in bigram_counts:
    prob = bigram_counts[(first, second)] / unigram_counts[first]
    print("\nBigram exists.")
    print("Probability =", round(prob, 4))
else:
    print("\nBigram does not exist.")
    print("Probability = 0")

word = input("\nEnter one word for next word prediction: ").lower()

possible = {}

for (w1, w2), count in bigram_counts.items():
    if w1 == word:
        possible[w2] = count / unigram_counts[w1]

if possible:
    print("\nPossible next words:")
    for w, p in possible.items():
        print(w, ":", round(p, 4))
    prediction = max(possible, key=possible.get)
    print("Predicted next word:", prediction)
else:
    print("No prediction possible.")

w1 = input("\nEnter first word: ").lower()
w2 = input("Enter second word: ").lower()

possible = {}

for (a, b, c), count in trigram_counts.items():
    if a == w1 and b == w2:
        possible[c] = count / bigram_counts[(a, b)]

if possible:
    print("\nPossible next words:")
    for w, p in possible.items():
        print(w, ":", round(p, 4))
    prediction = max(possible, key=possible.get)
    print("Predicted next word:", prediction)
else:
    print("No prediction possible.")
