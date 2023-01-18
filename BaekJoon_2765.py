i = 1

while(True):
    inch, cycle, time = map(float,input().split())    
    
    distance = 3.1415927 * inch * cycle / 63360
    MPH = (distance / time) * 3600
    
    if cycle != 0:       
        print('Trip #{}: {:.2f} {:.2f}' .format(i, distance, MPH))
        i += 1
    elif cycle == 0:
        break