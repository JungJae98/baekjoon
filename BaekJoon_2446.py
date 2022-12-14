star = int(input())

for i in range(0, star):
    print(" "*i + "*"*(2*(star-i)-1))
for i in range(0, star-1):
    print(" "*(star-i-2)+"*"*(2*i+3))