def mergeSort(arr):
    if len(arr) <=1 :
        return 0
    cnt = 0
    m = len(arr)//2
    l = arr[:m]
    h = arr[m:]
    cnt += mergeSort(l)
    cnt += mergeSort(h)
    i = j = k = 0

    while(i< len(l) and j < len(h)):
        if (l[i] <= h[j]):
            arr[k] = l[i]
            i+=1
            k+=1
        else:
            arr[k] = h[j]
            j+=1
            k+=1
            cnt+=(mid-i)
        
            
    while i < len(l):
        arr[k] = l[i]
        i+=1
        k+=1
    while( j < len(h)):
        arr[k] = h[j]
        j+=1
        k+=1
    return cnt

a = [1, 20, 6, 4, 5] 
print(mergeSort(a))
print(a)


