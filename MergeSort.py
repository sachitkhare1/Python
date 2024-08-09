def merge1 (arr , low , mid , high ) :
    
    n1 = mid - low +1
    n2 = high - mid

    l = [0] *n1 
    r = [0] *n2

    for i in range (n1) :
        
        l[i] = arr [low +i] 

    for i in range (n2) :
         
         r[i] = arr [mid + 1 + i]

    i=0
    j=0
    k=low

    while i < n1 and j < n2:
        if l[i] <= r[j]:
            arr[k] = l[i]
            i += 1
        else:
            arr[k] = r[j]
            j += 1
        k += 1

# copy the remaining elements of l[] 
    while i < n1:
        arr[k] = l[i]
        i += 1
        k += 1

# Copy the remaining elements of r[]
    while j < n2:
        arr[k] = l[j]
        j += 1
        k += 1

def mergeSort(arr , low , high) :
    
    if low < high :
        
        mid = (low + high ) //2

        mergeSort (arr , low , mid)
        mergeSort ( arr , mid +1 , high )
        merge1 (arr , low , mid , high )

def printff (n) :

    for i in n :
      print (i , end= "")
      print ()
   

arr = [ 33 ,55 ,3 ,5 ,25 ]

print ("Before using Merge Sorting :")

printff(arr)

mergeSort(arr , 0 , len(arr)-1)

print ("After the Merge Sorting :")

print(arr)