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
#define _CRT_SECURE_NO_WARNING
#define FIO cin.tie(0); cout.tie(0); ios::sync_with_stdio(0);
using namespace std;
const int INF = 1e9;

int n, m, s, e;
priority_queue<pair<int, int>, vector<pair<int, int>>, greater<pair<int, int>> >pq; //√÷º“»¸
vector <int> dist(1001, INF);
vector<pair<int, int>> edge[1001];
int arr[1001];

void dijkstra() {
	pq.push(make_pair(0, s));
	dist[s] = 0;

	while (!pq.empty()) {
		int cost = pq.top().first;
		int here = pq.top().second;
		pq.pop();

		if (dist[here] < cost) continue;
		for (int i = 0; i < edge[here].size(); i++) {
			int next = edge[here][i].first;
			int nextcost = edge[here][i].second;

			if (dist[next] > dist[here] + nextcost) {
				dist[next] = dist[here] + nextcost;
				pq.push(make_pair(dist[next], next));
				arr[next] = here;
			}
		}
	}
}

int main() {
	FIO;
	cin >> n >> m;
	for (int i = 0; i < m; i++) {
		int a, b, c;
		cin >> a >> b >> c;
		edge[a].push_back(make_pair(b, c));
	}
	cin >> s >> e;

	dijkstra();

	cout << dist[e] << "\n";

	vector <int> res;
	res.push_back(e);
	int city = arr[e];
	while (city) {
		res.push_back(city);
		city = arr[city];
	}

	cout << res.size() << "\n";

	for (int i = res.size() - 1; i >= 0; i--) {
		cout << res[i] << " ";
	}

}