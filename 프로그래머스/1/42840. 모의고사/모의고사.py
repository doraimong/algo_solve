def solution(answers):
    answer = []
    first, second, third = [1, 2, 3, 4, 5], [2, 1, 2, 3, 2, 4, 2, 5], [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    lenFir, lenSec, lenThird = len(first), len(second), len(third)
    firstRes, secondRes, thirdRes = 0, 0, 0
    
    for i in range(len(answers)) : 
        if answers[i] == first[i % lenFir]:firstRes += 1
        if answers[i] == second[i % lenSec]:secondRes += 1
        if answers[i] == third[i % lenThird]:thirdRes += 1
    maxAnsCnt = max([firstRes, secondRes, thirdRes])
    
    if maxAnsCnt == firstRes: answer.append(1)
    if maxAnsCnt == secondRes: answer.append(2)
    if maxAnsCnt == thirdRes: answer.append(3)
    
    return answer