from collections import deque

def bfs():

    # 인덱스: 자식노드, 인덱스의 값: 부모노드
    parents = [0] * (n+1)
    parents[1] = 1 # 방문처리 하려고 넣은 임의의 값

    # 루트부터 탐색
    q = deque([1])
    
    while q:
        node = q.popleft()

        for c in graph[node]:
            # 방문한 적 있다 == 부모 노드 있음
            if not parents[c]:
                parents[c] = node
                q.append(c) # c가 부모인 노드 탐색

    return parents


n = int(input())
graph = [[] for _ in range(n+1)]

for _ in range(n-1):
    s, e = map(int, input().split())
    graph[s].append(e)
    graph[e].append(s)

result = bfs()
print(*result[2:], sep="\n")