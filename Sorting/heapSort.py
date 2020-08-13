def heapify(a, n, i):
    largest = i
    left = 2*i + 1
    right = 2*i + 2
    if left < n and  a[largest] < a[left]:
        largest = left
    if right < n and  a[largest] < a[right]:
        largest = right
    if largest!=i:
        a[largest] , a[i] = a[i], a[largest]
        heapify(a, n, largest)
    

def heapsort(a):
    n = len(a)
    for i in range(n//2 - 1, -1, -1):
        heapify(a, n, i)

    for i in range(n-1, 0, -1):
        a[i], a[0] = a[0], a[i]
        heapify(a, i, 0)

    

    pass

a = [1,4,2,2,5,6,12,4]
heapsort(a)
print(a)