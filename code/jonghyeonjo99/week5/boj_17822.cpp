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

int n, m, t;
int arr[51][51];
bool near = false; //인접하면서 수가 같은 경우 판단


int main() {
	FIO;
	cin >> n >> m >> t;
	for (int i = 1; i <= n; i++) {
		for (int j = 1; j <= m; j++) {
			cin >> arr[i][j];
		}
	}
	for (int i = 0; i < t; i++) {
		int x, d, k;
		cin >> x >> d >> k;
		for (int j = 1; j <= n; j++) {
			//x배수의 원판
			if (j % x == 0) {
				//시계방향
				if (d == 0) {
					for (int l = 1; l <= m; l++) {
						int next = l + k;
						if (next > m) {
							next = next % m;
						}
						arr[j][next] = arr[j][k];
					}
				}
				//반시계방향
				else {
					for (int l = 1; l <= m; l++) {
						int next = l - k;
						if (next <= 0) {
							next += m;
						}
						arr[j][next] = arr[j][k];
					}
				}
			}
		}
		// 인접하면서 같은 수가 있는지 탐색
		// 있다면, 인접하면서 같은 수 0으로 초기화 후 남은 수 더하기
		// 없다면, 수들의 평균을 구해서 큰수 -1, 작은 수 +1
	}
	//t번 수행 후, 원판에 적힌 수의 합 출력.
}