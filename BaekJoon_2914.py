a, b = map(int, input().split())

if a == 1:
    print(a*b)
elif a != 1:
    print(a*(b-1)+1)
    