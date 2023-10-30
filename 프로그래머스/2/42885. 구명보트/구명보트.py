'''
생각
방법1:정렬/최소 값부터 모으기?

방법2:


1. 정렬ㄴㄴ -> 최대한 배를 가득 채울 수 있는 무게들이 정렬한다고 구해지는게 아님(배낭문제 같은데 풀이법 생각 안나네)

'''
def solution(people, limit):
    res = 0
    people.sort()
    l,r=0,len(people)-1
    
    while(l<=r):
        if people[l] + people[r] <= limit:
            l +=1
            r -=1
            res +=1
        else:
            r -=1
            res +=1
    
    return res