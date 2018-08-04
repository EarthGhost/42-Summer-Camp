import sys

word = sys.argv[1]

def capitalize(s):
    ret = " "
    i = False  # capitalize
    for char in s:
        if i:
            ret += char.upper()
        else:
            ret += char.lower()
        if char != ' ':
            i = not i
    return ret

cap = capitalize(word) #calling function foo

def Vowel(string):
    vowels = 'AEIOU'
    res = string
    for char in res:
        if char in vowels:
            res = res.replace(char, '*')
    return res

def matched(str):
    count = 0
    for i in str:
        if i == "(":
            count += 1
        elif i == ")":
            count -= 1
    if count != 0:
        print("Balanced? False")
    elif count == 0:
        print ("Balanced? True")


print(cap)
print(Vowel(cap))
matched(cap)
        #replace the capital leters to aestrisk
#print the strin 
