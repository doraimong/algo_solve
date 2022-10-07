
#include <iostream>
#include "algorithm"
#include <vector>
using namespace std;

int L,C;	//L : 암호 갯수 / C: 주어지는 문자열 개수  
vector<char> v;
vector<int> res;

bool check(){
	int vowel=0;
	for(int i=0; i<res.size(); i++){
		char temp=v[res[i]];
		if(temp == 'a' || temp == 'e' || temp == 'i' || temp == 'o' || temp == 'u' )
			vowel++;
	}
	
	if(vowel>=1 && L-vowel>=2)return true;
	else return false;
	
}

void dfs(int idx){
	//출력 
	if((int)res.size() == L && check()){
		for(int i : res){
			printf("%c",v[i]);
		}
		printf("\n");
		return;
	}
	
	//출력이 아닌 상황  
	for(int i=idx+1; i<C; i++){
		res.push_back(i);
		dfs(i);
		res.pop_back();
	}
	
}

int main(){
	cin>>L>>C;
	
	for(int i=0; i<C; i++){
		char c;
		cin>>c;
		v.push_back(c);
	}
	
	sort(v.begin(), v.end());
	for(int i=0; i<v.size(); i++){
		res.push_back(i);
		dfs(i);
		res.pop_back();
	}
	
	
	return 0;
}