a, b = map(int,input().split())
kmin = a*1000/b

n = int(input())
for i in range(n):
    a, b = map(int,input().split())
    kmin = min(kmin, a*1000/b)
print(round(kmin, 2))