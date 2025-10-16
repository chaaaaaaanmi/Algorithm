max_cnt = 0

# k: 현재 피로도
# dungeons: [최소 필요 피로도, 소모 피로도]
# 던전 개수: 1 ~ 8
def solution(k, dungeons):

    visited = [0] * len(dungeons)
    bfs(k, 0, dungeons, visited)
    return max_cnt


def bfs(k, cnt, dungeons, visited):
    global max_cnt
    
    
    # 한 노드에서 탐험 끝나면 최대 횟수 갱신
    if cnt > max_cnt:
        max_cnt = cnt
        
    for i in range(len(dungeons)):
        # 방문한 적 없고, 탐험 가능한 경우
        if not visited[i] and k >= dungeons[i][0]:
            visited[i] = 1
            # 다음 탐험
            bfs(k-dungeons[i][1], cnt+1, dungeons, visited)
            # 복구
            visited[i] = 0