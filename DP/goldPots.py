def solve(a, i, j):
    if i == j:
        return a[i]
    if i+1==j:
        return max(a[i], a[j])
    s = a[i] + min(solve(a, i+2, j), solve(a, i+1, j-1))
    e = a[j] + min(solve(a, i+1, j-1), solve(a, i, j-2))
    return max(s,e)


if __name__ == '__main__':
 
    # pots of gold (even number) arranged in a line
    coin = [4, 6, 2, 3]
 
    print("Maximum coins collected by player is", 
          solve(coin, 0, len(coin) - 1))
