import sys
from collections import deque
input = sys.stdin.readline

# 상 하 좌 우
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]


def bfs():

    sg_q = deque([])
    fire_q = deque([])

    # 불, 상근이 위치 찾기
    for x in range(h):
        for y in range(w):
            if building[x][y] == "*":
                fire_q.append((x, y))
            if building[x][y] == "@":
                sg_q.append((x, y))
                visited[x][y] = 1

    time = 1
    while sg_q:

        # 매초마다 불이 퍼진다.
        for _ in range(len(fire_q)):
            r, c = fire_q.popleft()

            for d in range(4):
                nr = r + dr[d]
                nc = c + dc[d]

                # 범위 체크, 빈 공간인지 체크
                if 0 <= nr < h and 0 <= nc < w and building[nr][nc] == ".":
                    building[nr][nc] = "*"
                    fire_q.append((nr, nc))

        # 상근이 이동
        # 인접 좌표 탐색이 끝이 나야 시간이 증가한다.
        for _ in range(len(sg_q)):
            r, c = sg_q.popleft()

            for d in range(4):
                nr = r + dr[d]
                nc = c + dc[d]

                # 범위 체크
                if 0 <= nr < h and 0 <= nc < w:
                    # 빈 공간이고, 방문한 적 없으면 갈 수 있다.
                    if building[nr][nc] == "." and not visited[nr][nc]:
                        sg_q.append((nr, nc))
                        visited[nr][nc] = 1

                # 범위 벗어나면 탈출
                else:
                    return time
                
        # 인접 좌표 탐색이 끝났다면 1초 증가
        time += 1

    return "IMPOSSIBLE"


t = int(input())
result_list = []
for _ in range(t):

    w, h = map(int, input().split(" "))
    building = [list(input().strip()) for _ in range(h)]
    visited = [[0] * w for _ in range(h)]

    result = bfs()
    result_list.append(result)

print(*result_list, sep="\n")