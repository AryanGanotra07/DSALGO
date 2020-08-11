x = 15
y = 32

while(y!=0):
    carry = x&y
    x = x^y
    y = carry << 1
print(x)