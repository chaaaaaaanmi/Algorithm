def solution(s):
    
    if len(s) == 1:
        return 1
    
    min_answer = len(s)
    
    # 자르는 단위는 1 ~ len(s)//2
    for i in range(1, len(s)//2+1):
        
        answer = 0
        cnt = 1 # 문자열 반복 횟수 (일단 하나는 존재하는거니까 1)
        string = s[:i] # 비교할 문자열
        
        # i 단위로 자르면서 비교해보기
        for j in range(i, len(s), i):
            # 현재 문자열
            current = s[j:j+i]
        
            # 비교할 문자열과 현재 문자열이 같다
            if string == current:
                cnt += 1
                continue

            # 비교할 문자열과 현재 문자열이 다르다
            else:
                answer += len(string)
                # cnt가 1이면 생략
                if cnt > 1:
                    answer += len(str(cnt))
                
                string = current # 비교할 문자열 갱신
                cnt = 1 # cnt 초기화
                
        # 마지막 그룹까지 계산
        answer += len(string)
        if cnt > 1:
            answer += len(str(cnt))
                
        # min 갱신
        min_answer = min(answer, min_answer)
    
    return min_answer