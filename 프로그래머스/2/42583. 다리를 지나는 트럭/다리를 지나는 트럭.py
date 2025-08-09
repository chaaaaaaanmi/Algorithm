from collections import deque

def solution(bridge_length, weight, truck_weights):
    
    trucks = deque(truck_weights)
    bridge = deque([0]*bridge_length)
    w = 0  # 다리 위 무게 합
    time = 0
    
    while trucks or w > 0:
        time += 1
        
        # 1초 증가 -> 다리에서 하나 빼기 (다리에 현재 한 자리 빈 상태)
        left = bridge.popleft()
        w -= left
        
        # 다음 트럭이 있고, 무게 견딜 수 있는지 체크
        if trucks and w + trucks[0] <= weight:
            truck = trucks.popleft()
            bridge.append(truck)
            w += truck
        # 다음 트럭 못 건너는거면 0 채우기
        else:
            bridge.append(0)
            
    return time