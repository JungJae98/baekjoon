hour, minute = map(int, input().split())
addTime = int(input())

if (minute+addTime >= 60):
    hour += (minute + addTime) // 60
    minute = minute + addTime
else:
    hour += (minute + addTime) // 60
    minute = minute + addTime
hour = hour % 24
minute = minute % 60

print(hour,minute)
