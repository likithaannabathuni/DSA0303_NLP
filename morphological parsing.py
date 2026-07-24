word = input("Enter a word: ")

state = 0

for ch in word:
    if state == 0:
        if ch == 'i':
            state = 1
    elif state == 1:
        if ch == 'n':
            state = 2
        else:
            state = 0
    elif state == 2:
        if ch == 'g':
            state = 3
        else:
            state = 0

if state == 3:
    print("Valid suffix 'ing' found")
else:
    print("Suffix 'ing' not found")
