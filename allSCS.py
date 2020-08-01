
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
28
29
30
31
32
33
34
35
36
37
38
39
40
41
42
43
44
45
46
47
48
49
50
51
52
53
54
55
56
57
58
59
60
61
62
63
64
65
66
67
68
69
70
71
72
73
74
75
76
77
78
79
80
81
82
83
84
85
86
87
88
89
90
91
92
93
94
95
96
97
98
99
100
101
102
103
104
105
106
107
108
109
110
# Function to return all SCS of substrings X[0..m-1], Y[0..n-1]
def SCS(X, Y, m, n):
 
    # if we have reached the end of first string, create a list
    # containing second substring and return
    if m == 0:
        return [Y[:n]]
 
    # if we have reached the end of second string, create a list
    # containing first substring and return
    elif n == 0:
        return [X[:m]]
 
    # if last character of X and Y is same, it should occur
    # only one time in SSC
    if X[m - 1] == Y[n - 1]:
 
        # find all SCS of substring X[0..m-2], Y[0..n-2]
        scs = SCS(X, Y, m - 1, n - 1)
 
        # append current character X[m - 1] or Y[n - 1] to all SCS of
        # substring X[0..m-2] and Y[0..n-2]
 
        return [str + X[m - 1] for str in scs]
 
    # we reach here when the last character of X and Y don't match
 
    # if top cell of current cell has more value than the left cell,
    # then append current character of string X to all SCS of
    # substring X[0..m-2], Y[0..n-1]
 
    if lookup[m - 1][n] > lookup[m][n - 1]:
 
        scs = SCS(X, Y, m - 1, n)
        return [str + X[m - 1] for str in scs]
 
    # if left cell of current cell has more value than the top cell,
    # then append current character of string Y to all SCS of
    # substring X[0..m-1], Y[0..n-2]
 
    if lookup[m][n - 1] > lookup[m - 1][n]:
 
        scs = SCS(X, Y, m, n - 1)
        return [str + Y[n - 1] for str in scs]
 
    # if top cell value is same as left cell, then go in both
    # top and left directions
 
    # append current character of string X to all SCS of
    # substring X[0..m-2], Y[0..n-1]
    top = SCS(X, Y, m - 1, n)
 
    # append current character of string Y to all SCS of
    # substring X[0..m-1], Y[0..n-2]
    left = SCS(X, Y, m, n - 1)
 
    return [str + X[m - 1] for str in top] + [str + Y[n - 1] for str in left]
 
 
# Function to fill lookup table by finding the length of LCS
# of substring X[0..m-1] and Y[0..n-1]
def LCS(X, Y, m, n):
 
    # first row and first column of the lookup table are already 0
 
    # fill the lookup table in bottom-up manner
    for i in range(1, m + 1):
 
        for j in range(1, n + 1):
            # if current character of X and Y matches
            if X[i - 1] == Y[j - 1]:
                lookup[i][j] = lookup[i - 1][j - 1] + 1
            # else if current character of X and Y don't match
            else:
                lookup[i][j] = max(lookup[i - 1][j], lookup[i][j - 1])
 
 
# Function to find all Shortest Common SuperSequence of string X and Y
def findSCS(X, Y):
 
    m = len(X)
    n = len(Y)
 
    # fill lookup table
    LCS(X, Y, m, n)
 
    # find all longest common sequences
    A = SCS(X, Y, m, n)
 
    # since list can contain duplicates, "convert" the list to Set
    scs = set(A)
 
    # return set containing all SCS
    return scs
 
 
if __name__ == '__main__':
 
    X = "ABCBDAB"
    Y = "BDCABA"
 
    # lookup[i][j] stores the length of LCS of substring X[0..i-1], Y[0..j-1]
    lookup = [[0 for x in range(len(Y) + 1)] for y in range(len(X) + 1)]
 
    # Find all Shortest Common SuperSequence of string X and Y
    scs = findSCS(X, Y)
 
    # print all SCS present in the Set
    print("All Shortest Common Supersequence of", X, "and", Y, "are:", scs)
 