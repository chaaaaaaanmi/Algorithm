def solution(s):
    
    if len(s) == 1:
        return 1
           
    answer = len(s) # 압축이 안 되는 경우
    
    # cut 단위로 자르기
    for cut in range(1, len(s)//2+1):
        
        prev = s[:cut]
        count = 1
        result = ""
        
        # cut 단위로 반복
        for i in range(cut, len(s), cut):
            current = s[i:i+cut]
            
            # 중복이면 count + 1
            if current == prev:
                count += 1
                
            # 그게 아니면 result에 붙이기
            else:
                if count > 1:
                    result += str(count) + prev
                else:
                    result += prev
                    
                # 다음 비교할 문자열로 갱신
                prev = current
                count = 1
        
        # 마지막 덩어리 처리
        if count > 1:
            result += str(count) + prev
        else:
            result += prev
            
        # 가장 짧은 길이 갱신
        answer = min(answer, len(result))
        
    return answer