import array as arr

a = arr.array ('i' ,[1,2,3,4,5,6])


print ("Array before Insertion :", end="")

for i in range (0,5) :
    print ( a[i] , end=" ")

a.insert(1,22)

print ()

print ("Array after the insertion :", end="")

for i in range (0,6) :
    print (a[i] , end=" ")

a.remove(22)

print()
print ("rr" , end="")
for i in range (0,5) :
    print (a[i], end=" ")

# -------------------------
