def part (arr , low , high) :
     
    pivot = arr[high]
    i = low -1

    for j in range (low , high):
         if arr[j] < i :

            i+=i
            arr[i] ,arr[j] = arr[j], arr[i]
    arr[i+1], arr [high] = arr[high] , arr[i+1]
    return  i+1


def quicksort (arr , low , high) :
    
    if low < high :
        #   index

          pi = part (arr , low , high)
          quicksort (arr , low , pi -1)
          quicksort (arr , pi+1 ,high )
       
def printArray (ar) :

    for i in ar :
        print (ar, end="")
        print()     

ar = [78,98,32,65,95,14,32]

print ("Print the elements before Sorting : ")

printArray(ar)
print()

print ("print the Elements after the sorting :")
    
quicksort( ar , 0 , len(ar)-1)

printArray (ar)
print()