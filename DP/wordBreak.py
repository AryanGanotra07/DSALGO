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





if __name__ == "__main__":
    dict = [
        "self", "th", "is", "famous", "Word",
        "break", "b", "r", "e", "a", "k", "br",
        "bre", "brea", "ak", "problem"
    ]
 
    # input String
    str = "Wordbreakproblem"
    print(solve2(str, dict))