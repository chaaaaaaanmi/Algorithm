from collections import deque

n, k = map(int, input().split())
visited = [0] * 100001 # 0 <= n,k <= 100000

def bfs(n):

    q = deque([n])
    visited[n] = 1

    while q:
        current = q.popleft()

        # 동생 만남
        if current == k:
            # 시작 위치부터 1초로 시작했으니까 -1
            return visited[current] - 1
        
        # 선택지 => 뒤로 한 칸, 앞으로 한 칸, 순간이동
        for next in (current-1, current+1, current*2):
            # 범위 체크, 방문 체크
            if 0 <= next <= 100000 and not visited[next]:
                visited[next] = visited[current] + 1
                q.append(next)

answer = bfs(n)
print(answer)