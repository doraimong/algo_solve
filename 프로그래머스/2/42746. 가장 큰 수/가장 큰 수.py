'''
사전 순 정렬
숫자의 길이를 늘려서 비교하기
ex> 3, 30, 34
-3, 30은 3이 먼저 와야함
이것을 역사전순으로 비교하기 위해 길이연장(숫자*3) 333, 303030 -> 333 - 303비교 => 3(큰것)이 앞에 오게 된다.

-3, 34는 34가 먼저 와야함
333 - 343434 -> 333, 343 => 343(큰것)이 앞에 오게 된다.
'''
def solution(numbers):
    answer = ''
    
    if all(num == 0 for num in numbers):
        return '0'
    
    numbers = list(map(str, numbers))
    numbers.sort(key= lambda i: i*3, reverse=True)
    answer = ''.join(numbers)
    
    return answer