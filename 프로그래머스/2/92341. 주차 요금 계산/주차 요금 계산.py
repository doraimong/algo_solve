'''
fee : 기본시간(분), 기본 요금, 단위 시간, 단위 요금
records : 시간, 차량 번호, 입출 여부
'''
import math
def solution(fees, records):
    def change(r):
        temp = r.split()
        a,b = map(int, temp[0].split(':'))
        return [a*60+b, temp[1], temp[2]]
    
    def changeFee(time):
        if time <= fees[0]:
            return fees[1]
        else:
            return int(math.ceil((time - fees[0]) / fees[2]) * fees[3]) + fees[1]
    
    answer = []
    
    records = list(change(r) for r in records)
        
    IN, OUT = [], []
    for r in records: IN.append(r) if r[2] == 'IN' else OUT.append(r)
      
    if len(OUT) == 0:
        answer.append(changeFee((23*60+59) - IN[0][0]))
        return answer
    
    answerDict = dict()
    for i in IN:
        if i[1] not in answerDict : answerDict[i[1]] = 0
        for idx,o in enumerate(OUT): # OUT기록을 돌리기
            if i[1] == o[1] and i[0] <= o[0] : # IN, OUT기록 중 차량 번호 동일 & 입 출 기록이 알맞다면 시간에 맞게 계산
                answerDict[i[1]] += o[0] - i[0]
                break;
            # 출차 기록이 업는 경우
            if idx == len(OUT)-1: 
                answerDict[i[1]] += (23*60+59) - i[0]
                
    print(answerDict)
    temp = sorted(answerDict.items())
    for i in temp:
        answer.append(changeFee(i[1]))
        
    return answer