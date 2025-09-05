a, b, v = map(int, input().split())

if v <= a:
    print(1)
    
else:
    day = (v-a) // (a-b)
    day += 1

    if v - ((a-b) * (day-1)) > a:
        day += 1
    
    print(day)