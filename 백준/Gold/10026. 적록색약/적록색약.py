from collections import deque

n = int(input())
painting = [list(input()) for _ in range(n)]


dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

def bfs(start_r, start_c, color, rg, visited):

    q = deque([(start_r, start_c)])
    visited[start_r][start_c] = 1

    while q:
        r, c = q.popleft()

        for d in range(4):
            nr = r + dr[d]
            nc = c + dc[d]

            if 0 <= nr < n and 0 <= nc < n and not visited[nr][nc]:
                # 적록색약 O
                if rg and color in ["R", "G"]:
                    if painting[nr][nc] in ["R", "G"]:
                        visited[nr][nc] = 1
                        q.append((nr, nc))
                # 적록색약 X
                else:
                    if painting[nr][nc] == color:
                        visited[nr][nc] = 1
                        q.append((nr, nc))


visited = [[0] * n for _ in range(n)]
rg = False
zone = 0
for i in range(n):
    for j in range(n):
        if not visited[i][j]:
            color = painting[i][j]
            bfs(i, j, color, rg, visited)
            zone += 1

visited = [[0] * n for _ in range(n)]
rg = True
rg_zone = 0
for i in range(n):
    for j in range(n):
        if not visited[i][j]:
            color = painting[i][j]
            bfs(i, j, color, rg, visited)
            rg_zone += 1

print(zone, rg_zone)