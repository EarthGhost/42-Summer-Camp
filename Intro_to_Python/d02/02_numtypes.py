import sys
num1 = int(sys.argv[1])
num2 = int(sys.argv[2])

answer = num1 // num2
remain = num1 % num2
print("{} divided by {} equals {} remainder {}".format(num1, num2, answer, remain))
a = int(10) 
b = float(56.99)
c = complex(2,3)

if type(a) is int:
    atype = 'Integer'
    print("Variable a contains : {} which is of type: {}".format(a, atype))


if type(b) is float:
    atype = 'Float'
    print("Variable a contains : {} which is of type: {}".format(b, atype))

if type(c) is complex:
    atype = 'Complex'
    print("Variable a contains : {} which is of type: {}".format(c, atype))
