k, n = map(int, input().split())
lan = [int(input()) for _ in range(k)]


start = 1
end = max(lan)
answer = 0

while start <= end:
    
    mid = (start + end) // 2  # 자를 길이
    cnt = 0

    for l in lan:
        cnt += l // mid

    if cnt >= n:
        answer = mid
        start = mid + 1
    else:
        end = mid - 1

print(answer)