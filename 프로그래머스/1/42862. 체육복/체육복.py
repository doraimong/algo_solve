def solution(n, lost, reserve):
    res = n
    tempDelReserve = []
    lost.sort()
    reserve.sort()
    for r in reserve:
        if r in lost:
            lost.remove(r)
            tempDelReserve.append(r)
            
    reserve = [i for i in reserve if i not in tempDelReserve]
    
    del1,del2 = 0,0
    reserve2 = [i for i in reserve]
    for l in lost:
        # print(l)
        if l - 1 in reserve:
            reserve.remove(l-1)
            continue
        elif l+1 in reserve:
            reserve.remove(l+1)
            continue
        del1 += 1
        
    for l in lost:
        # print(l)
        if l + 1 in reserve2:
            reserve2.remove(l+1)
            continue
        elif l-1 in reserve2:
            reserve2.remove(l-1)
            continue
        del2 += 1
        
    res -= min(del1, del2)
    print(res)
    print(lost)
    print(reserve)
    return res