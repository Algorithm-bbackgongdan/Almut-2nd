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
bool near = false; //�����ϸ鼭 ���� ���� ��� �Ǵ�


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
			//x����� ����
			if (j % x == 0) {
				//�ð����
				if (d == 0) {
					for (int l = 1; l <= m; l++) {
						int next = l + k;
						if (next > m) {
							next = next % m;
						}
						arr[j][next] = arr[j][k];
					}
				}
				//�ݽð����
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
		// �����ϸ鼭 ���� ���� �ִ��� Ž��
		// �ִٸ�, �����ϸ鼭 ���� �� 0���� �ʱ�ȭ �� ���� �� ���ϱ�
		// ���ٸ�, ������ ����� ���ؼ� ū�� -1, ���� �� +1
	}
	//t�� ���� ��, ���ǿ� ���� ���� �� ���.
}