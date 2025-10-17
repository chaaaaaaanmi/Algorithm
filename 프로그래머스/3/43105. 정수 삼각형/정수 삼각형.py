def solution(triangle):
    
    for depth in range(1, len(triangle)):
        # depth 층의 각 값 순회
        for i in range(len(triangle[depth])):
            
            # 제일 왼쪽이면, 이전 depth의 제일 왼쪽 값밖에 더할게 없음
            if i == 0:
                triangle[depth][i] += triangle[depth-1][0]
            
            # 오른쪽 끝이면, 이전 depth의 제일 오른쪽 값밖에 더할게 없음
            elif i == (len(triangle[depth])-1):
                triangle[depth][i] += triangle[depth-1][-1]
                
            # 이전 depth의 좌우 칸 중에 더 큰 값을 더하기
            else:
                triangle[depth][i] += max(triangle[depth-1][i-1], triangle[depth-1][i])
    
    # 제일 마지막 depth에서 최댓값
    return max(triangle[-1])