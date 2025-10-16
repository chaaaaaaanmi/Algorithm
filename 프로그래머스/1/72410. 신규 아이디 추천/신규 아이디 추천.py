def solution(new_id):
    
    alpha = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
    nums = [str(i) for i in range(0, 10)]
    
    # 1단계: 대문자 -> 소문자
    current_id = new_id.lower()

    # 2단계
    temp = []
    for c in current_id:
        if c in alpha or c in nums or c in "-_.":
            temp.append(c)
    
    # 3단계
    idx = 0
    while idx < len(temp)-1:
        
        if temp[idx] == "." and temp[idx+1] == ".":
            temp.pop(idx)
            continue
            
        idx += 1
    
    # 리스트 -> 문자열
    # 4단계: 양 옆 . 날리기
    current_id = "".join(temp).strip(".")
        
    # 5단계
    if len(current_id) == 0:
        current_id = "a"
        
    # 문자열 -> 리스트
    temp = [c for c in current_id]
    # 6단계
    if len(temp) >= 16:
        temp = temp[:15]
        while temp[-1] == ".":
            temp.pop()
    
    # 7단계
    if len(temp) <= 2:
        while len(temp) < 3:
            temp.append(temp[-1])


    return "".join(temp)