star = int(input())

for i in range (0, star):
    print(" "*(star-i-1) + "*" + "*"*2*i)
for i in range (star-1, 0, -1):
    print(" "*(star-i) + "*"*(2*i-1))