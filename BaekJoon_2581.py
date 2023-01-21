#자연수 M과 N이 주어질 때 M 이상 N이하의 자연수 중 소수인 것을 모두 골라 이들 소수의 합과 최솟값을 찾는 프로그램을 작성하시오
a = int(input())
b = int(input())
sosu = []


#소수를 찾는다 그럼 소수는 자기 자신과 1을 제외한 어떠한 수로 나누어도 나누어 떨어지지 않는 수를 뜻한다.
#그렇다면 자기 자신과 1을 제외한 수로 나누어도 나누어 떨어지지 않는 수를 찾으면 된다.
#따라서 i는 원하는 범위의 수를 나타낼 수 있다.
#그렇다면 어떻게 소수라는 것을 증명할 수 있을 것인가를 증명해보면 된다.
#따라서 그럼 소수를 증명하기 위한 자기 자신과 1을 제외한 수로 나누어 보면 된다.
for i in range(a, b+1):
    error = 0
    if i > 1:
       for k in range(2,i):
           if i % k == 0:
               error += 1
               break
       if error == 0:
           sosu.append(i)
if len(sosu) > 0:
    print(sum(sosu))
    print(min(sosu))
else:
    print(-1)