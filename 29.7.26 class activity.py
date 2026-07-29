# Unigram and Bigram Laplace Smoothing in NLP

from collections import Counter

# Training Corpus
corpus = [
    "Students learn NLP",
    "Students learn python",
    "Students write code",
    "Teachers teach NLP",
    "Teachers teach python"
]

# -----------------------------
# Tokenization
# -----------------------------
tokens = []
for sentence in corpus:
    words = sentence.lower().split()
    tokens.extend(words)

# Vocabulary
vocab = sorted(set(tokens))
V = len(vocab)

print("Vocabulary:", vocab)
print("Vocabulary Size =", V)

# -----------------------------
# Unigram Counts
# -----------------------------
unigram_counts = Counter(tokens)
N = len(tokens)

print("\nUnigram Counts")
print(unigram_counts)

# -----------------------------
# Bigram Counts
# -----------------------------
bigram_counts = Counter()

for sentence in corpus:
    words = sentence.lower().split()
    for i in range(len(words) - 1):
        bigram_counts[(words[i], words[i + 1])] += 1

print("\nBigram Counts")
print(bigram_counts)

# -----------------------------
# Unigram Laplace Smoothing
# Formula:
# P(word) = (Count(word)+1)/(Total Words + Vocabulary Size)
# -----------------------------
def unigram_probability(word):
    count = unigram_counts[word.lower()]
    return (count + 1) / (N + V)

# -----------------------------
# Bigram Laplace Smoothing
# Formula:
# P(word2|word1) =
# (Count(word1,word2)+1)/(Count(word1)+Vocabulary Size)
# -----------------------------
def bigram_probability(word1, word2):
    bigram_count = bigram_counts[(word1.lower(), word2.lower())]
    unigram_count = unigram_counts[word1.lower()]
    return (bigram_count + 1) / (unigram_count + V)

# -----------------------------
# Unigram Probabilities
# -----------------------------
print("\nUnigram Smoothed Probabilities")

uni_words = [
    "students",
    "teachers",
    "learn",
    "write",
    "python",
    "nlp",
    "teach",
    "code"
]

for word in uni_words:
    count = unigram_counts[word]
    prob = unigram_probability(word)
    print(f"P({word}) = ({count}+1)/({N}+{V}) = {prob:.4f}")

# -----------------------------
# Bigram Probabilities
# -----------------------------
print("\nBigram Smoothed Probabilities")

pairs = [
    ("students", "learn"),
    ("students", "write"),
    ("learn", "code"),
    ("teach", "python"),
    ("write", "nlp")
]

for w1, w2 in pairs:
    bcount = bigram_counts[(w1, w2)]
    ucount = unigram_counts[w1]
    prob = bigram_probability(w1, w2)
    print(f"P({w2}|{w1}) = ({bcount}+1)/({ucount}+{V}) = {prob:.4f}")
