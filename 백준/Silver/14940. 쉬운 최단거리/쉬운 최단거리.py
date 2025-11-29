from collections import deque

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

def bfs(start_r, start_c):

    q = deque([(start_r, start_c)])
    visited = [[0] * m for _ in range(n)]
    visited[start_r][start_c] = 1

    while q:
        r, c = q.popleft()

        for d in range(4):
            nr = r + dr[d]
            nc = c + dc[d]

            if 0 <= nr < n and 0 <= nc < m and MAP[nr][nc] and not visited[nr][nc]:
                if r == start_r and c == start_c:
                    visited[nr][nc] = 1
                else:
                    visited[nr][nc] = visited[r][c] + 1

                q.append((nr, nc))

    return visited


n, m = map(int, input().split())
MAP = [list(map(int, input().split())) for _ in range(n)]

for i in range(n):
    for j in range(m):
        if MAP[i][j] == 2:
            result = bfs(i, j)

for i in range(n):
    answer = []

    for j in range(m):
        if MAP[i][j] == 2:
            answer.append(0)

        elif MAP[i][j] == 0 and result[i][j] == 0:
            answer.append(0)

        elif MAP[i][j] != 0 and result[i][j] == 0:
            answer.append(-1)

        else:
            answer.append(result[i][j])

    print(*answer)