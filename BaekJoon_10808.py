S = input()
list = [0]*26

for i in  S:
    list[ord(i)-97]+=1
for i in list:
    print(i, end=" ")
    