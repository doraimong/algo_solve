def solution(citations):
    answer = 0
    citations.sort()
    
    for h in range(citations[-1], 1, -1):
        more, less = 0,0
        for c2 in citations:
            if c2 >= h:
                more += 1
            else :
                less += 1
        if less <= h <= more:
            return h
    return answer