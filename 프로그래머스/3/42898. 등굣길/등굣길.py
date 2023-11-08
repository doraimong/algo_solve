'''
풀이전 생각
그냥 bfs 로 최단 거리의 개수 구하면 될듯?
dp버전이니까 1,1까지의 최단거리 개수 구하고 반복해 나가는 형식일까?
'''
def solution(m, n, puddles):# c,r
    mapL = [[0 for i in range(m+1)] for _ in range(n+1)]
    mapL[1][1] = 1
    for i in range(1, n+1):
        for j in range(1, m+1):
            if i == 1 and j == 1:
                continue
            if [j, i] in puddles:
                mapL[i][j] = 0
            else:
                mapL[i][j] = (mapL[i-1][j] + mapL[i][j-1]) % 1000000007
    return mapL[n][m]
