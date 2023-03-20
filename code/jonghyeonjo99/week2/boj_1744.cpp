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

int n;
int sum = 0;
int num_mi = 0;
int num_pl = 0;
bool check_0 = false;
vector <int> v;
vector <int> mi;

int main() {
	FIO;
	cin >> n;

	for (int i = 0; i < n; i++) {
		int a;
		cin >> a;
		v.push_back(a);
	}

	sort(v.rbegin(), v.rend());

	for (int i = 0; i < n; i++) {
		if (v[i] > 0) num_pl++;
		if (v[i] <= 0) {
			mi.push_back(v[i]);
			if (v[i] < 0) num_mi++;
			if (v[i] == 0) check_0 = true;
		}
	}

	sort(mi.begin(), mi.end());

	for (int i = 0; i < n - 1; i += 2) {
		if (v[i + 1] > 1) {
			sum += v[i] * v[i + 1];
		}
		else if (0 < v[i + 1] && v[i + 1] <= 1) {
			sum += v[i + 1] + v[i];
		}
	}
	if (num_pl % 2 == 1) sum += v[num_pl - 1];

	//음수가 짝수개
	if (num_mi % 2 == 0) {
		for (int i = 0; i < num_mi; i += 2) {
			sum += mi[i] * mi[i + 1];
		}
	}
	//음수가 1개
	else if (num_mi == 1) {
		//0이 있음
		if (check_0 == true) {
			sum += mi[0] * mi[1];
		}
		else sum += mi[0];
	}
	// 음수가 홀수개 있을 때 (1개 아님)
	else if (num_mi != 1 && num_mi % 2 == 1) {
		//0이 있음
		if (check_0 == true) {
			for (int i = 0; i < mi.size(); i += 2) {
				sum += mi[i] * mi[i + 1];
			}
		}
		//0 없음
		else {
			for (int i = 0; i < mi.size() - 2; i += 2) {
				sum += mi[i] * mi[i + 1];
			}
			sum += mi[mi.size() - 1];
		}
	}

	cout << sum;
}