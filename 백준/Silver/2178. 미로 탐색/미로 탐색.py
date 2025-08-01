from collections import deque

n, m = map(int, input().split())
miro = [list(map(int, input().strip())) for _ in range(n)]

# 상 우 하 좌
dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]

def bfs(start_r, start_c):
    
    q = deque([(start_r, start_c)])
    visited[start_r][start_c] = 1
    count[start_r][start_c] = 1 # 시작 위치도 포함

    while q:

        r, c = q.popleft()

        if r == n-1 and c == m-1:
            break

        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]

            # 범위 체크
            if 0 <= nr < n and 0 <= nc < m:
                # 1인지 체크, 방문여부 체크
                if miro[nr][nc] and not visited[nr][nc]:
                    q.append((nr, nc))
                    visited[nr][nc] = 1
                    count[nr][nc] = count[r][c] + 1


visited = [list([0] * m) for _ in range(n)]
count = [list([0] * m) for _ in range(n)]

bfs(0, 0)
print(count[n-1][m-1])