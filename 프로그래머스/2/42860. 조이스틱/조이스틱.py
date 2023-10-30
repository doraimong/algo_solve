'''
보류 -> 극악의 난이도
'''

def solution(name):
    res = 0
    min_move = len(name) -1
    
    for i, c in enumerate(name):
        # 위아래키 조작
        res += min(ord(c) - ord('A'), ord('Z') - ord(c) + 1)
        
        # 해당 알파벳 다음부터 연속된 A의 문자열 찾기
        next = i + 1
        while next < len(name) and name[next] == 'A':
            next += 1
        
        # 좌우키 조작 최소값 계산(CCACCAA면 1인덱스에서 )
        min_move = min([min_move, 2*i + len(name)-next, i+2*(len(name)-next)])
    
    res += min_move
    
    return res


'''
풀기 전 생각
1. 순열 + 가지치기?
2. 뭔가 그리디는 다 보는 완탐과는 다르게 드릴로 뚫어버리는 맛이 있어야하는데 1번은 없는 듯 함
3. 풀이법
    1. 위 아래 키를 몇번 누르는지 구하기(AAA 문자열 - 정답 문자열 해서)
    2. 좌우 키를 몇번 누르는지 구하기(좌로 갈 때, 우로 갈 때 크기 비교하면 될듯) => 안됌(한 방향으로 쭉 가는게 아님)
    1 1 3 1
    1 1 3 1
def solution(name):
    res = 0
    startRight = 0
    startLeft = 0
    pointForRight = 0
    pointForLeft = 0
    for n in range(name):
        if name[i] != 'A':
            temp = abs(ord('A')- ord(n))
            temp = min(temp, abs(26-ord(n)))
            res += temp
            
            print(temp)
        
                
    print("res")
    print(res)
    
    res += min(startRight, startLeft)
    
    print(res)
    return res
'''