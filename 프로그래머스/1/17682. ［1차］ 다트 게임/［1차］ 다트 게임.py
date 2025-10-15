# 입력값 나누기
def ex(s):
    i = 0 # index
    arr = []
    
    while i < len(s):
        
        # 숫자
        # 10일 경우
        if s[i] == "1" and i+1 < len(s) and s[i+1] == "0":
            num = 10
            i += 2 
        else:
            num = int(s[i])
            i += 1
            
        # 보너스
        bonus = s[i]
        i += 1
        
        # 옵션 (있을 수도, 없을 수도)
        opt = ""
        if i < len(s) and s[i] in ("*", "#"):
            opt = s[i]
            i += 1

        # 점수, 보너스, 옵션
        arr.append((num, bonus, opt))

    return arr

# 보너스 계산
def solve_bonus(score, bonus):
    
    if bonus == "S":
        return score
    
    if bonus == "D":
        return score ** 2
    
    if bonus == "T":
        return score ** 3
        
        
# 옵션 계산
def solve_option(score, option):
    
    if option == "*":
        return score * 2
    
    if option == "#":
        return -score
    
    # 옵션은 없을수도
    return score

    
def solution(dartResult):

    scores = []    
    # 입력값 처리
    result = ex(dartResult)
    
    
    # 점수 계산
    for num, bonus, option in result:

        # 보너스 계산
        current = solve_bonus(num, bonus)

        # 옵션 계산
        current = solve_option(current, option)
        
        # *은 직전 점수도 2배
        if option == "*" and scores:
            scores[-1] *= 2
    
        scores.append(current)
    
    return sum(scores)
        