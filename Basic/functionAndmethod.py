#  Method overloading and Overriding
# overloading.......

class Load :
   
   def my_method (self , *args , **kwargs) :
      
    print (f"Positional arguments :{args}")
    print (f"keyword arguments :{kwargs}")


obj = Load()
obj.my_method(1,2,3,54, x=4, fk =5)

