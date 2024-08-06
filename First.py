print ("This Program check the Given number is Palindrom or not :- ")
number=int(input("Enter the number: "))

p=number

s=0

while number!=0:
    remainder = number % 10
    s = s *10 + remainder
    number//= 10


if p == s:
 print(f"Palindrom :{s}")

else :
 print(f"Not a Palindrom : {p} ")