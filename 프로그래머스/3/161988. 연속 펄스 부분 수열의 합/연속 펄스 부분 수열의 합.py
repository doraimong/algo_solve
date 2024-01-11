'''
sequence * 1부터 시작 수열 / -1부터 수열 적용
최장 증가 부분 수열
20만개 원소 -> 대략의 시간 복잡도 예상 -> 시간복잡도별 알고리즘 종류 학습, 
제곱이하

'''
def solution(sequence):
    answer, best1, best2 = 0,0,0
    
    # 펄스 수열 1부터 시작
    for i,s in enumerate(sequence):
        if i % 2 == 0 : # 1
            best1 = max(s, best1+s)
        else : # * -1
            best1 = max(best1 -s,-s)
        answer = max(answer, best1)
    
    # 펄스 수열 -1부터 시작
    for i,s in enumerate(sequence):
        if i % 2 == 0 : # -1
            best2 = max(best2 -s, -s)
        else : # * 1
            best2 = max(s ,best2 + s)
        answer = max(best2, answer)
    
    return answer