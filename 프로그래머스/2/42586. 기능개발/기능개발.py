from collections import deque

def solution(progresses, speeds):
    answer = []
    
    q = deque(progresses)
    s = deque(speeds)
    
    while q:
        
        # 하루 작업 진도 빼기
        for i in range(len(q)):
            q[i] += s[i]
            
        count = 0
        while q and q[0] >= 100:
            q.popleft()
            s.popleft()
            count += 1

        if count > 0:
            answer.append(count)
        
    return answer