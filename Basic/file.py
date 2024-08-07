
# using loop

a = []

t = (1,5,6,8,5,8)

# for i in t:
#     a.append(i)

a= list(t)

print(a)

tuple1 = tuple(a)

print (tuple1)

s = set (a)
 
print (s)

# --------------------------------

l1 = []

l2 = []

for i in range(0, 3):
    
    l1.append(int (input("enter the Numbers :")))

    l2.append(input("Enter the Name :"))

c = list ( zip (l1 , l2))

print (c)
    
# d= dict(key , values)