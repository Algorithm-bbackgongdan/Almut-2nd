# BOJ_16234 : 인구이동
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
  ```
### 결과
성공 (구글링 참조)
### 접근
우선 인접한 나라에 각각 방문해야하기 때문에 2차원배열 BFS를 이용하여 2차원 배열 내에서 주어진 인구수 차이 L~R사이만큼 차이가 난다면 연합국으로 묶어주었습니다.

visited 배열을 이용하여 방문한 국가와 방문하지 않은 국가를 구분하였다.
2개 이상의 국가가 연합국으로 묶인다면, 각 나라의 인구수를 (연합국 총 인구수) / (연합국 수)로 재설정 해주었다.

while문 안에서 위의 과정을 연합국이 만들어지지않을 때까지 반복한 후 반복 횟수를 변수 day에 저장하여 인구 이동이 며칠동안 일어났는지 출력하였다.
## 문제 회고
처음 문제를 풀 때, 국가의 인구수를 (연합국 총 인구수) / (연합국 수)로 재설정해주는 과정을 BFS 함수 내에 넣어 문제를 풀었는데 인구이동 기간을 제대로 출력하지 못하였다.

그래서 구글링을 통해 이후 연합되는 나라들만 담는 vector를 만들어 while문 안에서 인구수를 재설정해주는 방법을 통해 문제를 풀 수 있었다.

 BFS 알고리즘을 사용하는 것과 더불어 문제의 조건에 맞는 구현이 요구되어 고민을 길게 하였다.

# BOJ_1744 : 수 묶기
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

	for (int i = 0; i < n-1; i += 2) {
		if (v[i + 1] > 1) {
			sum += v[i] * v[i + 1];
		}
		else if (0 < v[i+1] && v[i+1] <= 1) {
			sum += v[i + 1] + v[i];
		}
	}
	if (num_pl % 2 == 1) sum += v[num_pl-1];

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
  ```
### 결과
성공
### 접근
가장 큰 수를 만들기 위해 주어진 수열을 크기 순(양수는 내림차순, 음수는 오름차순)으로 정렬한다.
그리고 아래의 조건들을 구현한다.
1. 1이 아닌 양수는 무조건 묶는게 더 커진다. (큰 수끼리 묶는다.)
2. 음수는 음수끼리 묶는다.
3. 음수가 짝수개 있다면, 절대값이 큰 순서대로 묶는다. 
4. 음수가 홀수개(1개x) 있을 때, 0이 있다면 절대값이 가장 작은 음수와 묶는다.

## 문제 회고
천천히 조건들을 생각하여 하나하나 구현 했을 때 실패없이 성공하였다.
그렇다보니 코드가 길고 지저분한 느낌이 있다.

# 150370 : 개인정보 수집 유효기간
### code
```python
def solution(today, terms, privacies):
    answer = []
    dict = {}
    cnt = 0
    
    today_spilt = today.split(".")
    year = int(today_spilt[0])
    month = int(today_spilt[1])
    day = int(today_spilt[2])
    totalDay = year*12*28 + month*28 + day
    
    for i in terms:
        type,month = i.split(" ")
        dict[type] = month
    
    for j in privacies:
        privacies_spilt = j.split(" ")
        privacies_date = privacies_spilt[0]
        privacies_type = privacies_spilt[1]
        privacies_date_spilt = privacies_date.split(".")
        p_year = int(privacies_date_spilt[0])
        p_month = int(privacies_date_spilt[1])
        p_day = int(privacies_date_spilt[2])
        p_totalDay = p_year*12*28 + p_month*28 + p_day + int(dict[privacies_type]) * 28
        cnt += 1
        if totalDay >= p_totalDay:
            answer.append(cnt)
    return answer

  ```
### 결과
성공
### 접근
(오늘 날짜까지의 일수)와 (개인정보 수집날짜의 일수 + 유효기간 일수)를 비교하여 오늘 날짜까지의 일수가 더 크다면 약관의 유효기간이 지났음을 의미하기 때문에 개인정보를 파기하여야 한다.
주어진 날짜를 "." 기준으로 잘라 일수를 계산하고, terms와 privacies를 " " 기준으로 잘라 각각 딕셔너리로 만들고 약관 유형을 추출하였다. 
## 문제 회고
처음에 c++로 해결하고자 하였으나 c++에서 문자열 자르기가 복잡하여 split함수가 있는 파이썬으로 해결하였다. 코드 구현에 있어서 파이썬이 정말 편한 언어임을 다시 한번 깨달았다.

# 150367 : 표현 가능한 이진트리
### code
```c++

  ```
### 결과
실패
### 접근
주어진 10진수의 숫자를 2진수로 변환하고, 최소한의 포화 이진트리 노드 개수가 될 때까지 2진수의 왼쪽에 0을 추가한다.(수 변화x)

이진 트리의 루트노드에 해당하는 2진수 문자열의 중앙값이 1이면 이진트리로 표현 가능. 

2진수 문자열의 중앙값이 0일 때, 좌우의 숫자 중 1개라도 1이라면 이진 트리로 표현 불가능. (루트노드가 없는데 자식노드가 있을 수는 없기 때문)

위의 아이디어를 반복하여 문제를 해결 할 수 있다.
## 문제 회고
접근에서와 같은 아이디어를 떠올렸지만, 포화이진트리의 노드개수만큼 0을 추가하고, 반복하여 2진수를 확인하는 코드구현에 실패하였다.
구글링을 통해 다시 공부해야겠다.