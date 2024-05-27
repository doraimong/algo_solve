'''
dfs
'''
def solution(n, computers):
    answer = 0
    visit = [0 for _ in range(n)]
    
    def dfs (i):
        for idx, c in enumerate(computers[i]):
            if c == 0 or visit[idx] == 1: continue # 연결 no
            visit[idx] = 1
            dfs(idx)
        
    for i in range(n):
        if visit[i] == 1: continue
        visit[i] = 1
        dfs(i)
        answer += 1
    
    return answer