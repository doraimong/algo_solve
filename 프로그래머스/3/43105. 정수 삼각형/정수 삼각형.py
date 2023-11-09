def solution(triangle):
    answer = 0
    size = max([len(i)for i in triangle])
    dp = [[0 for _ in range(size)] for _ in range(size)]
    dp[0][0] = triangle[0][0]
    for i in range(size-1):
        for j,num in enumerate(triangle[i]):
            dp[i+1][j] = max(dp[i+1][j], dp[i][j] + triangle[i+1][j])
            dp[i+1][j+1] = max(dp[i+1][j+1], dp[i][j] + triangle[i+1][j+1])
            
    # for i in dp:
    #     print(i)
    answer = max(dp[size-1])
    return answer