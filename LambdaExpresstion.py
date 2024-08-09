

# l =lambda x : 2 if (x<3 ) else x


# print (l(1))

# -----------------------------------------------------------
# nested lambda function

# List = [[2,3,4],[1, 4, 16, 64],[3, 6, 9, 12]]

# sortList = lambda x: (sorted(i) for i in x)

# secondLargest = lambda x, f : [y[len(y)-2] for y in f(x)]  # does not under stands 

# res = secondLargest(List, sortList)

# print(res)

# ---------------------------------------------------------

# using filter 

li =[2,32,44,50,64,65,74,83,72]

ff = list (filter (lambda age :(age >18) , li ))

print (ff)

# ----------------------------------------------------------

# using map function

l = [2,43,4,6,5]

gd = list ( map ((lambda x : (x*2)), l)) 

print (gd)

# ----------------------
# using reduce method of functool 

from functools import reduce

l1 = [ 3 , 4, 6, 3, 2, 34 ]

bb = reduce ((lambda x ,y: x+y) ,l1)

print (bb)

