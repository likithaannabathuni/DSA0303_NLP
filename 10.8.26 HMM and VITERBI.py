
# HMM with Viterbi Algorithm
# Probabilities are calculated automatically

from collections import defaultdict

# Number of training sentences
n = int(input("Enter number of training sentences: "))

data = []

for i in range(n):
    print("\nTraining sentence", i + 1)

    words = input("Enter words: ").split()
    tags = input("Enter tags: ").split()

    data.append((words, tags))


# Count probabilities
initial_count = defaultdict(int)
transition_count = defaultdict(int)
emission_count = defaultdict(int)

tag_count = defaultdict(int)
total_sentences = len(data)

states = set()

for words, tags in data:

    states.update(tags)

    # Initial state count
    initial_count[tags[0]] += 1

    # Count transitions
    for i in range(1, len(tags)):
        transition_count[(tags[i - 1], tags[i])] += 1

    # Count emissions
    for word, tag in zip(words, tags):
        emission_count[(tag, word)] += 1
        tag_count[tag] += 1


states = list(states)

# Calculate initial probabilities
initial_prob = {}

for state in states:
    initial_prob[state] = initial_count[state] / total_sentences


# Calculate transition probabilities
transition_prob = {}

for previous in states:
    for current in states:

        count = transition_count[(previous, current)]

        total = 0

        for state in states:
            total += transition_count[(previous, state)]

        if total == 0:
            transition_prob[(previous, current)] = 0
        else:
            transition_prob[(previous, current)] = count / total


# Calculate emission probabilities
emission_prob = {}

for state in states:
    for word in set(word for words, tags in data for word in words):

        count = emission_count[(state, word)]

        if tag_count[state] == 0:
            emission_prob[(state, word)] = 0
        else:
            emission_prob[(state, word)] = count / tag_count[state]


# User enters test sentence
print("\nEnter sentence to predict:")
test_words = input().split()

# Viterbi algorithm
viterbi = []
backpointer = []

# Initialization
first = {}
first_path = {}

for state in states:

    emission = emission_prob.get((state, test_words[0]), 0)

    first[state] = initial_prob[state] * emission
    first_path[state] = [state]

viterbi.append(first)
backpointer.append(first_path)


# Recursion
for word in test_words[1:]:

    current = {}
    current_path = {}

    for state in states:

        emission = emission_prob.get((state, word), 0)

        best_probability = 0
        best_previous = None

        for previous in states:

            probability = (
                viterbi[-1][previous]
                * transition_prob.get((previous, state), 0)
                * emission
            )

            if probability > best_probability:
                best_probability = probability
                best_previous = previous

        current[state] = best_probability

        if best_previous is not None:
            current_path[state] = (
                backpointer[-1][best_previous] + [state]
            )

    viterbi.append(current)
    backpointer.append(current_path)


# Find best final state
final_state = max(viterbi[-1], key=viterbi[-1].get)

best_path = backpointer[-1][final_state]

print("\nInput sentence:", test_words)
print("Most likely tags:", best_path)
print("Probability:", viterbi[-1][final_state])

