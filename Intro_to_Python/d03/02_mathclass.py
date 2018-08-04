import sys 

l1 = sys.argv[1:]
sort  = sorted(l1,key=int)
total = len(sort)

final = []
for i in sort:
    i = int(i)
    final.append(i)

def maximum(lst):
     print("Max: {}".format(lst[-1]))
maximum(final)

def minmum(lst):
    print("Min: {}".format(lst[0]))
minmum(final)

def range(lst):
        print("range: {}".format(lst[-1] - lst[0]))
range(final)

def median(sort):
    sorted_nums = sorted(final)
    length_n = len(final)
    middle = length_n // 2 
    if length_n % 2 == 0:
        median_even = (sorted_nums[middle - 1] + sorted_nums[middle]) / 2
        return(median_even)
    else:
        return(sorted_nums[middle])
print('Median:', median(final))

def mean(lst):
    average = sum(lst) / total
    print("mean: {}".format(average))
mean(final)

def mode(lst):
    print('mode: ', end = '')
    print(max(set(lst), key=lst.count))
mode(sort)


