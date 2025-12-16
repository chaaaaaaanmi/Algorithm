def solve(start):

    if len(answer) == m:
        print(*answer)
        return
    
    prev = -1
    for i in range(start, n):
        if arr[i] == prev:
            continue
        
        prev = arr[i]

        answer.append(arr[i])
        solve(i)
        answer.pop()


n, m = map(int, input().split())
arr = sorted(list(map(int, input().split())))

answer = []
solve(0)