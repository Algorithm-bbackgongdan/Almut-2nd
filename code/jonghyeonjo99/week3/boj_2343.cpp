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

ll n, m;
ll lec[100001];
vector <ll> v;

int main() {
	FIO;
	ll total = 0;
	ll cnt = 0;
	ll temp = 0;
	ll left = 0;
	cin >> n >> m;
	for (int i = 0; i < n; i++) {
		cin >> lec[i];
		total += lec[i];
		left = max(left, lec[i]);
	}
	ll right = total;
	while (left <= right) {
		ll mid = (left + right) / 2;
		for (int i = 0; i < n; i++) {
			temp += lec[i];
			if (temp > mid) {
				temp -= lec[i];
				cnt++;
				temp = lec[i];
			}
			if (i == n - 1) {
				temp = 0;
				cnt++;
			}
		}
		if (cnt <= m) {
			right = mid - 1;
			cnt = 0;
		}
		else if (cnt > m) {
			left = mid + 1;
			cnt = 0;
		}
	}
	cout << left;
}