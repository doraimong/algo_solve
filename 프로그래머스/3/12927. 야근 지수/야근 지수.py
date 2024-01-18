'''
힙에 넣고 빼주기, -1 작업
'''
import heapq

def solution(n, works):
    answer = 0
    
    # 우선순위 큐 생성 및 *-1을 이용한 정렬
    works = [-i for i in works]
    heapq.heapify(works)
        
    # n > 0 이거나 pq에 요소가 있으면, 야근 피로도 감소
    while n > 0 and len(works) != 0:
        w = -heapq.heappop(works)
        w -= 1
        n -= 1
        if w == 0:continue
        heapq.heappush(works, -w)
    
    # 제곱 계산
    answer = sum([i*i for i in works])
    
    return answer