'''
bfs돌리는데 시작->레버, 레버->출구
visit 숫자로 구성
'''
from collections import deque

def solution(maps):
    answer = 0
    dr, dc = [0, 0, -1, 1], [-1, 1, 0, 0]
    sizeR, sizeC = len(maps), len(maps[0])
    visit = [list(int(1e9) for _ in range(sizeC)) for _ in range(sizeR)]
    start, leber, end = [],[],[]
    
    for i in range(sizeR):
        for j in range(sizeC):
            if maps[i][j] == 'S':
                start = [i,j]
            elif maps[i][j] == 'L':
                leber = [i,j]
    
    def bfs(pos, target):
        dq = deque()
        dq.appendleft(pos + [0])
        while dq:
            r,c, dis = dq.pop()
            for i in range(4):
                nr, nc = r+dr[i], c+dc[i]
                if -1<nr<sizeR and -1<nc<sizeC and maps[nr][nc] != 'X' and dis+1 < visit[nr][nc] :
                    if maps[nr][nc] == target:
                        return dis+1
                    else:
                        visit[nr][nc] = dis+1
                        dq.appendleft([nr, nc, dis+1])
        return -1
    
    #시작점에서 레버로 가는 시간
    answerTemp = bfs(start, 'L')
    if answerTemp == -1 :
        return -1
    else:
        answer += answerTemp
    
    #레버에서 출구로 가는 시간
    visit = [list(int(1e9) for _ in range(sizeC)) for _ in range(sizeR)]
    answerTemp = bfs(leber, 'E')
    if answerTemp == -1 :
        return -1
    else:
        answer += answerTemp
    
    return answer
