def solution(alp, cop, problems):
    answer = 0
    goalA, goalC = 0,0
    for p in problems:
        goalA = max(goalA, p[0])
        goalC = max(goalC, p[1])
    
    dp = [[1e9] * (goalC+2) for _ in range(goalA+2)]
    alp, cop = min(alp, goalA), min(cop, goalC)
    dp[alp][cop] = 0
    
    for i in range(alp, goalA+1):
        for j in range(cop, goalC+1):
            dp[i+1][j] = min(dp[i+1][j], dp[i][j]+1)
            dp[i][j+1] = min(dp[i][j+1], dp[i][j]+1)
            for p in problems:
                if i >= p[0] and j >= p[1]:
                    na, nc = min(i + p[2], goalA), min(j + p[3], goalC)  
                    dp[na][nc] = min(dp[na][nc], dp[i][j] + p[4])
            
    return dp[goalA][goalC]
