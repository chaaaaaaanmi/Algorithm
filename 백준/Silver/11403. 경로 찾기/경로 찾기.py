from collections import deque

def bfs(start, end):

    q = deque([start])
    visited = [0] * n
    visited[start] = 1

    while q:
        node = q.popleft()

        for next_node in graph[node]:
            if next_node == end:
                return True
            if not visited[next_node]:
                visited[next_node] = 1
                q.append(next_node)

    return False


n = int(input())
graph = [[] for _ in range(n)]

# 그래프 채우기
for i in range(n):
    row = list(map(int, input().split()))
    for j in range(n):
        if row[j]:
            graph[i].append(j)

result = [[0] * n for _ in range(n)]
for i in range(n):
    for j in range(n):
        can = bfs(i, j)
        if can:
            result[i][j] = 1

for row in result:
    print(*row)