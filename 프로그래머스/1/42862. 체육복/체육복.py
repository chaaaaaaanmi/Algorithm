def solution(n, lost, reserve):
    
    lost.sort()
    reserve.sort()
    
    # 여벌 체육복이 있지만 도난당한 학생은 빌려줄 수 없다
    for student in lost[:]:
        if student in reserve:
            reserve.remove(student)
            lost.remove(student) # 어쨋든 수업은 들을 수 있음
            
    # 빌려줄 수 있는 학생 기준으로 앞, 뒤 살펴보기
    for can in reserve:
        if can-1 in lost:
            lost.remove(can-1)
        elif can+1 in lost:
            lost.remove(can+1)
    
    return n - len(lost)