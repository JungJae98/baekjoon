sum = 0;
hour = 0;
minute = 0;

a = int(input())
b = int(input())
c = int(input())
d = int(input())

sum = a+b+c+d

hour = sum // 60
minute = sum % 60

print(hour)
print(minute)