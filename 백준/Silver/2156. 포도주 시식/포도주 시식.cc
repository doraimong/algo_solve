#include <iostream>
using namespace std;

int load[10001] = { 0 }, dp[10001] = { 0 };

int compare(int a, int b, int c) {
	return a >= b ? a >= c ? a : c : b >= c ? b : c;
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
	cin >> total;

	for (int i = 1; i <= total; i++)
	{
		//fscanf_s(fp, "%d", &load[i]);
		cin >> load[i];
	}

	dp[1] = load[1];
	dp[2] = dp[1] + load[2];

	for (int i = 3; i <= total; i++)
	{
		dp[i] = compare(dp[i - 3] + load[i - 1] + load[i], dp[i - 2] + load[i], dp[i - 1]);
	}

	cout << dp[total];

	return 0;
}