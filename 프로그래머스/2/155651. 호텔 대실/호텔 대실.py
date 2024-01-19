'''
그리디 같은데 / 종료 시간을 기준으로 정렬해서하는 ....

시작 시간 정렬 후 정답 개수만큼 while?
1000 000
n^2 

time list 만들기
'''
def solution(book_time):
    answer = 0
    for i,b in enumerate(book_time): # 한세트의 start, end
        start,end = int(b[0].replace(":","")), int(b[1].replace(":",""))
        book_time[i] = [start//100*60 + start%100, end//100*60 + end%100+9]
    book_time.sort()
    
    time = [0] * 1450
    
    for b in book_time :
        for i in range(b[0], b[1]+1):
            time[i] += 1
    
    answer = max(time)
    return answer
