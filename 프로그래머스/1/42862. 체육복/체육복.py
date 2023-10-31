def solution(n, lost, reserve):
    
    lost.sort()
    reserve.sort()
    
    res = n
    tempDelReserve = []
    for r in reserve:
        if r in lost:
            lost.remove(r)
            tempDelReserve.append(r)
            
    reserve = [i for i in reserve if i not in tempDelReserve]
    
    del1 = 0
    for l in lost:
        if l - 1 in reserve:
            reserve.remove(l-1)
            continue
        elif l+1 in reserve:
            reserve.remove(l+1)
            continue
        del1 += 1
        
    res -= del1
    return res

'''
개선코드
def solution(n, lost, reserve):
    # 중복되는 학생을 제거
    set_reserve = set(reserve) - set(lost)
    set_lost = set(lost) - set(reserve)
    
    for r in set_reserve:
        if r - 1 in set_lost:
            set_lost.remove(r - 1)
        elif r + 1 in set_lost:
            set_lost.remove(r + 1)

    return n - len(set_lost)
'''