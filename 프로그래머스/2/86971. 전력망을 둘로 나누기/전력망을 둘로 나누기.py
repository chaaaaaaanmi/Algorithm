from collections import deque

def bfs(v, graph, visited):
    
    q = deque([v]) # 탐색 시작 노드 미리 넣어두기
    visited[v] = 1 # v 방문처리
    cnt = 1 # v 포함
    
    while q:
        
        node = q.popleft()
    
        for next_node in graph[node]:
            if not visited[next_node]:
                visited[next_node] = 1
                cnt += 1
                q.append(next_node)
    
    return cnt


def solution(n, wires):
    
    answer = n
    
    # 그래프 채우기
    graph = [[] for _ in range(n+1)] # 1번 노드부터 쓸라고
    for s, e in wires:
        graph[s].append(e)
        graph[e].append(s)
        
    # 전선 하나씩 끊어보기
    for i in range(len(wires)):
        
        visited = [0] * (n+1)
        visited[0] = 1 # 0번 노드는 없음(방문처리)
        
        # 끊을 전선 정보
        a, b = wires[i]
        
        # 전선 끊기
        graph[a].remove(b)
        graph[b].remove(a)
        
        # 끊은 지점을 기준으로 탐색
        temp_a = bfs(a, graph, visited)
        temp_b = bfs(b, graph, visited)
        
        # 최솟값 갱신
        answer = min(answer, abs(temp_a - temp_b))
        
        # 전선 연결 복구
        graph[a].append(b)
        graph[b].append(a)
    
    return answer