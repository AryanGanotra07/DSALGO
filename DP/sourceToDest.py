
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
# DP function to calculate the minimum cost to reach the destination city n
# from the source city 0
def findMinCost(cost):
 
    # lookup[i] stores the minimum cost to reach city i from city 0
    lookup = [None] * N
 
    # Initialize lookup with the direct ticket price from the source city
    for i in range(N):
        lookup[i] = cost[0][i]
 
    # repeat loop till lookup is filled with all minimum values
    isFilled = False
    while not isFilled:
        isFilled = True
 
        # fill lookup in bottom-up manner
        for i in range(N):
            for j in range(N):
                if lookup[i] > lookup[j] + cost[j][i]:
                    lookup[i] = lookup[j] + cost[j][i]
                    isFilled = False
 
    # return the minimum cost to reach city N-1 from city 0
    return lookup[N - 1]
 
 
if __name__ == '__main__':
 
    cost = [
        [0, 25, 20, 10, 105],
        [20, 0, 15, 80, 80],
        [30, 15, 0, 70, 90],
        [10, 10, 50, 0, 100],
        [40, 50, 5, 10, 0]
    ]
 
    N = len(cost)
    print("The minimum cost is", findMinCost(cost))
 