def solve(start):

    if len(answer) == m:
        print(*answer)
        return
    
    for i in range(start, n+1):
        answer.append(i)
        solve(i+1)
        answer.pop() # 복구


n, m = map(int, input().split())
answer = []
solve(1)