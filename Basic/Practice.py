# converting the 2 lists into dictionary
tup = (1,2,3,4,5,6)

list2 = [ 9,8,7,6,5,4]

dic1 = {}

# dic1 = {list2[i] : list2[ i + 1 ] for i in range (0 , len(list2) , 2) }

# print( "dictionary :" , dic1)



# -----------------------------------------------

# for i in range ( 0 , len( list2 ) , 2) :
    
#      dic1 [ list2 [i] ] = list2 [ i+1 ]

# print ( "dictionary :" , dic1)

# for i in range (0 , len(tup) ,2 ) :
#     dic1 [ tup [i] ] = tup [ i + 1 ]

# print ( "dictionary :" , dic1)

it = iter (tup)

dic1 = dict(zip (it , it))

for i in dic1 :
    print (i)

# list3 = list(tup)

# tup1 = set(list2)

# print ( tup1)

# Decorators

# def print1 (func) :
    
#     print(func("hello"))

# def upp (text) :
#     return text.upper()
    
# print1 (upp)

# def gr (func) :
#     def jj () :
#         print ("function start.")
       
#         func()
#         print ( " after function.")

    
#     return jj

# def used ():
#     print (" inside the function.")

# used = gr (used)

# used ()