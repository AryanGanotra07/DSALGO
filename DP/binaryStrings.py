def solve(n, ld):
    if n==0:
        return 0
    if n==1:
        return 1 if ld == 1 else 2
    if ld == 0:
        return solve(n-1, 1) + solve(n-1, 0)
    return solve(n-1, 0)


if __name__ == "__main__":
    n  = 5
    print(solve(5, 0))