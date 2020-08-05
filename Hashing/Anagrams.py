def anagrams(A):
    temp = [str(sorted(list(A[i]))) for i in range(len(A))]
    dict = {}
    for i in range(len(temp)):
        if temp[i] in dict:
            dict[temp[i]].append(i+1)
        else:
            dict[temp[i]] = [i+1]
    return list(dict.values())