def maximize(arr, n):
    first  = [float('-inf')]*(len(A)+1)
    second = [float('-inf')]*(n)
    third = [float('-inf')]*(n-1)
    fourth = [float ('-inf')]*(n-2)

    for i in reversed(range(len(A))):
        first[i] = max(first[i+1], arr[i])
    for i in reversed(range(len(A)-1)):
        second[i] = max(second[i+1], first[i+1]-arr[i])
    for i in reversed(range(len(A)-2)):
        third[i] = max(third[i+1], second[i+1]+arr[i])
    for i in reversed(range(len(A)-3)):
        fourth[i] = max(fourth[i+1], third[i+1]-arr[i])
    return fourth[0]


if __name__ == '__main__':
    A = [3,9,10,1,30,40]
    print(maximize(A, len(A)))