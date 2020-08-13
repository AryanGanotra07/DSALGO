def partition(arr, low, high):
    i = ( low )         # index of smaller element 
    print(i)
    pivot = arr[high]     # pivot 
  
    for j in range(low , high): 
  
        # If current element is smaller than the pivot 
        if   arr[j] < pivot: 
          
            # increment index of smaller element 
           
            arr[i],arr[j] = arr[j],arr[i] 
            i = i+1 
    print(arr)
  
    arr[i],arr[high] = arr[high],arr[i] 
    return ( i) 
    

def quickSort(a, l, h):
    if l < h:
        p = partition(a, l, h)
        
        quickSort(a, l, p-1)
        quickSort(a, p+1, h )


a  = [ 1,2,3,2,4,5,6,1]
quickSort(a, 0, len(a)-1)
print(a)