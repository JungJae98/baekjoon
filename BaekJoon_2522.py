star = int(input())

for i in range(1, star + 1):
    print(" " * (star - i) + '*' * i)
for i in range(1, star):
    print(" " * i + '*' * (star - i))