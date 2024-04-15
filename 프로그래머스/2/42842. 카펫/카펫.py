'''
brown + yellow 하면 카페트 크기가 나온다 -> 가로, 세로가 될수 있는 케이스 확보(1)
위 케이스에서 나온 가로,세로를 임의로 지정(맨 마지막에 역정렬)
가로, 세로로 brown격자의 수가 맞는지 확인

'''
def solution(brown, yellow):
    answer = []
    hap = brown + yellow
    #brwon + yellow(넓이)를 이용해 가로 or 세로가 될 수 있는 수의 절반값(ex> 넓이가 20 이면 11이 end값이 된다.)
    end = hap//2 + 1 if hap%2 == 0 else hap//2 
    
    for i in range(1,end):
        if hap % i != 0:continue
        w,h = hap // i, i # wid,height를 임의로 지정(나중에 역정렬)
        
        if (w + h -1)*2-2 == brown: # brown격자의 개수와 같다면 정답
            answer = [w, h]
            
    return sorted(answer, reverse = True)
