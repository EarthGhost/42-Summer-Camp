import sys

n= int(sys.argv[1])
base = int(sys.argv[2])
convertString = "0123456789ABCDEFJHIJKLMNOPQRSTUVWXYZ"

def toStr(n,base):
    if n < base: 
        return convertString[n]
    else:
        return toStr(n//base,base) + convertString[n%base]

print(toStr(n, base))
