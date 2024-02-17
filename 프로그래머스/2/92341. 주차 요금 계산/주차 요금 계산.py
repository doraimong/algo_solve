'''
fee : 기본시간(분), 기본 요금, 단위 시간, 단위 요금
records : 시간, 차량 번호, 입출 여부
'''
import math
def solution(fees, records):
    def change(r): #한개의 records를 변환(시간-> 분)
        temp = r.split()
        a,b = map(int, temp[0].split(':'))
        return [a*60+b, temp[1], temp[2]]
    
    def changeFee(time): # 분단위 시간에 대한 요금 책정
        return math.ceil(max(0, (time - fees[0])) / fees[2]) * fees[3] + fees[1]
    
    answer = []
    records = list(change(r) for r in records)
    IN, OUT = [], []# 입,출에 대한 분리
    for r in records: IN.append(r) if r[2] == 'IN' else OUT.append(r)
    
    # 종료1 -> OUT기록이 없는 경우
    if len(OUT) == 0:
        answer.append(changeFee((23*60+59) - IN[0][0]))
        return answer
    
    parkingTimeDict = dict() # 차량 번호별 시간 저장
    for i in IN:
        if i[1] not in parkingTimeDict : parkingTimeDict[i[1]] = 0
        for idx,o in enumerate(OUT): 
            #IN, OUT기록 중 차량 번호 동일 & 입 출 기록이 있다 -> 출차 기록에 따라 시간 계산
            if i[1] == o[1] and i[0] <= o[0] : 
                parkingTimeDict[i[1]] += o[0] - i[0]
                break;
            # 출차 기록이 업는 경우(OUT 마지막까지 돌았는데도 for문 탈출 불가 -> 출차 기록이 없다(23:59))
            if idx == len(OUT)-1: 
                parkingTimeDict[i[1]] += (23*60+59) - i[0]
                
    temp = sorted(parkingTimeDict.items()) # 차량 번호 오름차순 정렬
    for i in temp:
        answer.append(changeFee(i[1]))
        
    # 종료 2
    return answer
