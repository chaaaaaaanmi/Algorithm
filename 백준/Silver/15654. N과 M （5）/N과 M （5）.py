def solve():

    if len(answer) == m:
        print(*answer)
        return
    
    for i in range(n):
        if not visited[i]:
            visited[i] = 1
            answer.append(arr[i])
            
            solve()

            answer.pop() # 복구
            visited[i] = 0


n, m = map(int, input().split())
arr = sorted(list(map(int, input().split())))

visited = [0] * n
answer = []
solve()