def solution(numbers):
    
    # 문자열로 변경
    numbers = [str(num) for num in numbers]
    # 내림차순 정렬
    numbers.sort(key=lambda x : x*4, reverse=True)
    
    if numbers[0] == "0":
        return "0"
    else:
        return "".join(numbers)