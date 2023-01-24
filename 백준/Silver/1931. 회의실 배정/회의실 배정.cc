#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;

int main()
{
    int total;
    cin>>total;
    
    vector<pair<long, long>> arr;
    
    for(int i=0; i<total; i++){
        long a,b;
        cin>>a>>b;
        arr.push_back({b,a});//0 종료 1 시작
    }
    
    sort(arr.begin(), arr.end()); 
    
    long start = arr[0].first;
    long res=1;
    
    
    
    for(int i=1; i<total; i++){
        if(start <= arr[i].second){
            res++;
            start = arr[i].first;
        }
    }
    
    cout<<res;
 
    return 0;
}