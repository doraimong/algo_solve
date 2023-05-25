#include <iostream>
using namespace std;

int main() {
	int total;
	cin >> total;

	int load[100001] = { 0 }, dp[100001] = {0};
	
	//입력
	for (int i = 1; i <= total; i++)
	{
		int get;
		cin >> load[i];

	}

	//solve
	int res = -10000;
	for (int i = 1; i <= total; i++)
	{
		dp[i] = max(dp[i - 1] + load[i], load[i]);
		res = max(res, dp[i]);
	}
	cout << res;
	return 0;
}