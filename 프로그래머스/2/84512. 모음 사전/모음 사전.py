answer = 0
alpha = ["A", "E", "I", "O", "U"]

def dfs(current, word):
    global answer, alpha
    
    answer += 1
    
    # 단어 찾음 - True
    if current == word:
        return True
    
    # 최대 길이 5 - 탐색 계속
    if len(current) == 5:
        return False
    
    # 알파벳 하나씩 꺼내서 붙여보기
    for a in alpha:
        if dfs(current+a, word):
            return True
    

def solution(word):
    global answer, alpha

    for a in alpha:
        if dfs(a, word):
            return answer
