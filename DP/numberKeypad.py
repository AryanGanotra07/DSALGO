# The function returns false if (i, j) is not a valid position
def isValid(i, j):
 
    # for handling '*' or '#' (present in 4th row and 1st & 3rd column)
    if i == 3 and (j == 0 or j == 2):
        return False
 
    return 0 <= i <= 3 and 0 <= j <= 2
 
 
# Function to fill a dict that stores the mapping of cells
# reachable from current cell
def fillDictionary(keypad):
 
    # Below lists details all 4 possible movements from current cell
    row = [0, -1, 0, 1]
    col = [-1, 0, 1, 0]
 
    # do for each row
    for i in range(4):
 
        # do for each column of row i
        for j in range(3):
 
            # move in all four possible directions of current digit key[i][j]
            for k in range(4):
 
                r = i + row[k]
                c = j + col[k]
 
                # insert adjacent cell to dictionary if valid
                if isValid(i, j) and isValid(r, c):
                    k = ord(key[i][j]) - 48
                    v = ord(key[r][c]) - 48
                    keypad.setdefault(k, []).append(v)
 
 
# Function to count all numbers starting from digit i and
# having length n
def getCount(keypad, i, n, lookup):
    if n == 1:  # reached end of digit
        return 1
 
    # if sub-problem is seen for the first time, solve it and
    # store its result in an list
    if lookup[i][n] == 0:
 
        # recur for digit i
        lookup[i][n] = getCount(keypad, i, n - 1, lookup)
 
        # recur for all digits reachable from i
        for e in keypad.get(i):
            lookup[i][n] += getCount(keypad, e, n - 1, lookup)
 
    # return the subproblem solution
    return lookup[i][n]
 
 
if __name__ == '__main__':
 
    # Maximum N-digit number allowed
    N = 8
 
    # mobile keypad
    key = [
        ['1', '2', '3'],
        ['4', '5', '6'],
        ['7', '8', '9'],
        ['*', '0', '#']
    ]
 
    n = 2
 
    # use a dict to store mapping of cells reachable from current cell
    keypad = {}
    fillDictionary(keypad)
 
    # create a lookup table to store solutions of sub-problems lookup[i][j]
    # stores count of all numbers starting from digit i having length n
    lookup = [[0 for x in range(N)] for y in range(10)]
 
    # get count of of each digit
    count = 0
    for i in range(10):
        count += getCount(keypad, i, n, lookup)
 
    print("Total possible combinations are", count)