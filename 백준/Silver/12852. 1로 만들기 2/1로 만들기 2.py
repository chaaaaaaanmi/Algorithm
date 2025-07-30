from collections import deque

def bfs(start):
    q = deque([start])
    
    visited[start] = 1

    while q:
        n = q.popleft()

        # 1이 되면 종료
        if n == 1:
            break

        for next in [n-1,
                     n//3 if n % 3 == 0 else -1,
                     n//2 if n % 2 == 0 else -1]:
            # 방문한적 없다면 q에 추가하고 방문체크
            if next >= 1 and next <= start and not visited[next]:
                visited[next] = 1
                dist[next] = dist[n] + 1
                path[next] = n
                q.append(next)

x = int(input())
visited = [0] * (x+1)
dist = [0] * (x+1) # 최소 연산 횟수
path = [0] * (x+1) # 경로 저장
bfs(x)

print(dist[1])

# 경로 역추적
current = 1
result_path = []
while current != 0:
    result_path.append(current)
    current = path[current]

print(*result_path[::-1])