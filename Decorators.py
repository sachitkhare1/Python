# function return function
from functools import wraps
# def text(tx):
#     return tx.upper()

# print (text("Hello Ayush sir"))

# --------------------------------------------------

# passing function as arguments 

# def Upper1 (text):
#     return text.upper()

# def Lower1 (text):
#     return text.lower()

#  The function_call function takes a single argument function, which is expected to be a function object.

# def greet (func ):
#     greeting = func("Learning Decorators...")
#     print (greeting)

# greet(Upper1)
# greet(Lower1)

# ----------------------------------------------

# add_13 it is a variable/ object create for create_adder


# show("sachit")


# def create_adder (x):
#     def adder (y):
#         return x+y
#     return adder

# add_13 = create_adder (15)

# print ( add_13 (10))


# def repeat(n) : 
     
#      def decorators1(func) :
#           def Wrapper (*args ,**kwargs) :
#                for _ in range (n) :
#                    func (*args,**kwargs)
#           return Wrapper
#      return decorators1

# @repeat(4)
# def show (name) :
#      print(f"Hello {name}")



