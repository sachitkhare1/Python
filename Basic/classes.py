# class FirstClass :
     
    #  name = "sachit"
    #  number = 585

#      def fun (self) :
#           print ("Hello ", self.name)
#           print ("Marks ",self.number)
        
# obj = FirstClass()
# obj.fun()

#------------------------------------------------
# using _init_ method / constructor
# -----------------------------------------------

#      def __init__(self ,name , num):
         
#          self.name = name
#          self.number = num
        
#      def show (self) :
          
#           print (f"Hello {self.name} your marks {self.number}")
          
    
# obj1 = FirstClass("sachit" ,54)

# obj1.show ()

# print ( obj1.name )

# ----------------------------------------------
# using Getter and setter methods and use of str () it is use for print objects in string format / readable 
# ----------------------------------------------
#     def __init__(self , name) :
#             self.name = name
        
#     def set1(self , number ) :
#           self.number = number

#     def get1 (self) :
#           return self.number


# Obj1 = FirstClass(54)

# Obj1.set1("sachit")

# print (str(Obj1.get1())+" Marks :",str(Obj1.name))

# ---------------------------------------------
# use of Destructors / python has garbage collector like java _del_ method delete all reference object obj when program ends...
# ---------------------------------------------

	# Initializing
# 	def __init__(self):
# 		print("inside the init method.")

# 	# Deleting (Calling destructor)
# 	def __del__(self):
# 		print('Destructor called, Employee deleted.')

# obj = FirstClass()
# del obj

# ---------------------------------
# diamond Problem 
#----------------------------------

class Diamond (object) :
    
    def __init__(self) :
        pass
          
    def show (self):
        print ("inside the diamond class.")

class Base1 (Diamond) :
    
    def __init__(self):
        super().__init__()
    
    def show1(self):
        print ("inside the base1.")
        
class Base2 (Diamond) :
    
    def __init__(self):
         super().__init__()

    def show1(self):
        print("inside the base 2.")
     

class Lastclass(Base1, Base2 ) :
      def __init__(self):
          super().__init__()

      def show(self):
          print("inside the last class.")
           
ba = Lastclass()

print (ba.show1())