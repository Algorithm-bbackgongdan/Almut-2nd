#include <iostream>
#include <string>
#include <algorithm>
#include <vector>
#include <cmath>
#include <math.h>
#include <functional>
#include <queue>
#include <set>
#include <map>
#include <memory.h>
#define _CRT_SECURE_NO_WARNINGS
#define FIO cin.tie(0); cout.tie(0); ios::sync_with_stdio(0);
typedef long long ll;
using namespace std;
const int INF = 1e9;


int t, w, ans = 0;
int dropOrder[1001];
int dp[3][31][1001];
// dp[������ġ][����������Ƚ��][����ð�] = ���� ���� �ִ� �ڵ� ����

int main() {
	FIO;
	cin >> t >> w;
	for (int i = 1; i <= t; i++) {
		cin >> dropOrder[i];
	}
	memset(dp, -1, sizeof(dp));

	dp[1][w][0] = 0;

	for (int time = 0; time < t; time++) {
		for (int cnt = 0; cnt <= w; cnt++) {
			for (int pos = 1; pos <= 2; pos++) {
				if (dp[pos][cnt][time] >= 0) {
					int nextPos = dropOrder[time + 1];

					if (pos == nextPos) {	// ���� ��ġ�� �ڵΰ� ������
						dp[pos][cnt][time + 1] = dp[pos][cnt][time] + 1;
					}
					else {		// ���� ��ġ�� �ڵΰ� �������� ����
						if (cnt != 0) {	// �������� �ڵθ� �ݴ� ���
							dp[nextPos][cnt - 1][time + 1] = max(dp[nextPos][cnt - 1][time + 1], dp[pos][cnt][time] + 1);
						}				// �������� �ʴ� ���
						dp[pos][cnt][time + 1] = dp[pos][cnt][time];
					}
				};
			}
		}
	}
	// w�� ��� �Ҹ��ؼ� ���̻� �������� ���ϴ� ���� �ð��� t�� ��츦 ��� ��
	int ret = 0;
	for (int pos = 1; pos <= 2; pos++) {
		for (int time = 1; time <= t; time++) {
			ret = max(ret, dp[pos][0][time]);
		}
		for (int i = 0; i <= w; i++) {
			ret = max(ret, dp[pos][i][t]);
		}
	}
	cout << ret;
	return 0;
}