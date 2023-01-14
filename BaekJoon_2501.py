answer = []
p, q = map(int,input().split())

for i in range(1,p+1):
    if p % i == 0:
        answer.append(i)

answer.sort() 

if len(answer) < q: 
    result = 0
else:
    result = answer[q-1]

print(result)