import string

word = input("Enter word here:\n")

def remove_punct(word):
    return "".join(i.lower() for i in word if i in string.ascii_letters)

def palindrome(s):
    forward = remove_punct(s)
    rev = forward[::-1]
    if forward == rev:
        print("True")
    else:
        print ("False")

palindrome(word)
