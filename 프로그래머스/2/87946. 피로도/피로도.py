'''
순열
'''
def solution(k, dungeons):
    answer = -1
    visit, pick = [False for _ in range(len(dungeons))], [0 for _ in range(len(dungeons))] # 순열을 위한 리스트
    maxGameCnt = 0
    
    def perm(cnt) : #게임의 순서를 정함
        nonlocal maxGameCnt
        if cnt == len(dungeons): 
            tempGameCnt = play()
            maxGameCnt = max(maxGameCnt, tempGameCnt)
            return
            
        for i in range(len(dungeons)):
            if visit[i] : continue 
            pick[cnt] = i
            visit[i] = True
            perm(cnt+1)
            visit[i] = False
    
    def play(): #순서가 정해진 게임을 수행 -> 플레이 가능한 게임 개수 계산
        tempK, gameCnt = k, 0
        for i in pick:
            underHealth, minusHealth = dungeons[i]
            if tempK < underHealth: return gameCnt # '최소 필요 피로도'보다 남은 피로도가 적을 때 
            tempK -= minusHealth
            gameCnt += 1
        
        return gameCnt
        
        
    perm(0)
    
    return maxGameCnt