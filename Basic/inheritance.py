# class Person (object) :
    
#     def __init__(self , name , age) :
        
#         self.name = name 
#         self.age = age
    
#     def show (self) :
       
#        print (f"inside the Person class : name = {self.name} and age = {self.age}")

# class Emp (Person):

#     def __init__(self,name , age , id , address) :
        
#         self.id = id
#         self.address =address

#         Person.__init__(self ,name , age)

#     def display (self) :

#         print (f"""     Name = {self.name}
#        Age = {self.age}
#        Emp Id = {self.id}
#        Address = {self.address}""")

# obj = Emp("Sachit khare" , 22 , 3 , "Bhola Ram" )
# obj.display()


# -------------------------
# using super keyword..// single level inheretance...
# -------------------------
# class Person (object) :
    
#     def __init__(self , name , age) :
        
#         self.name = name 
#         self.age = age
    
#     def show (self) :
       
#        print (f"inside the Person class : name = {self.name} and age = {self.age}\n")

# class Emp (Person):

#     def __init__(self,sname , age , id , address) :
#         self.sname = sname
#         self.age = age
#         self.id = id
#         self.address =address

#         super().__init__("bittoo" , 22)

#     def display (self) :

#         print (f" Name = {self.sname} Age = {self.age} Emp Id = {self.id} Address = {self.address}")

# obj = Emp("sachit", 22 , 3 , "Bhola Ram" )
# obj.show()
# obj.display()

# -----------------------------------------------
# Multi-level inheretance...
# -----------------------------------------------

# class base (object):
    
#     def __init__(self) :
#         self.name = input("enter the name : ")
    
#     def showbase (self) :
#         print ("inside the base class Name =",self.name)


# class base2 (base) :
  
#     def __init__(self):
        
#         super().__init__()
#         self.age = input ("enter the age :")

#     def showbase2 (self):
#         print (f"Name ={self.name} and Age = {self.age}")


# class drived1 (base2) :
      
#       def __init__(self):
          
#           super().__init__()
#           self.address = input ("enter the Adress :")

#       def showDerived (self):
         
#           print (f"Name :{self.name} Age :{self.age} Address : {self.address}")

# dd = drived1 ()

# dd.showbase()
# dd.showbase2()
# dd.showDerived()

# -------------------------------------------------
# Multiple inheretance...
# -------------------------------------------------

class base ():
    
    def __init__(self) :
        self.name = input("enter the name : ")
    
    def showbase (self) :
        print ("inside the base class Name =",self.name)


class base2 () :
  
    def __init__(self):
        self.age = input ("enter the age :")

    def showbase2 (self):
        print ( f"Age = {self.age}")


class drived1 (base ,base2) :
      
      def __init__(self):
          
          base.__init__(self)
          base2.__init__(self)
          self.address = input ("enter the Adress :")

      def showDerived (self):
         
          print (f"Name :{self.name} Age :{self.age} Address : {self.address}")

dd = drived1 ()

dd.showbase()
dd.showbase2()
dd.showDerived()

# --------------------------------------------
# hierarchical inheretance
# Hybrid inheretance
# --------------------------------------------







