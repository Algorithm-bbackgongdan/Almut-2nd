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


int N, R, L;
int board[51][51];
int visited[51][51];

vector<pair<int, int>> v;
queue<pair<int, int>> q;

int dx[4] = { 1,0,-1,0 };
int dy[4] = { 0,1,0,-1 };
int sum = 0;
int day = 0;

bool flag = true;
void bfs(int x0, int y0) {
	visited[x0][y0] = 1;
	q.push(make_pair(x0, y0));

	while (!q.empty()) {
		int x = q.front().first;
		int y = q.front().second;
		q.pop();

		for (int i = 0; i < 4; ++i) {
			int nx = x + dx[i];
			int ny = y + dy[i];

			if ((0 <= nx && nx < N) && (0 <= ny && ny < N) && L <= abs(board[nx][ny] - board[x][y]) && abs(board[nx][ny] - board[x][y]) <= R && visited[nx][ny] != 1) {
				visited[nx][ny] = 1;
				sum += board[nx][ny];
				v.push_back({ nx,ny });
				q.push(make_pair(nx, ny));
			}
		}
	}
}
int main() {
	FIO;
	cin >> N >> L >> R;

	for (int i = 0; i < N; i++) {
		for (int j = 0; j < N; j++) {
			cin >> board[i][j];
		}
	}
	while (flag) {
		flag = false;
		for (int i = 0; i < N; i++) {
			for (int j = 0; j < N; j++) {
				if (!visited[i][j]) {
					sum = board[i][j];
					v.clear();
					v.push_back({ i,j });
					bfs(i, j);
				}
				if (v.size() >= 2) {
					flag = true;
					for (int i = 0; i < v.size(); i++) {
						board[v[i].first][v[i].second] = sum / v.size();
					}
				}
			}
		}
		if (flag) day++;

		memset(visited, 0, sizeof(visited));
	}

	cout << day;

}