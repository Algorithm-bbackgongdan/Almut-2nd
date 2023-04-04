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
using namespace std;
const int INF = 1e9;

int v, e;
int arr[401][401];

void floyd(void) {
	for (int k = 1; k <= v; k++) {
		for (int i = 1; i <= v; i++) {
			for (int j = 1; j <= v; j++) {
				arr[i][j] = min(arr[i][j], arr[i][k] + arr[k][j]);
			}
		}
	}
}

int main() {
	FIO;

	cin >> v >> e;

	for (int i = 1; i <= v; i++) {
		for (int j = 1; j <= v; j++) {
			arr[i][j] = INF;
		}
	}

	for (int i = 0; i < e; i++) {
		int a, b, c;
		cin >> a >> b >> c;
		arr[a][b] = c;
	}

	floyd();

	int res = INF;
	for (int i = 1; i <= v; i++) {
		for (int j = 1; j <= v; j++) {
			if (arr[i][j] != INF && arr[j][i] != INF) {
				res = min(res, arr[i][j] + arr[j][i]);
			}
		}
	}
	if (res == INF) {
		res = -1;
	}
	cout << res;
}