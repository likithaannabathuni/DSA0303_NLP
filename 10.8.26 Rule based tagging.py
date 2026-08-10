import re
def rule_based_pos_tag(sentence):
    words = sentence.split()
    tagged_words = []
    for word in words:
        # Remove punctuation
        clean_word = re.sub(r'[^\w]', '', word)
        lower_word = clean_word.lower()
        # Rule 1: Determiners
        if lower_word in ["a", "an", "the"]:
            tag = "DT"
        # Rule 2: Pronouns
        elif lower_word in ["i", "you", "he", "she", "it", "we", "they"]:
            tag = "PRP"
        # Rule 3: Prepositions
        elif lower_word in ["in", "on", "at", "by", "with", "from", "to"]:
            tag = "IN"
        # Rule 4: Conjunctions
        elif lower_word in ["and", "or", "but", "because"]:
            tag = "CC"
        # Rule 5: Helping verbs
        elif lower_word in ["is", "am", "are", "was", "were", "be", "been"]:
            tag = "VB"
        # Rule 6: Words ending with "ing"
        elif lower_word.endswith("ing"):
            tag = "VBG"
        # Rule 7: Words ending with "ly"
        elif lower_word.endswith("ly"):
            tag = "RB"
        # Rule 8: Words ending with "ed"
        elif lower_word.endswith("ed"):
            tag = "VBD"
        # Rule 9: Common adjectives
        elif lower_word in ["good", "bad", "big", "small", "beautiful", "quick"]:
            tag = "JJ"
        # Rule 10: Words ending with "s"
        elif lower_word.endswith("s"):
            tag = "NNS"
        # Rule 11: Default rule - noun
        else:
            tag = "NN"
        tagged_words.append((clean_word, tag))
    return tagged_words
# Get input from user
sentence = input("Enter a sentence: ")
# Perform POS tagging
result = rule_based_pos_tag(sentence)
print("\nRule-Based POS Tags:")
for word, tag in result:
    print(word, "->", tag)
