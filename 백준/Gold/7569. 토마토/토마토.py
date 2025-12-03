from collections import deque

# m: 가로, n: 세로, h: 상자 수
m, n, h = map(int, input().split())
tomato = [[list(map(int, input().split())) for _ in range(n)] for _ in range(h)]

# 위 아래 왼 오 앞 뒤
dy = [0, 0, 0, 0, -1, 1]
dx = [0, 0, -1, 1, 0, 0]
dz = [1, -1, 0, 0, 0, 0]

def bfs(q, tomato):

    while q:
        length = len(q)

        for _ in range(length):
            z, y, x = q.popleft()

            for d in range(6):
                nz = z + dz[d]
                ny = y + dy[d]
                nx = x + dx[d]

                # 범위 체크
                if 0 <= ny < n and 0 <= nx < m and 0 <= nz < h:
                    # 안 익은 토마토인지 확인
                    if tomato[nz][ny][nx] == 0:
                        q.append((nz, ny, nx))
                        tomato[nz][ny][nx] = tomato[z][y][x] + 1


q = deque([])

# 1: 익은 토마토, 0: 안 익은 토마토, -1: 토마토 없음
for z in range(h):
    for y in range(n):
        for x in range(m):
            # q에 익은 토마토 전부 넣기
            if tomato[z][y][x] == 1:
                q.append((z, y, x))

bfs(q, tomato)
day = 0
all = True
for z in range(h):
    for y in range(n):
        for x in range(m):
            # 하나라도 안 익었으면 -1
            if tomato[z][y][x] == 0:
                all = False
            else:
                day = max(day, tomato[z][y][x])

if all:
    # 익은 토마토 1부터 더하기 시작했으니까
    print(day - 1)
else:
    print(-1)