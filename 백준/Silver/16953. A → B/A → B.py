def solve(num, cnt):
    global min_cnt

    # 가지치기
    if num > b:
        return
    
    if num == b:
        min_cnt = min(min_cnt, cnt)
        return

    # 2 곱하기
    solve(num*2, cnt+1)
    
    # 오른쪽에 1 추가하기
    solve((num*10)+1, cnt+1)



a, b = map(int, input().split())
min_cnt = 1e9
solve(a, 0)

if min_cnt >= 1e9:
    print(-1)
else:
    print(min_cnt+1)