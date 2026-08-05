import nltk

# Run only once
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger_eng')

sentence = input("Enter a sentence: ")

words = nltk.word_tokenize(sentence)
tags = nltk.pos_tag(words)

for word, tag in tags:
    if tag.startswith("NN"):
        print(word, "- Noun")
    elif tag.startswith("PRP") or tag.startswith("WP"):
        print(word, "- Pronoun")
    elif tag.startswith("VB"):
        print(word, "- Verb")
    elif tag.startswith("JJ"):
        print(word, "- Adjective")
    elif tag.startswith("RB"):
        print(word, "- Adverb")
    elif tag == "CC":
        print(word, "- Conjunction")
