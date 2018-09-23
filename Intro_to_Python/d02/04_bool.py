l1 = [False,True,True,None,True,None,None,False,False,None,True,False]
l2 = ["or","or","or","==","!=","==","and","==","!=","and","!=","and"]
l3 = [False,False,None,None,True,True,False,True,None,False,True,None]
i = 0

#while i < 12:
 #  print(l1[i], end=' ')
  # print(l2[i], end=' ')
  # print(l3[i], end=' => ')
  # i += 1

for i in range(0, len(l1)):
    a = l1[i]
    b = l3[i]

    if l2[i] == "or":
        print ("%r %s %r  => %r" % (l1[i] , l2[i] , l3[i] , a or b))
    elif l2[i] == "and":
        print ("%r %s %r  => %r" % (l1[i] , l2[i] , l3[i] , a and b))
    elif l2[i] == "!=": 
        print ("%r %s %r  => %r" % (l1[i] , l2[i] , l3[i] , a != b))
    elif l2[i] == "==":
        print ("%r %s %r  => %r" % (l1[i] , l2[i] , l3[i] , a == b))

   # answer = l1[i] + l2[i] + l3[i]
    #print (l1[i] + l2[i] + l3[i] , ' => ' , answer)
