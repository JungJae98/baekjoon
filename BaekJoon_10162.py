time = int(input())

if time % 10 != 0:
    print(-1)
else:
    time5m = time1m = time10s = 0
    time5m = time // 300
    time = time % 300
    time1m =  time // 60
    time = time % 60
    time10s = time // 10
    print(time5m, time1m, time10s)

