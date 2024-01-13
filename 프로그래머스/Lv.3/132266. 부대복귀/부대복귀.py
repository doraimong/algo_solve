'''
1:1이 아닌 다:1 최단 경로를 찾아야한다 -> 최단 경로 알고리즘 학습 / n^2 이하 알고리즘

2.벨만-포드 (1:다)
- 시간 복잡도 (eN)
- 간선의 가중치가 음수에도 동작(음수 사이클 발생 시 최단거리 정의 불가 => 감지 및 중단 시켜야)
3. 워셜플로이드(다:다)
- 모든 노드 쌍 사이의 최단 거리를 탐색
- 시간 복잡도(N^3)
- 음의 가중치도 처리 가능 (음의 사이클 처리 불가)

1. 다익스트라(1:다)
방법 : 
1. 기록속 노드 거리 0
2. 시작 노드에서 다익스트라 함수 진행
3. 가까운 노드의 가중치를 갱신 & 
- 시작 노드에서 아직 방문하지 않은 노드 중 가장 가까운 노드 선택 -> 그 이웃에 대한 거리 업데이트
- 시간복잡도 O(N^2) , 우선순위 큐 사용시(elogN)
- 가중치 음수인 경우 작동 ㄴ
'''
from queue import Queue
import math, sys

def bfs(graph, start, visit):# 
    # print(start)
    visit[start] = 0
    q = Queue()
    q.put(start)
    # 내 주위 탐색 -> 값 갱신 & 추가
    while not q.empty():
        now_node = q.get()
        for next_node in graph[now_node]:
            if visit[next_node] == -1:
                visit[next_node] = visit[now_node] + 1
                q.put(next_node)
    
    return visit

def solution(n, roads, sources, destination): # 총 지역 수, 왕복 가능한 길, 부대원의 위치, 강철부대 지역
    answer = []
    visit = [-1] * (n+1) 
    graph_list = [[] for _ in range(n+1) ]
    # print(graph_list)
    for i,j in roads : 
        graph_list[i].append(j)
        graph_list[j].append(i)
    
    answer = bfs(graph_list, destination, visit)
    answer = [answer[i] for i in sources]
    
    return answer