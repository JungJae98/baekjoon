n = int(input())
sum = 0
result = 0
A = list(map(int, input().split()))

for i in range (0,n):
    if (A[i] == 1):
        sum += 1
        result += sum
    else:
        sum = 0

print(result)
