# 11779 : 최소비용구하기2
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
#define _CRT_SECURE_NO_WARNING
#define FIO cin.tie(0); cout.tie(0); ios::sync_with_stdio(0);
using namespace std;
const int INF = 1e9;

int n, m, s, e;
priority_queue<pair<int, int>, vector<pair<int, int>>, greater<pair<int, int>> >pq; //최소힙
vector <int> dist(1001, INF);
vector<pair<int, int>> node[1001];
int arr[1001];

void dijkstra() {
	pq.push(make_pair(0, s));
	dist[s] = 0;

	while (!pq.empty()) {
		int cost = pq.top().first;
		int here = pq.top().second;
		pq.pop();

		if (dist[here] < cost) continue;
		for (int i = 0; i < node[here].size(); i++) {
			int next = node[here][i].first;
			int nextcost = node[here][i].second;

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
		node[a].push_back(make_pair(b, c));
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
  ```
## 결과
성공

## 접근
버스의 개수가 10,000개가 넘어가기 때문에 우선순위 큐를 이용하여 시간복잡도가 개선된 다익스트라 알고리즘을 사용해야한다고 생각하였다.
항상 가장 비용이 적은 노드를 선택해야 하기때문에 최소힙을 사용하였다.

다익스크라 알고리즘을 통해 출발도시에서 도착도시까지의 최소 거리를 구하고,
그 과정에서 거쳐가는 도시를 배열에 저장해주어 거쳐간 도시의 수와 순서를 출력하였다.
## 문제 회고
출발도시와 도착도시 사이의 최소거리를 구하는 과정은 다익스트라를 통해서 어렵지않게 구할 수 있었다. 오히려 지나간 도시의 개수와 순서를 출력하는 방법에 대한 고민이 더 길었다.

그리고 백준 '스페셜저지'의 뜻을 몰랐는데 예시의 답안 출력과 내가 제출한 코드의 도시 순서가 달랐지만 성공으로 뜬걸 보고 검색해보고 그 뜻을 알게 되었다.
* 스페셜져지 : 답이 여러 가지가 될 수 있어 그 모두를 답으로 채점하기 위한 특별한 채점 프로그램이 들어가 있다는 뜻

# 1956 : 운동
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

int v,e;
int arr[401][401];

void floyd(void) {
	for (int k = 1; k <= v; k++) {
		for (int i = 1; i <= v; i++) {
			for (int j = 1; j <= v; j++) {
				arr[i][j] = min(arr[i][j], arr[i][k] + arr[k][j]);
			}
		}
	}
}

int main() {
	FIO;

	cin >> v >> e;

	for (int i = 1; i <= v; i++) {
		for (int j = 1; j <= v; j++) {
			arr[i][j] = INF;
		}
	}

	for (int i = 0; i < e; i++) {
		int a, b, c;
		cin >> a >> b >> c;
		arr[a][b] = c;
	}

	floyd();

	int res = INF;
	for (int i = 1; i <= v; i++) {
		for (int j = 1; j <= v; j++) {
			if (arr[i][j] != INF && arr[j][i] != INF) {
				res = min(res, arr[i][j] + arr[j][i]);
			}
		}
	}
	if (res == INF) {
		res = -1;
	}
	cout << res;
}
  ```
## 결과
성공
## 접근
1. 플로이드-워셜을 이용하여 마을과 마을 사이 거리의 최솟값을 2차원배열에 갱신하여준다. 
2. 사이클을 돌아야하기 때문에 출발했던 마을로 다시 돌아오는 경우만 생각한다.
3. 사이클 중 가장 거리의 합이 작은 사이클을 출력한다.
## 문제 회고
공부한 직후에 풀어서 그런지 비교적 쉽게 풀었다.

그런데, 2차원 배열에 INF값을 채우는 함수로 fill함수 (```fill(&arr[0][0], &arr[400][400], INF);```)를 썼을 때는 틀리고, 위의 코드에서처럼 for문을 사용했을 때는 맞았다고 나온다... vs에서는 잘 돌아가는데... 뭐가 문제인지 모르겠다.
# 92341 : 주차요금계산
### code
```python
import math
def solution(fees, records):
    visited = [False for i in range(10000)]
    parkingTime = [0 for i in range(10000)]
    res = [0 for i in range(10000)]
    answer = []
    freeTime,freeFee,unitTime, unitFee = fees
    
    for i in range(len(records)):
        carnum = records[i][6:10]
        idx = int(carnum)

        if records[i][11:] == "IN":
            visited[idx] = True
            start_H = int(records[i][0:2])
            start_M = int(records[i][3:5])
            time = start_H * 60 + start_M
            res[idx] = time
        elif records[i][11:] == "OUT":
            visited[idx] = False
            end_H = int(records[i][0:2])
            end_M = int(records[i][3:5])
            time = end_H * 60 + end_M
            parkingTime[idx] += time - res[idx]
            
    endTime = 23 * 60 + 59
    for i in range(len(visited)):
        if visited[i] == True:
            visited[i] = False
            parkingTime[i] += endTime - res[i]
    
    for times in parkingTime:
        if times != 0:
            if times <= fees[0]:
                answer.append([parkingTime.index(times),fees[1]])
            else:
                fee = freeFee + math.ceil((times - freeTime)/unitTime) * unitFee
                answer.append([parkingTime.index(times),fee])
    sorted(answer)
    
    ans = [row[1] for row in answer]
    return ans

  ```
## 결과
성공
## 접근
차량의 입.출차 기록 순서를 따라서 입차하는 차량의 번호를 인덱스로 하여 입차시간을 저장해주었다. 그리고 그 차가 나갈 때 출차 시각과 입차 시각을 뺀 주차시간을 parkingTime 배열에 저장해주었다.
23시 59분까지 출차하지 않는 차량은 visited배열을 이용하여 처리해주었다. 
## 문제 회고
문제는 비교적 빠르게 풀었는데, int형 slicing 오류로 시간을 꽤 잡아먹었다. 프로그래머스는 어느 라인에서 오류가 발생했는지 알려주지않아서 오류를 찾는 과정이 꽤 어려운것같다ㅠ
# 92342 : 양궁대회
### code
```python
from itertools import combinations_with_replacement as cr

def solution(n, info):
    # 중복조합으로 모든 경우 탐색하면서 정답 갱신
    # 최대로 점수 차이가 클 때의 점수 분포 + 그 때의 점수 차이 값(max[-1])
    max = [-1] * 12
    for comb in cr(range(11), n):
        cur = [0] * 12
        # 점수별 화살 개수
        for c in comb:
            cur[10 - c] += 1
        
        # 점수 차이 계산
        for i in range(11):
            # 라이언 점수 획득
            if cur[i] > info[i]:
                cur[-1] += 10 - i
            # 어피치 점수 획득
            elif info[i] != 0:
                cur[-1] -= 10 - i
        
        # 라이언이 우승하지 못하는 경우
        if cur[-1] <= 0:
            continue
            
        # 기존의 점수 차이 최댓값을 갱신하는 경우
        if cur[::-1] > max[::-1]:
            max = cur

    return [-1] if max[-1] <= 0 else max[:-1]
  ```
## 결과
실패 (구글링)
## 접근
* 내 생각
1. 라이언이 화살을 쏘는 최적의 방법은 과녁판의 k점에 어피치가 맞춘 화살보다 1개 더 많이 맞춰 점수를 얻거나, 0발을 쏴서 화살을 아끼는 방법이다.
2. 라이언이 높은 점수를 얻을 수 있도록 10점부터 0점 순서로 화살을 맞춰가며 얻을 수 있는 점수를 비교한다.
3. 가장 큰 점수차이가 같은 경우, 낮은 점수의 과녁판에 화살을 맞춘 경우를 출력해준다.

* 구글링
1. 라이언이 쏠 수 있는 모든 경우의 수를 구한다.(중복조합)
2. 어피치의 info와 비교하여 라이언의 점수가 더 높은 경우 중,
가장 점수 차이가 크고, 낮은 점수의 과녁에 화살을 맞은 경우를 출력해준다. 
## 문제 회고
러프하게 아이디어까지 생각해봤는데, 어피치와 라이언 점수비교 구현을 하지 못했다ㅠㅠ 그래서 결국 구글링을 하였는데, 라이언이 쏠 수 있는 모든 경우의 수를 어피치의 점수판과 비교하는 방법을 찾았다.
시간초과가 나지않을까? 했는데 중복조합의 수가 생각보다 많지않았다.

때로는 복잡하게 생각하는 것보다 직관적이고 심플한 방법이 통할 수 도 있을 것 같다.