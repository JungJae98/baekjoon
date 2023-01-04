import sys
# N, m, M, T, R = map(int, input().split()) 밑 방법보다 시간복잡도가 안좋음
N, m, M, T, R = map(int, sys.stdin.readline().split())
#N = 운동시간
#m = 최소맥박, 초기맥박
#M = 최대맥박
#T = 증가맥박
#R = 감소맥박
now = m
time, Ex_time = 0, 0

while(Ex_time < N):
    if m+T > M:
        break
    if now+T <= M:
        now += T
        time += 1
        Ex_time += 1
    else:
        now = max(now-R, m)
        time += 1
    # elif now - R > m:
    #     now -= R
    #     time += 1
    # elif now - R < m:
    #     now = m
    #     time += 1
        
print(time if Ex_time == N else -1)
