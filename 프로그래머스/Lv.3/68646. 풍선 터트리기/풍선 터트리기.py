'''
구현문제

규칙 : 
1. 한개의 요소 기준 왼쪽 전체 최솟값(좌 최소값), 오른쪽 전체 최솟값(우 최소값)을 구함
2. 좌 최소값, 우 최소값 중 한개라도 현재 요소보다 크다면 살아남을 수 있다.

+ 특징 
0, -1 인덱스는 항상 생존 가능
ex> 
1. 0번 인덱스(이하 0번)를 기준으로 하면, 0번 기준 오른쪽 모든 요소 중 최소값(이하 오른쪽 최소값)을 구한다.
2. 해당 최소값이 0번 인덱스 빼고 나머지는 다 없앨 수 있따.
3. 0번과 오른쪽 최소값만 남는다. 여기서 무조건 오른쪽 최소값을 날릴 수 있다.([-1, 5] 라면 오른쪽이 크기 때문에, [5, -1]라면 작은 풍선 터뜨릴수 있기 때문)

'''

def solution(a):
    answer = 2
    left_min, right_min = [a[0]],[a[-1] for _ in range(len(a))]
    
    test = []
    right_min_val = a[-1]
    for i in range(1,len(a)-1): # 0, -1인덱스 값 제외 / 좌,우 최소값 탐색
        if left_min[-1] > a[i-1]:
            left_min.append(a[i-1])
        else :
            left_min.append(left_min[-1])
        
        if right_min_val > a[-1-i+1] : # 뒤에서부터 인덱스를 조절해서 최소값을 구함
            right_min[-1-i] = right_min_val = a[-1-i+1]
        else : 
            right_min[-1-i] = right_min_val
            
    
    for i in range(1,len(a)-1):# 해당 요소의 좌,우 최소값 중 하나라도 요소의 값보다 크면 해당 요소는 answer 추가
        if left_min[i] > a[i]:
            answer += 1
            test.append(a[i])
            continue
            
        if right_min[i] > a[i]:
            test.append(a[i])
            answer += 1
            continue
    
    return answer
