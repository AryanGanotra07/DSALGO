a = [1,2,3,4,5,3,2,1]

x = 0
y = 0
xor = a[0]
for i in range(1, len(a)):
    xor^=a[i]
set_bit_no = xor & ~(xor-1)

for i in range(len(a)):
    if a[i] & set_bit_no:
        x = x^a[i]
    else:
        y = y^a[i]

print(x,y)