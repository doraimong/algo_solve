#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;


int main() {

    int get;
   cin >> get;

    vector<pair<long, long>> v;

    long temp1, temp2;
    bool zero = false;
    for (int i = 0; i < get; i++) {
       cin >> temp1 >> temp2;
        v.push_back({ temp2, temp1 });
    }
    //정렬
    sort(v.begin(), v.end());
    //solved
    int res = 1, beforeindex=0;
    for (int i = 1; i < v.size(); i++) {
        if (v[beforeindex].first <= v[i].second) {
           beforeindex = i;
           res++;
        }       
    }

    cout << res;

    return 0;
}