import sys
import os 
from collections import defaultdict
basedir = os.path.dirname(__file__)
reldir = "./capitols.txt"
full_fp = os.path.join(basedir, reldir)
cap_list = defaultdict(list)
with open(full_fp) as txtfile:
    for i in txtfile:
        (key, val) = i.rstrip('\n').split(",")
        cap_list[key].append(val)
infin = 1
while infin == 1:
    state = input("Ready: ")
    if state in cap_list:
        cap = cap_list[state]
        print(', '.join(cap))
    elif state.lower() == "done":
        print("Exit")
        break
    else:
        print("nil")

#with open("capitols.txt") as c:
 #   content = c.readlines()


