def scramble(a, b):
    if a == b:
        return True
    if len(a) <= 1:
        return False
    for k in range(1, len(a)):
        c1 = scramble(a[0:k], b[k :]) and scramble(a[k:], b[0:k])
        c2 = scramble(a[0:k], b[0:k]) and scramble(a[k:], b[k:])
        if c1 or c2:
            return True
    return False


if __name__ == "__main__":
    a = "greaat"
    b = "rgesat"
    print(scramble(a,b))