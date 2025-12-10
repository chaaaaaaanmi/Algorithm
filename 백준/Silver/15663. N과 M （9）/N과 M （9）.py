def solve():

    if len(answer) == m:
        s.add(tuple(answer))
        return

    for i in range(n):
        if not visited[i]:
            answer.append(arr[i])
            visited[i] = 1

            # 재귀
            solve()

            # 복구
            answer.pop()
            visited[i] = 0


n, m = map(int, input().split())
arr = list(map(int, input().split()))

visited = [0] * n
answer = []
s = set()
solve()
s = sorted(list(s))

for i in range(len(s)):
    print(*list(s[i]))