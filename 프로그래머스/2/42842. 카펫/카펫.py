def solution(brown, yellow):
    answer = []
    hap = brown + yellow
    end = hap//2 + 1 if hap%2 == 0 else hap//2
    temp = int(1e9)
    # print(end)
    for i in range(1,end):
        # print(f'{temp} == {answer}')
        if hap % i != 0:continue
        
        if hap // i + i  <= temp and (hap // i + i -1)*2-2 == brown:
            answer = [hap // i, i]
            temp = (hap // i) + i
        # print(answer)
    return sorted(answer, reverse = True)