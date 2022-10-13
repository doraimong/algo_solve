#include <iostream>
#include <vector>
#include <cstring>
using namespace std;

vector<pair<int, int>> v[100003];
int visit[100003] = { 0 };
int mostdis=0, mostdes=0, moststart=0;

void dfs(int location, int cost) {
	visit[location] = 1;
	int tempsize = v[location].size();
	
	for (int i = 0; i < tempsize; i++) {
		int nextnode = v[location][i].first;
		
		//방문한적 없으면 
		if (visit[nextnode] == 0) {
			dfs(nextnode, cost + v[location][i].second);
		}
	}

	if (mostdis < cost) {
		mostdis = cost;
		mostdes = location;
		//moststart = -1;
	}
}

int main() {
	/*FILE* fp;
	fopen_s(&fp, "test.txt", "r");
	if (fp == NULL) {
		cout << "파일 없음";
		return 1;
	}*/

	int total;
	//fscanf_s(fp, "%d", &total);
	scanf("%d",&total);
	
	for (int i = 0; i < total; i++) {
		int x, y, size=0;
		//fscanf_s(fp, "%d", &x);
		scanf("%d", &x);
		while (1) {
			//fscanf_s(fp, "%d", &y);
			scanf("%d", &y);
			if (y == -1)break;
			else /*fscanf_s(fp, "%d", &size);*/  scanf("%d", &size);
			v[x].push_back({ y, size });
		}
	}
	
	/*for (int i = 1; i <= total; i++) {
		int temp ;
		for (int ii = 0; ii <  v[i].size(); ii++) {
			cout << v[i][ii].first << " "<< v[i][ii].second<<"  ";
		}
		cout << endl;
	}*/
	
	//for (int i = 1; i <= total; i++) {
		//cout << i << " 노드의 탐색(main함수)" << endl;
		dfs(1, 0);
		//if (moststart == -1)moststart = i;
		memset(visit, 0, sizeof(visit));
		dfs(mostdes, 0);

	//}

	//dfs(1, 0);
	cout << mostdis << endl;


	return 0;
}