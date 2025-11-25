from collections import deque
import sys
input = sys.stdin.readline

def bfs(v):
    global connect

    q = deque([v])
    visited[v] = 1

    while q:
        node = q.popleft()

        for next_node in graph[node]:
            if not visited[next_node]:
                visited[next_node] = 1
                q.append(next_node)

    connect += 1


n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]

for _ in range(m):
    s, e = map(int, input().split())
    graph[s].append(e)
    graph[e].append(s)

visited = [0] * (n+1)
connect = 0
for i in range(1, n+1):
    if not visited[i]:
        bfs(i)

print(connect)