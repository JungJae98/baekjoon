star = int(input())

for i in range (star+1, 1, -1):
    print(" "*(star-i+1) + "*"*(i-1))