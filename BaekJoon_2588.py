a = int(input())
b = int(input())
result = a*b

b = list(map(int,str(b)))

for i in range (2, -1, -1):
    c = a*b[i]
    print (c)

print(result)
