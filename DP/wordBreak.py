def solve(s,d, out=""):
    if not s:
        print(out)
        return 
    for i in range(1, len(s)+1):
        pr = s[:i]
        if pr in d:
            solve(s[i:], d, out + " " + pr)
def solve2(s,d):
    if not s:
        return True
    for i in range(1, len(s)+1):
        pr = s[:i]
        if pr in d and solve2(s[i:],d):
            return True
    return False

def wordBreak(dict, str, lookup):
 
    # n stores length of current substring
    n = len(str)
 
    # return true if we have reached the end of the String
    if n == 0:
        return True
 
    # if sub-problem is seen for the first time
    if lookup[n] == -1:
 
        # mark sub-problem as seen (0 initially assuming String
        # can't be segmented)
        lookup[n] = 0
 
        for i in range(1, n + 1):
            # consider all prefixes of current String
            prefix = str[:i]
 
            # if prefix is found in dictionary, then recur for suffix
            if prefix in dict and wordBreak(dict, str[i:], lookup):
                # return true if the can be segmented
                lookup[n] = 1
                return True
 
    # return solution to current sub-problem
    return lookup[n] == 1





if __name__ == "__main__":
    dict = [
        "self", "th", "is", "famous", "Word",
        "break", "b", "r", "e", "a", "k", "br",
        "bre", "brea", "ak", "problem"
    ]
    
 
    # input String
    str = "Wordbreakproblem"
    lookup = [-1] * (len(str) + 1)
    print(wordBreak(dict,str, lookup))