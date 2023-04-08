# 3665 : 최종순위
### code
```c++
  //나의 코드
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

//답안 코드
#include <bits/stdc++.h>
using namespace std;

bool adj[501][501];
int degree[501];


int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);
    
    int t;
    cin >> t;
    for (int T = 0; T < t; T++) {

        memset(adj, 0, sizeof(adj));
        memset(degree, 0, sizeof(degree));
        int n;
        cin >> n;

        vector<int> pre;
        for (int i = 0; i < n; i++) {
            int tmp;
            cin >> tmp;
            pre.push_back(tmp);
        }

		for (int i = 0; i < pre.size(); i++) {
            for (int j = i + 1; j < pre.size(); j++) {
                adj[pre[i]][pre[j]] = 1;
                degree[pre[j]]++;
            }
        }

        int m;
        cin >> m;


        for (int i = 0; i < m; i++) {
            int a, b;
            cin >> a >> b;

            if (adj[a][b] == 1) {
                adj[a][b] = 0;
                degree[b]--;
                adj[b][a] = 1;
                degree[a]++;
            }
            else {
                degree[a]--;
                adj[b][a] = 0;
                adj[a][b] = 1;
                degree[b]++;
            }
        }

        
        queue<int> Q;

        for (int i = 1; i <= n; i++) {
            if (degree[i] == 0) {
                Q.push(i);
            }
        }

        vector<int> ans;

        bool cantKnow = false;

        while (!Q.empty()) {

            if (Q.size() >= 2) {
                cantKnow = true;
                break;
            }

            int x = Q.front(); Q.pop();
            ans.push_back(x);

            for (int i = 1; i <= n; i++) {
                if (adj[x][i] == 1) {
                    int nx = i;

                    if (--degree[nx] == 0) {
                        Q.push(nx);
                    }

                }
            }
        }

        if (cantKnow) {
            cout << "?\n";
            continue;
        }


        if (ans.size()!=n) {
            cout << "IMPOSSIBLE\n";
            continue;
        }
        else {
			for (auto x : ans) {
				cout << x << ' ';
			}
			cout << '\n';
        }


    }
  
    return 0;
}
  ```
## 결과
실패 후 책을 통한 학습
## 접근
1. 작년 순위의 순서를 미리 저장한다.
2. 입력에 주어지는 올해 변동된 순위를 갱신한다.
    - 갱신 과정에서 작년순서와 동일한데, 변동사항에 있는 경우 논리적 오류로 판단 -> "IMPOSSIBLE" 출력
3. 갱신 후 진입차수가 0인 노드를 queue에 push.
    - 이 때, 진입차수가 0인 노드가 없다면, 경우의 수가 1개가 아님을 의미 -> "?" 출력
4. while문을 반복하여 정해진 순서대로 순위 결정.
## 문제 회고
IMPOSSIBLE과 ?의 경우를 찾는데 상당히 애를 먹었다.
노트에 적어가며 나름 경우의 수를 찾을려고 노력했다. 

그 결과, 작년과 순위가 동일한데 변동되었다고 입력되는 경우(논리적 오류)와 올해 순위가 1개로 정해지지 않는 경우에는 진입차수가 0인 노드가 없다는 규칙을 찾아 코드로 옮겨보았다. 테스트 케이스는 통과하였지만, 채점결과 항상 25% 쯤에서 오답처리가 되었다. 결국 스터디 교재의 문제 해설을 보고 학습하였다.

해설 코드와 내 코드를 비교하면서 작년 순서를 저장하는 간결한 방법과, 작년과 같은 순서가 주어졌을 때 간선방향을 뒤집어 사이클이 발생하였음을 확인할 수 있는 방법을 배울 수 있었다. 
# 17472 : 다리 만들기2
### code
```c++
#include<iostream>
#include<algorithm>
#include<vector>
#include<queue>
#include<tuple>
using namespace std;

int N, M, ans;
int island_num; // 섬 개수
int map[11][11];
int visit[11][11];
int island_visit[7];
int parent[7];
int dx[4] = { 1,-1,0,0 };
int dy[4] = { 0,0,1,-1 };
vector<tuple<int, int, int>> vec; // {거리, 섬1, 섬2}
vector<int> graph[7];
queue<int> q;

int find(int u)
{
	if (u == parent[u]) return u;
	else return find(parent[u]);
}

bool union_island(int u, int v)
{
	u = find(u);
	v = find(v);

	if (u != v)
	{
		// 노드 결합
		parent[u] = v;

		// 섬 간의 연결관계 기록
		graph[u].push_back(v);
		graph[v].push_back(u);
		return true;
	}
	else return false;
		
}

// 섬 번호 부여하기
void DFS(int x, int y)
{
	if (visit[x][y]) return;
	
	visit[x][y] = true; // 방문 표시
	map[x][y] = island_num; // 섬 번호

	for (int i = 0; i < 4; i++)
	{
		int next_x = x + dx[i];
		int next_y = y + dy[i];

		if (next_x >= 1 && next_x <= N && next_y >= 1 && next_y <= M)
		{
			if (map[next_x][next_y] != 0 && !visit[next_x][next_y])
				DFS(next_x, next_y);
		}
	}
}

// 섬 간의 최소거리 구하기
void distance(int now, int x, int y)
{
	for (int i = 0; i < 4; i++)
	{
		int now_x = x;
		int now_y = y;
		int dist = 0;

		while (true)
		{
			now_x += dx[i];
			now_y += dy[i];
			
			// 범위 이탈 또는 현재 섬일 경우 탈출
			if (now_x < 1 || now_x > N || now_y < 1 || now_y > M || map[now_x][now_y] == now) break;

			if (map[now_x][now_y] != 0)
			{
				// {거리, 출발한 섬, 도착한 섬} push
				vec.push_back({ dist , now, map[now_x][now_y] });
				break;
			}
			dist++;
		}
	}
}

int main()
{
	ios::sync_with_stdio(0);
	cin.tie(0);

	cin >> N >> M;

	// 초기 세팅
	for (int i = 1; i <= 6; i++)
		parent[i] = i; // 자기 자신을 부모로 지정

	// 섬 정보 입력받기
	for (int i = 1; i <= N; i++)
		for (int j = 1; j <= M; j++)
			cin >> map[i][j];

	// 섬 번호 부여하기
	for (int i = 1; i <= N; i++)
		for (int j = 1; j <= M; j++)
		{
			if (map[i][j] != 0)
			{
				if(!visit[i][j]) island_num++;
				DFS(i, j);
			}
		}

	// 섬 간의 거리 구하기
	for (int i = 1; i <= N; i++)
		for (int j = 1; j <= M; j++)
		{
			if (map[i][j] != 0)
			{
				distance(map[i][j], i, j);
			}
		}

	sort(vec.begin(), vec.end());

	// MST 구하기
	for (int i = 0; i < vec.size(); i++)
	{
		int dist = get<0>(vec[i]);
		int island_1 = get<1>(vec[i]);
		int island_2 = get<2>(vec[i]);

		// 다리길이가 2미만이면 패스!
		if (dist < 2) continue;

		// 두 섬간의 다리 건설 시
		if (union_island(island_1, island_2))
			ans += dist;
	}

	// 섬이 모두 연결되어 있는지 확인
	int cnt = 1;
	q.push(1);

	while (!q.empty())
	{
		int now_island = q.front();
		q.pop();
		island_visit[now_island] = true;

		for (int i = 0; i < graph[now_island].size(); i++)
		{
			int next_island = graph[now_island][i];
			if (!island_visit[next_island])
			{
				q.push(next_island);
				cnt++;
			}
		}
	}

	if (cnt != island_num) cout << -1 << '\n';
	else cout << ans << '\n';
}
  ```
## 결과
실패 후 구글링..
## 접근
1. 1로 구분되어있는 섬에 번호를 부여해준다. (DFS)
2. 섬과 섬 사이를 이어주는 다리를 만든다.
3. 섬과 섬을 이어주는 다리들 중 최소거리를 구한다.(크루스칼 알고리즘을 활용하여 최소신장트리만들기)
4. 모든 섬들이 다리를 통해 연결되어있는지 확인.
## 문제 회고
여태 풀어본 문제들 중 호흡이 가장 길었다.
구현의 거의 모든 부분에서 어려웠는데, 특히 다리의 방향이 중간에 바뀌면 안되기 때문에 다리의 방향을 가로 또는 세로로만 움직이게 만드는 것이 어려웠다.
2차원 dfs,bfs에 어느정도 익숙해졌다고 생각했는데 아닌 것같다ㅠㅠ
# 17822 : 원판돌리기
### code
```c++
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
  ```
## 결과
아직 푸는 중..
## 접근
문제의 순서를 그대로 따라가면서 풀이 중입니다.
2차원 배열에 원판의 숫자를 저장하고 원판의 회전에 따라 배열값을 갱신해준 후,
인접하면서 같은 수가 있는지 탐색할 예정입니다.
## 문제 회고
이번 주 문제들 중 그나마 풀 수 있을 것같다는 자신감을 준 문제이다..ㅎㅎ
제출기한은 넘겼지만, 끝까지 풀어보겠습니다..!ㅠㅠ