for i in range(int(input())):
    n = int(input())
    T = 0
    sum = 0
    for k in range(1,n+1):
        for j in range(1,k+2):
            T+=j
        sum += k*T
        T = 0
    print(sum)