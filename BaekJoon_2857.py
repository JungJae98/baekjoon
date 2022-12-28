a = []
flag = 0
for i in range(5):
    a.append(input())
    
for i in range(len(a)):
    if ('FBI' in a[i]):
        print(i+1, end=' ')
        flag = 1
        
if (flag == 0):
    print("HE GOT AWAY!")

  