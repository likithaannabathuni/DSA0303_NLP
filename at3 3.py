import re

# Input text
text = input("Enter the text:\n")

while True:
    print("\n------ MENU ------")
    print("1. Search Date")
    print("2. Search Phone Number")
    print("3. Search Hashtag")
    print("4. Search Mention")
    print("5. Search Prefix")
    print("6. Search Suffix")
    print("7. Search Word")
    print("8. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        result = re.findall(r'\b\d{2}/\d{2}/\d{4}\b', text)
        print("Dates:", result if result else "No Date Found")

    elif choice == 2:
        result = re.findall(r'\b[6-9]\d{9}\b', text)
        print("Phone Numbers:", result if result else "No Phone Number Found")

    elif choice == 3:
        result = re.findall(r'#\w+', text)
        print("Hashtags:", result if result else "No Hashtag Found")

    elif choice == 4:
        result = re.findall(r'@\w+', text)
        print("Mentions:", result if result else "No Mention Found")

    elif choice == 5:
        prefix = input("Enter Prefix: ")
        result = re.findall(r'\b' + re.escape(prefix) + r'\w*\b', text)
        print("Matching Words:", result if result else "No Match Found")

    elif choice == 6:
        suffix = input("Enter Suffix: ")
        result = re.findall(r'\b\w*' + re.escape(suffix) + r'\b', text)
        print("Matching Words:", result if result else "No Match Found")

    elif choice == 7:
        word = input("Enter Word: ")
        result = re.findall(r'\b' + re.escape(word) + r'\b', text)
        print("Word Found:", result if result else "Word Not Found")

    elif choice == 8:
        print("Program Ended.")
        break

    else:
        print("Invalid Choice!")
