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

vector <int> sequence[502];
int cnt[502];
int last_year_rank[502];
queue <int> new_rank;
int t, n, m;

int main() {
	FIO;
	cin >> t;
	for (int i = 0; i < t; i++) {
		bool flag_im = false;
		memset(last_year_rank, 0, sizeof(last_year_rank));
		memset(cnt, 0, sizeof(cnt));
		vector<vector<int>> sequence(502, vector<int>(502, 0));

		cin >> n;

		for (int j = 1; j <= n; j++) {
			int team;
			cin >> team;
			last_year_rank[j] = team;
		}
		for (int j = 1; j <= n; j++) {
			for (int k = j + 1; k <= n; k++) {
				int team_num = last_year_rank[j];
				sequence[team_num].push_back(last_year_rank[k]);
				cnt[last_year_rank[k]]++;
			}
		}

		cin >> m;

		for (int j = 1; j <= m; j++) {
			int a, b;
			cin >> a >> b;

			for (int k = 0; k < sequence[a].size(); k++) {
				if (sequence[a][k] == b) {
					flag_im = true;
				}
			}

			for (int k = 0; k < sequence[b].size(); k++) {
				if (sequence[b][k] == a) {
					sequence[b].erase(sequence[b].begin() + k);
					sequence[a].push_back(b);
					cnt[a]--;
					cnt[b]++;
				}
			}

		}
		if (flag_im == true) {
			flag_im = false;
			cout << "IMPOSSIBLE" << "\n";
			continue;
		}
		for (int j = 1; j <= n; j++) {
			if (cnt[j] == 0) new_rank.push(j);
		}
		if (new_rank.size() == 0) {
			cout << "?\n";
			break;
		}

		vector<int> ans;
		while (!new_rank.empty()) {
			int now = new_rank.front();
			new_rank.pop();
			ans.push_back(now);

			for (int j = 0; j < sequence[now].size(); j++) {
				int next = sequence[now][j];
				cnt[next]--;
				if (cnt[next] == 0) new_rank.push(next);
			}
		}
		for (int j = 0; j < ans.size(); j++) {
			cout << ans[j] << " ";
		}
		cout << "\n";
	}
}