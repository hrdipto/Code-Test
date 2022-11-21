word = input("Insert Word >")

reverse_word = word[-1::-1]

if len(word):
    if word == reverse_word:
        print("True")
    else:
        print("False")
else:
    print("Type something!")