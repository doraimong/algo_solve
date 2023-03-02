#include <iostream>
#include <queue>
using namespace std;

struct Type{
    int r,c;
};

int main()
{
    int dirR[] = {1, -1, 0, 0};
    int dirC[] = {0, 0, 1, -1};
    
    int R,C;
    cin>>R>>C;
    
    int map[R][C];
    int visit[R][C];
    
    int startR,startC;
    
    for(int i=0; i<R; i++){
        for(int j=0; j<C; j++){
            cin>>map[i][j];
            //visit[R][C] = 0;
            if(map[i][j] == 2){
                startR = i;
                startC = j;
            }
        }
    }
    
    
    // 2에서부터 시작
    queue<Type> q;
    q.push({startR, startC});
    //visit[startR][startC] = 1;
    
    while(!q.empty()){
        int r,c,cnt;
        r = q.front().r;
        c = q.front().c;
        
        q.pop();
        
        //map[r][c] = cnt;
        //visit[r][c] = 1;
        
        for(int i=0; i<4; i++){
            int nr,nc;
            nr = r + dirR[i]; nc = c + dirC[i];
            
            if(-1<nr && nr < R && -1<nc && nc < C){
                if(map[nr][nc] != 1)continue;
                
                map[nr][nc] = map[r][c] + 1; 
                q.push({nr,nc});
                
            }
            
            
        }
    }
    
    for(int i=0; i<R; i++){
        for(int j=0; j<C; j++){
            if(map[i][j] == 1)cout<<-1<<" ";
            else if(map[i][j] == 0)cout<<map[i][j]<<" ";
            else cout<<map[i][j]-2<<" ";
        }cout<<endl;
    }
    

    return 0;
}