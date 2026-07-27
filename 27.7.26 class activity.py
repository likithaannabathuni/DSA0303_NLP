from collections import Counter

corpus = """
I love NLP
I love Python
I study NLP
You love NLP
We study Python
I study Python
"""

tokens = corpus.lower().split()

unigram_counts = Counter(tokens)

bigrams = []
for i in range(len(tokens) - 1):
    bigrams.append((tokens[i], tokens[i + 1]))

bigram_counts = Counter(bigrams)

total_words = len(tokens)

print("Tokens:")
print(tokens)

print("\nUnigram Frequency Counts:")
for word, count in unigram_counts.items():
    print(f"{word}: {count}")

print("\nBigram Frequency Counts:")
for bg, count in bigram_counts.items():
    print(f"{bg}: {count}")

print("\nUnigram Probabilities:")
for word, count in unigram_counts.items():
    print(f"P({word}) = {count}/{total_words} = {count/total_words:.4f}")

print("\nBigram Probabilities (MLE):")
for (w1, w2), count in bigram_counts.items():
    probability = count / unigram_counts[w1]
    print(f"P({w2}|{w1}) = {count}/{unigram_counts[w1]} = {probability:.4f}")

w1 = input("\nEnter first word: ").lower()
w2 = input("Enter second word: ").lower()

if (w1, w2) in bigram_counts:
    probability = bigram_counts[(w1, w2)] / unigram_counts[w1]
    print(f"\nBigram ({w1}, {w2}) exists.")
    print(f"Probability = {probability:.4f}")
else:
    print(f"\nBigram ({w1}, {w2}) does not exist.")
    print("Probability = 0")
