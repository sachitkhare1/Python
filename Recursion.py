# direct Recursion

# def fact (n) :
    
#     if n<=1 :
#         return 1
#     else :
#         return n*fact(n-1)
  
# print (fact (5))

# -----------------------------
# Indirect Recursion
# ------------------------------

def fact1 (n) :

    if n<=1 :
      
         return 1
        
    else :
        return n*fact1 (n-1)
    
def Input1 () :
   
    n= int (input ("Enter the number : " ))
    
    if  n > 1 :
     
     return fact1(n)

    else :
      return 1

print(Input1())

