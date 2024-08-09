# class DecoratorsClass :
#     def __init__(self) -> None:
#         pass
        
#     def Print (func) :
#         def show ( *args , **kwargs) :

#             print ("inside the Decorators Class.")

#             result = func (*args ,**kwargs) 

#             print ("after the Decorators function of Decorators class.")

#             return result
#         return show


def insert_list () :
    l = []
    n = int (input ("enter the the size of list :") )

    for i in range (n) :
       element = int (input ("enter the elements of list : "))
       l.append(element)
    return l
    
li = []

def calling () :
    
    
    c = int (input ("enter the size of List :"))

    for i in range (c) :
        e = insert_list() 
        li.append(e)
   
calling()
print (li)