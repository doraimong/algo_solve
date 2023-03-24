#include <iostream>
#include <vector>
#include <queue>
#define INF 999999999
using namespace std;

int main(){
    
    int V, E, start;
    scanf("%d %d",&V, &E);
    scanf("%d",&start);
    //cin>>V>>E;
    // cin>>start;
    
    vector<pair<int,int>> v[V+1];
    int arr[V+1];
    for(int i=0; i<V+1; i++)arr[i] = INF;
    
    for(int i=0; i<E; i++){
        int a,b,c;
        scanf("%d %d %d",&a, &b ,&c);
        // cin>>a>>b>>c;
        v[a].push_back({b,c});
    }
    
    arr[start] = 0;
    
    priority_queue<pair<int, int>> pq;
    pq.push({0, start});
    
    while(!pq.empty()){
        int dis = -pq.top().first;
        int now = pq.top().second;
        pq.pop();
        
        //해당 위치에서 다음노드까지 거리 갱신
        //현재 노드에서 연결된 애들 보기
        for(int i=0; i<v[now].size(); i++){
            int w = v[now][i].second;
            int next = v[now][i].first;
            
            if(dis + w < arr[next]){
                arr[next] = dis + w;
                pq.push({-arr[next], next});
            }
        }
    }
    for(int i=1; i<=V; i++){
        if(arr[i] == INF)cout<<"INF"<<endl;
        else cout<<arr[i]<<endl;
    }


    return 0;

}