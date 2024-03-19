'''
타겟이 50만 -> 2중 for 금지
그리디, dp 중 해결
'''
def solution(targets):
    answer = 0
    targets = sorted(targets, key=lambda x : x[1])
    e=0
    for t in targets:
        if e <= t[0]:
            answer += 1
            e = t[1]
            
    return answer
