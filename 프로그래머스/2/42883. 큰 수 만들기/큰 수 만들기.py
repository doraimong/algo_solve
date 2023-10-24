def solution(number, k):
    stack = []
    
    for num in number:
        # print(stack)
        while stack and stack[-1] < num and k > 0:
            stack.pop()
            k-=1
        stack.append(num)
        # print(f"res = {stack}")
        
     # k가 남았다면 그 만큼 작은 숫자를 골라서 빼야함
    # temp = stack
    # temp = temp.sort()
    # print(stack)
    # for i in temp[:k]:
    #     stack.remove(i)
    # res = ''.join(stack)
        
    return ''.join(stack[:len(stack)-k])







'''
N,K = 0,0
res = -1
visit = []

def comb(cnt, start):
    global res
    
    if(cnt == K):
        
        print(visit)
        temp = int(''.join([N[i] for i in range(len(N)) if i not in visit]))
        # if temp == 194:
        #     print('ee')
        res = max(temp, res)
        return
    
    hopeful = str(res)[cnt]
    for i in range(start, len(N)):
         # res의 해당 자리수 vs 들어갈 수 -> 유망하면 진행
        print(f"유망 테스트 {hopeful} {N[i]} {cnt}번 인덱스")
        if hopeful < N[i]:
            print("통과")
            visit[cnt] = i
            comb(cnt+1, i+1)
            
    
def solution(number, k):
    global N,K,visit, res
    N, K= number, k
    visit = [0] * k
    res = int(number[:len(number)-k])
    print(f"시작 res {res}")
    print(str(res)[1])
    comb(0,0)
    
    return str(res)
'''