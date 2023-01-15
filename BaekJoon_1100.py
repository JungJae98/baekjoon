a =[]
for i in range(8):
    a.append(list(map(str, list(input()))))

F = 0
for i in range(8):
    for k in range(8):
        if(i+k) % 2 == 0:
            if(a[i][k] == 'F'):
                F += 1
print(F)