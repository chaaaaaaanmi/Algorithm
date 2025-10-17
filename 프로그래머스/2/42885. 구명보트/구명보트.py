from collections import deque

def solution(people, limit):
    
    # 무거운 순서로 정렬
    q = deque(sorted(people, reverse=True))
    print(q)

    boat = 0
    while q:
        
        # 무거운 사람부터 빼내기
        w = q.popleft()
        
        # 아직 사람이 남아 있고, limit 남으면 가벼운 사람 같이 빼내기
        if len(q) > 0 and q[-1] <= (limit - w):
            q.pop()
        
        boat += 1
    
    return boat