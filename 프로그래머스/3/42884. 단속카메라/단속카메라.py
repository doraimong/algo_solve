def solution(routes):
    res = 0
    # routes.sort()
    routes.sort(key = lambda x : x[1])
    pointNode = routes[0]
    for i in range(1, len(routes)):
        nowNode = routes[i]
        if pointNode[1] < nowNode[0]:
            pointNode = nowNode
            res+=1
            
    # print(routes)
    return res+1

# 1,2 / 3,4/ 5,6