'''
선공이 규칙에 맞춰 이겼는데도 후공이 진행되면 안된다.(선공이 규칙 완료 -> 후공은 선공 -1 개여야함) 
-> 반대인 경우도 안된다.(후공이 규칙 완료 -> 선공은 후공==선공 개수 여야함) 
최초 공격을 선공이 아닌 후공이 한 경우
위 경우 1 
구현
'''
def solution(board):
    answer = -1
    oCnt,xCnt = sum(r.count('O') for r in board), sum(r.count('X') for r in board)
    oOk, xOk = False, False 
    
    def regulationOk() : 
        def check(get):
            nonlocal oOk, xOk
            if get == 'O':
                oOk = True
                print(f'oOk : {oOk}')
            elif get == 'X':
                xOk = True
                print(f'xOk : {xOk}')
            
        # 대각선
        if board[0][0] == board[1][1] == board [2][2]:
            check(board[0][0])
        elif board[0][2] == board[1][1] == board [2][0]:
            check(board[0][2])
            
        # 가로 세로
        for i in range(3):
            if board[i][0] == board[i][1] == board[i][2]:
                check(board[i][0])
            if board[0][i] == board[1][i] == board[2][i]:
                check(board[0][i])
                
    regulationOk()
    
    # 공 개수
    if oCnt == xCnt or oCnt - 1 == xCnt:
        # 1. 둘다 조건을 맞췃다면
        if oOk and xOk: 
            return 0
        # 2. 하나만 조건을 맞췃다면
        # 2-1. 개수 문제 없는지 
        if oOk:
            if oCnt -1 == xCnt: 
                return 1
            else :
                return 0
        elif xOk:
            if xCnt == oCnt:
                return 1
            else:
                return 0
        
    else : 
        return 0
    
    return 1