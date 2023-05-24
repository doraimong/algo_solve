#include <iostream>
using namespace std;

int load[1001] = { 0 }, load1[1001] = { 0 }, dp[1001] = { 0 }, dp1[1001] = { 0 };

int main() {
	int total;
	cin >> total;

	//입력
	for (int i = 1; i <= total; i++)
	{
		int get;
		cin >> get;
		load[i] = load1[total+1-i] = get;

	}

	//solve
	int res = 0, res1 = 0;
	for (int i = 1; i <= total; i++)
	{
		int top = 0, top1 = 0;
		for (int ii = 1; ii < i; ii++)
		{
			if (load[i] > load[ii])top = max(top, dp[ii]);
			if (load1[i] > load1[ii])top1 = max(top1, dp1[ii]);
		}
		dp[i] = top + 1;
		dp1[i] = top1 + 1;
		res = max(res, dp[i]);
		res1 = max(res1, dp1[i]);
	}
	int maxres = 0;
	for (int i = 1; i <= total; i++)
	{
		dp[i] += dp1[total+1-i];
		maxres = max(maxres, dp[i]);
	}
	cout << maxres-1 << endl;
	return 0;
}