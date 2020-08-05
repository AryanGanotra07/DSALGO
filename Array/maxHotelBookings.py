def solve(arrive, depart, K):
    arrive.sort()
    depart.sort()
    for i in range(len(arrive)):
        if i + K < len(arrive) and arrive[i+K] < depart[i]:
            return 0
    return 1

print(solve([1, 3, 5], [2, 6, 8], 2))