def solve(num, cnt):
    global min_cnt

    # 가지치기
    if num > b:
        return
    
    if num == b:
        min_cnt = min(min_cnt, cnt)
        return

    # 2 곱하기
    next = num * 2
    solve(next, cnt+1)
    # 복구
    next = num // 2
    
    # 오른쪽에 1 추가하기
    next = (num * 10) + 1
    solve(next, cnt+1)
    # 복구
    next = (num - 1) // 10



a, b = map(int, input().split())
min_cnt = 1e9
solve(a, 0)

if min_cnt >= 1e9:
    print(-1)
else:
    print(min_cnt+1)