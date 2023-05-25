//참고 https://dontdiethere.tistory.com/77
#include <iostream>
using namespace std;

int main()
{
    int total;
    cin>>total;
    
    int arr[total], dpLeft[total], dpRight[total];

    for(int i=0; i<total; i++){
        cin >> arr[i];
    }

    //왼쪽에서 시작하는 최장 증가 부분수열
    for(int i=0; i<total; i++){
        dpLeft[i] = 1;
        for(int j=0; j<i; j++){
            if(arr[j] < arr[i])dpLeft[i] = max(dpLeft[i], dpLeft[j]+1);
        }
    }
    
    //오른쪽에서 시작하는 최장증가부분수열
    for(int i=total-1; i>-1; i--){
        dpRight[i] = 1;
        for(int j=total-1; j>i; j--){
            if(arr[i] > arr[j])dpRight[i] = max(dpRight[i], dpRight[j]+1);
        }
    }
    
    // 해당 인덱스의 좌,우 최장증가부분수열 값이 제일 큰 인덱스 선정
    int res = 0;
    for(int i=0; i<total; i++){
        res = max(res, dpLeft[i] + dpRight[i]);
    }
    cout<<res-1;

    return 0;
}