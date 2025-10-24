from collections import deque

n = int(input())
e = int(input())

def bfs():

    q = deque([1])
    visited[1] = 1

    while q:
        node = q.popleft()

        for next_node in network[node]:
            if not visited[next_node]:
                visited[next_node] = 1
                q.append(next_node)


network = [[] for _ in range(n+1)]
visited = [0] * (n+1)
visited[0] = 1

for _ in range(e):
    s, e = map(int, input().split())
    network[s].append(e)
    network[e].append(s)

bfs()
cnt = -2  # 0번, 1번 노드 제외
for i in visited:
    if i == 1:
        cnt += 1

print(cnt)