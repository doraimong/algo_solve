'''
투포인터

뒤에 부분수열 짧은게 나오면 채택, 길이가 같으면 채택 ㄴ
'''

def solution(sequence, k):
    answer = [0,999999999]
    start,end,total = 0,0,sequence[0]
    size = len(sequence)
    
    while start <= end < size:
        if total < k :
            end += 1
            if end < size:
                total += sequence[end]
                
        elif total > k :
            total -= sequence[start]    
            start += 1     
            
        elif total == k :
            if abs(answer[0]-answer[1]) > abs(start - end) : 
                answer[0], answer[1] = start, end
            total -= sequence[start]
            start += 1
            
    return answer