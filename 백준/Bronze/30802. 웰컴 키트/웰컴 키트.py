n = int(input()) # 참가자 수
t_arr = list(map(int, input().split()))
t, p = map(int, input().split())

t_result = 0
for i in t_arr:
    if i == 0:
        continue

    elif i <= t:
        t_result += 1
    
    else:
        t_result += (i // t)
        if i % t != 0:
            t_result += 1

print(t_result)
print(n//p, n%p)