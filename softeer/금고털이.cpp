// 참고 https://0urtrees.tistory.com/304
#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;

using namespace std;

int main(int argc, char** argv)
{
int W,N;
    cin>>W>>N;
    
    int arr[N][2];
    vector<pair<int, int>> v;
    
    for(int i=0; i<N; i++){
        int a,b;
        cin>>a>>b;
        v.push_back({b, a});
    }
    
    sort(v.begin(), v.end());
    
    int res=0;
    for(int i=N-1; i>-1; i--){
        if(W-v[i].second >= 0) {
			 W -= v[i].second;
			 res += v[i].second * v[i].first;
		 }else {
			 res += W * v[i].first;
			 break;
		 }	
    }
    
    cout<<res;
}

