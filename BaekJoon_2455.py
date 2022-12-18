d = []
c = 0

for i in range(0,4):
    a, b = map(int, input().split())
    c += b
    c -= a 
    d.append(c)
    
print(max(d))