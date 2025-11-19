from collections import deque

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

def bfs(start_r, start_c, visited):

    q = deque([(start_r, start_c)])
    visited[start_r][start_c] = 1

    while q:
        r, c = q.popleft()

        for d in range(4):
            nr = r + dr[d]
            nc = c + dc[d]

            # 범위 체크
            if 0 <= nr < n and 0 <= nc < m:
                # 인접한 곳에 배추가 있고, 방문한 적 없으면
                if bachoo[nr][nc] == 1 and not visited[nr][nc]:
                    q.append((nr, nc))
                    visited[nr][nc] = 1


t = int(input())
answer = []
for _ in range(t):
    # m: 가로, n: 세로, k: 배추 위치 개수
    m, n, k = map(int, input().split())

    bachoo = [[0] * m for _ in range(n)]
    visited = [[0] * m for _ in range(n)]

    # 배추 채우기
    for _ in range(k):
        x, y = map(int, input().split())
        # 0 <= x <= m-1, 0 <= y <= n-1
        bachoo[y][x] = 1

    cnt = 0 # 배추흰지렁이
    for r in range(n):
        for c in range(m):
            # 이미 계산한 것들 제외
            if bachoo[r][c] == 1 and not visited[r][c]:
                bfs(r, c, visited)
                cnt += 1

    answer.append(cnt)

print(*answer, sep="\n")