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

int n, k;
int cnt = 0;
vector <int> sensor;
vector <int> res;

int main() {
    FIO;
    cin >> n >> k;
    for (int i = 0; i < n; i++) {
        int s;
        cin >> s;
        sensor.push_back(s);
    }
    sort(sensor.begin(), sensor.end());

    for (int i = 1; i < n; i++) {
        int distance = sensor[i] - sensor[i - 1];
        res.push_back(distance);
    }

    sort(res.begin(), res.end());

    for (int i = 0; i < n - k; i++) {
        cnt += res[i];
    }
    cout << cnt;

    return 0;
}