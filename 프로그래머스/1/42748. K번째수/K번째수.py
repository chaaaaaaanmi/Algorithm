def solution(array, commands):
    
    answer = []
    
    for c in range(len(commands)):
        i = commands[c][0]
        j = commands[c][1]
        k = commands[c][2]
        
        arr = array[i-1:j]
        arr.sort()
        answer.append(arr[k-1])
    
    return answer