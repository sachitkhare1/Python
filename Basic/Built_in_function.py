# abs() function return the absolute value 

n = -32
v = -25.258

print (" The Function Return the absolute value : ",abs(n))

print (" The Function Return the absolute value : ",abs(v))

# all() function It returns true if all items in passed iterable are true. 

a = [ 3,4,5,6 ]
b = { 2,5,False }
c = ( 0, False )

# for dictionary your key will be False then all() method return False value 
print ("Starting all Function")

d = {"sachit" : 100 , "false" : 5656 ,False : "False"}

print (all(a))
print (all(b))
print (all(c))
print (all(d))

# bin() function is used to return the binary representation of a specified integer.
# always starts with the prefix 0b
print ( " Starting bin Function ")
x = 10
y = bin(x)

print (" Binary :",y)

# bool() converts a value to boolean(True or False) using the standard truth testing procedure
print (" Staring bool Function ")

a = []

print ( bool(a) )
 
b="sachit"

print ( bool(b))

c= None

print ( bool(c))

# bytes() in Python is used for returning a bytes object. It is an immutable version of the bytearray() function
print("Starting bytes funtion ")

x = "Saksham"

array= bytes(x,'utf-8')

print(array)

# sum() function is used to get the sum of numbers of an iterable
#  sum() function only takes two arguments
s = sum ( [5,6,2] , 4 )

print (s)

# any() function returns true if any item in an iterable is true. Otherwise, it returns False.
# any() just Opposite of all()
print ("Starting any function ")

an = [ 2,3,5,6,8 ]

print (any(an))

# ascii() function returns a string containing a printable representation of an object and escapes the non-ASCII characters in the string using \x, \u or \U escapes

normal= "sachit khare"

print (ascii(normal))

other= "sachit f08"

print (ascii(other))

