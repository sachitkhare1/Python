print ("Starting List and their MEthods :")

em = ["sachit" ,100 , "False"]

print ("NAME : %s , Marks :%d ,Fail : %s " % (em[0], em[1] ,em[2]))

print ("Starting the Methods of Lists")

# Repetation Operator

l=em*2

print (l)

# Concatenation

list1= [8,6,4,6,4]

c = em + list1

print (c)

# length

print ("Length of list1 ",len(list1))
 
# iterating  
for i in list1:   
    print(i)  


# Membeship Operator
# it return ture if number is found in list otherwise return false

print (8 in list1)

print (89 in list1)

# min()
# max()
# remove()
# append()

list1.clear()

# print (list1, "" ,type(list1))

# n = int ( input ("ENTER THE SIZE OF LIST :"))

# for i in range ( 0 , n ):
#     list1.append(input("enter the names of animals :"))

# print("Printing the Name of Animals :")

# for j in list1:
#     print(j)

# print ("Starting Tuples :")

# tuples are immutable and 
# method of tuples 

tuple1 = ("sachit" ,65,9,8,6 )

print(tuple1.count(9))

r = tuple1.index(65)

print(r)

print ("starting Set")

set1 = {"bittoo" , 8, 5, 9, 4}

set2 = {"sachit" , 8, 9, 3, 7}

# set does not allow duplicates values set only allow unique elements and set is immutabel we can only add and remove the elements of set by using
# add() , update () methods and remove elements by using remove() and discard() methods 

set1.add("sachit")

print(set1)

set1.remove(9)

print (set1) 

# union and Intersection methods

print (set1|set2) 

print (set1&set2)

print (set1.union(set2))

print (set2.intersection(set1))

# dictionary
# dictionary are mutable values can be duplicate but key must be unique

dic1={"sachit" : "khare" , 8 :"bittoo" , "hi" : "chalo"}

# deleting elemnts using del and pop keyword 

del dic1[8]

dic1.pop("sachit")

print (dic1)

# any() popitem() clear() sorted() all() values() ,key() 
# tuples inside the list

list2=[]
t= ()
n = int (input("enter the size of tuple :"))

for i in range (0,n):
   
    list2.append(tuple(input("enter the numebr ")))

print(list2, type(list2))