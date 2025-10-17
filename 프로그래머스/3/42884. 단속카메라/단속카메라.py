# routes => [진입, 진출]
def solution(routes):
    answer = 0
    
    # 진출 시점 기준으로 정렬
    routes.sort(key=lambda x:x[1])
    camera = -30001
    
    for r in routes:
        # 카메라가 진입 시점보다 전에 있다 => 안찍혔다
        if camera < r[0]:
            answer += 1 # 카메라 추가
            # 카메라
            camera = r[1] # 카메라 위치를 진출 시점으로 변경
    
    return answer