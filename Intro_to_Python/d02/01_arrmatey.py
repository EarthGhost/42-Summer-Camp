import sys

args = sys.argv
total = len(args)

for i in range(total):
    print("Argv of " + str(i) + " is " + sys.argv[i])

args.sort(key=len)
args.reverse()
for i in range(total):
    print(args[i])


