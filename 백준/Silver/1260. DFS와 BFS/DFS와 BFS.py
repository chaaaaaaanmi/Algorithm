from collections import deque

def dfs(v, visited):

    s = [v]
    path = []

    while s:
        node = s.pop()
        if not visited[node]:
            visited[node] = 1
            path.append(node)

            # 역순이어야 작은 번호부터 방문
            for next_node in reversed(graph[node]):
                if not visited[next_node]:
                    s.append(next_node)

    return path


def bfs(v, visited):
    
    q = deque([v])
    visited[v] = 1
    path = []

    while q:
        node = q.popleft()
        path.append(node)

        for next_node in graph[node]:
            if not visited[next_node]:
                visited[next_node] = 1
                q.append(next_node)

    return path


# n: 정점 개수, m: 간선 개수, v: 탐색 시작 정점 번호
n, m, v = map(int, input().split())
graph = [[] for _ in range(n+1)] # 1부터 시작

# 그래프 채우기
for _ in range(m):
    s, e = map(int, input().split())
    graph[s].append(e)
    graph[e].append(s)

for g in graph:
    g.sort()

visited = [0] * (n+1)
result_dfs = dfs(v, visited)
print(*result_dfs)

visited = [0] * (n+1)
result_bfs = bfs(v, visited)
print(*result_bfs)