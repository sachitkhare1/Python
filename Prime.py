def check_Prime (number) :
    if number <= 1 :
        return False
    else:
        for j in range (2 , number):
            if number % j == 0:
                return False
            else:
                return True

number = int (input ("Enter the number :"))

if check_Prime( number ):
    print(" The Given number is Prime Number.")
else:
    print("The the given number is not a Prime Number.")
 
