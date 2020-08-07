
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
# Function to calculate total number of ways to achieve given
# sum with n throws of dice having k faces
def count(n, k, sum):
 
    # if desired sum is reached with n dices
    if n == 0:
        return sum == 0
 
    # desired sum can't be reached with current configuration
    if sum < 0 or k * n < sum or n > sum:
        return 0
 
    # if sub-problem is seen for the first time, solve it and
    # store its result in a list or map
    if lookup[n][sum] == 0:
        # recur for all possible solutions
        for i in range(1, k + 1):
            lookup[n][sum] += count(n - 1, k, sum - i)
 
    # return solution to current sub-problem
    return lookup[n][sum]
 
 
if __name__ == '__main__':
 
    n = 4        # n throws
    k = 6        # values 1 - 6
 
    sum = 15     # desired sum
 
    # create a lookup table to store solutions of sub-problems
    # lookup[i][j] stores number of ways to achieve sum j
    # with j throws of given dice.
    lookup = [[0 for x in range(sum + 1)] for y in range(n + 1)]
 
    print("Total number of ways are", count(n, k, sum))