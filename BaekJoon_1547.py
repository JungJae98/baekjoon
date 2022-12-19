n = int(input())
result = 1

for i in range (0, n):
    a, b = map(int, input().split())
    if (a==result):
        result = b
    elif(b==result):
        result = a
        
print(result)