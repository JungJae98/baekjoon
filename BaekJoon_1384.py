group_num =0

while(True):
    n = int(input())
    if n == 0:
        break
    name = []
    group = []
    cnt = 0
    group_num += 1
    for i in range (n):
        ## 사람들의 이름과 badwording 사용여부 입력받음
        name = input().split()
        ## 입력받은 정보를 group에 저장함
        group.append(name)
    print("Group", group_num)
    for i in range(n):
        for j in range(1, n):
            if group[i][j] == "N":
                saybad = group[(n-j+i)%n][0]
                hearbad = group[i][0]
                print("{} was nasty about {}".format(saybad, hearbad))
                cnt +=1
    if cnt == 0:
        print("Nobody was nasty")
    print()
        