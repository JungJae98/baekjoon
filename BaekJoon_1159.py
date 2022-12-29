lastName = []
counter = {}
flag = 0

for i in range(int(input())):
    result = input()
    result = result[:1]
    lastName.append(result)

for value in lastName:
    if value in counter:
        counter[value] += 1
    else:
        counter[value] = 1

for key, value in sorted(counter.items()):
    if value >= 5:
        print(key, end="") 
        flag = 1

if flag == 0:
    print("PREDAJA")
    