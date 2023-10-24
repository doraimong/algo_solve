def solution(number, k):
    stack = []
    
    for num in number:
        while stack and stack[-1] < num and k > 0: # 앞의 수보다 뒤의 수(num)이 크고 and 뺄 개수가 아직 남으면 
            stack.pop()
            k-=1
        stack.append(num)
        
    # 앞은 큰수 뒤는 작은 수 구조가 된다. -> 뒤에서 남은 k 만큼만 빼주면 됌
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