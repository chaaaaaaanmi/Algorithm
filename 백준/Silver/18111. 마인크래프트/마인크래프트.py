# n: 세로, m: 가로, b: 인벤토리 내 블록 개수
n, m, b = map(int, input().split())
MAP = [list(map(int, input().split())) for _ in range(n)]

time = 500 * 500 * 256 * 2
height = 0
min_h = min(map(min, MAP))
max_h = max(map(max, MAP))
for h in range(min_h, max_h+1):
    need = 0
    remove = 0

    for x in range(n):
        for y in range(m):
            if MAP[x][y] < h:
                need += h - MAP[x][y]
            elif MAP[x][y] > h:
                remove += MAP[x][y] - h

    # 인벤토리에 있는 블록보다 더 많은 블록이 필요하면 이 높이는 불가능
    if need - remove > b:
        continue

    current_time = (need * 1) + (remove * 2)
    if current_time <= time:
        time = current_time
        height = h


print(time, height, sep=" ")