def mergeSort(arr):
    if len(arr) <=1 :
        return 

    m = len(arr)//2
    l = arr[:m]
    h = arr[m:]
    mergeSort(l)
    mergeSort(h)
    i = j = k = 0

    while(i< len(l) and j < len(h)):
        if (l[i] < h[j]):
            arr[k] = l[i]
            i+=1
            k+=1
        else:
            arr[k] = h[j]
            j+=1
            k+=1
        
            
    while i < len(l):
        arr[k] = l[i]
        i+=1
        k+=1
    while( j < len(h)):
        arr[k] = h[j]
        j+=1
        k+=1

a = [4,2,1,41,4,12,4,5]
mergeSort(a)
print(a)


