#include <iostream>
#include <vector>
#include <queue>    
#define inf 99999999
using namespace std;

int dist[1001];
vector<pair<int, int>> vec[100001];

void dijkstra(int start){
    dist[start] = 0;    //시작 위치 가중치 설정
    
    // 힙에 값 넣기
    priority_queue<pair<int, int>> pq;
    pq.push({dist[start], start});
    
    // 노드의 개수만큼 루트
    while(!pq.empty()){ 
        int cur = pq.top().second;    // 큐의 맨 앞에 최솟값 가지고 있다.
        int distance = pq.top().first * -1;
        
        pq.pop();
        
        if(dist[cur] < distance)continue;    ///이미 담겨있는 것보다 distance가 크면 넘어감
        
        //인접 노드 확인
        for(int i=0; i < vec[cur].size(); i++){
            int next = vec[cur][i].first;
            int nextDistance = distance + vec[cur][i].second;
            
            // 다음 것과 기존의 내용 비교
            if(nextDistance < dist[next]){
                dist[next] = nextDistance;
                pq.push({nextDistance * -1, next});
            }
        }
        
    }
}

int main()
{
    int N, M, start, dest;
    cin>>N;
    cin>>M;
    
    //cout<<N<<" "<<M<<endl;
    
    for(int i=0; i<M; i++){
        int a,b,c;
        cin>>a>>b>>c;
        vec[a].push_back({b,c}); //시작점 a, 도착점 b, 가중치 c
    }
    
    cin>>start>>dest;
    
    // 가중치 초기 세팅 ㄱㄱ
    for(int i=0; i<=N; i++){
        dist[i] = inf;
    }
    
    dijkstra(start);
    
    cout << dist[dest];

    return 0;
}