from collections import deque

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

def bfs(start_r, start_c, n, visited):

    q = deque([(start_r, start_c)])
    visited[start_r][start_c] = 1
    cnt = 1

    while q:
        r, c = q.popleft()

        for d in range(4):
            nr = r + dr[d]
            nc = c + dc[d]

            if 0 <= nr < n and 0 <= nc < n and MAP[nr][nc] and not visited[nr][nc]:
                visited[nr][nc] = 1
                q.append((nr, nc))
                cnt += 1

    return cnt


n = int(input())
MAP = [list(map(int, input())) for _ in range(n)]
visited = [[0] * n for _ in range(n)]

result = []
for i in range(n):
    for j in range(n):
        if MAP[i][j] == 1 and not visited[i][j]:
            cnt = bfs(i, j, n, visited)
            result.append(cnt)

result.sort()
print(len(result))
print(*result, sep="\n")