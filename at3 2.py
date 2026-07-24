# DFA Simulator

# DFA Description
states = input("Enter states (space separated): ").split()
alphabet = input("Enter input alphabet (space separated): ").split()

print("\nEnter Transition Table:")
transition = {}

for state in states:
    transition[state] = {}
    for symbol in alphabet:
        next_state = input(f"Transition ({state}, {symbol}) -> ")
        transition[state][symbol] = next_state

initial_state = input("\nEnter Initial State: ")
final_states = input("Enter Final States (space separated): ").split()

# Number of strings
n = int(input("\nEnter number of input strings: "))

for i in range(n):
    string = input(f"\nEnter String {i+1}: ")

    current_state = initial_state
    path = [current_state]
    valid = True

    for ch in string:
        if ch not in alphabet:
            valid = False
            break
        current_state = transition[current_state][ch]
        path.append(current_state)

    print("Transition Path:")
    print(" → ".join(path))

    if valid and current_state in final_states:
        print("Accepted")
    else:
        print("Rejected")
