with open("names.txt") as f:
    content = f.readlines()

first_names = {}
last_names = {}

for word in content:
    f,l = word.split(',')
    l = l.strip('\n')
    if f in list(first_names.keys()):
        first_names[f].append(l)
    else:
        first_names[f] = [l]

    if l in list(last_names.keys()):
        last_names[l].append(f)
    else:
        last_names[l] = [f]

print("** Shared First Names **")
for key,val in first_names.items():
    if len(val) > 1:
        print(key,' (',len(val),'): ',val,sep='')

print("* Shared Last Names **")
for key,val in last_names.items():
    if len(val) > 1:
        print(key,' (', len(val),'): ',val,sep='')


