'''
1. bfs로 계속 해 나가다 보면 나오는거 아닌가 싶은데

1. 5로 만들수 있는 수를 만들고 그때 사용한 5의 개수를 저장, 
2. 그 수로 12를 만들고 그 수의 dp값을 찾아서 더해주기?
?1. 그 수의 dp 값을 다 채울 수 있나?
'''

def solution(N, number):
    dp = [set() for _ in range(9)]
    for i in range(1, 9):
        dp[i].add(int(str(N) * i))
        for j in range(1, i):
            for x in dp[j]:
                for y in dp[i - j]:
                    dp[i].add(x + y)
                    dp[i].add(x - y)
                    dp[i].add(y - x)
                    dp[i].add(x * y)
                    if y != 0:
                        dp[i].add(x // y)
                    if x != 0:
                        dp[i].add(y // x)
        if number in dp[i]:
            return i
    return -1



'''
def solution(N, number):
    dp = [set()]
    dp[0].add(N)
    ans = 0
    def solve():
        for i in range(1, 7):
            # print(f"i값 : {i}")
            # dp.append(set())
            # dp[i].add(int('5'*(i+1)))
            dp.append({int(str(N)*(i+1))})
            for a in range(0, int(i/2)+1):
                b = i-a
                # print(f"{a} {b}")
                temp = set()
                for valA in dp[a]:
                    for valB in dp[b]:
                        temp.update([valB-valA, valA-valB, valA+valB, valA*valB])
                        if valB != 0:
                            temp.add(valA//valB)
                        if valA != 0:
                            temp.add(valB//valA)
                dp[i].update(temp)
        
    solve()
    
    for idx, i in enumerate(dp):
        if number in i:
            return idx+1
    return -1
    '''