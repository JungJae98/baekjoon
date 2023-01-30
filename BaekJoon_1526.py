n = int(input())

while True:
    a=0
    for i in str(n):
        if i != '4' and i != '7':
            a=1
            n -= 1
    if a != 1:
        print(n)
        break

