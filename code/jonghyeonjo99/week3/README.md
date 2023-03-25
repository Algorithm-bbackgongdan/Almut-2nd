# 2343 : 기타 레슨
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
				temp = lec[i];
				cnt++;
			}
      //마지막에 블루레이에 저장되는 기타강의의 길이가 블루레이의 크기보다 작을 때
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
  ```
## 결과
성공
## 접근
기타강의의 길이는 순서가 정해져있기 때문에 크기 순으로 정렬을 할 수 없다. 따라서
블루레이 크기를 이분탐색하는 방법으로 문제를 풀어보았다.

가능한 가장 작은 블루레이의 크기는 하나의 가장 긴 기타 강의의 길이가 되어야한다.
그래야 각각의 강의를 블루레이 하나에 넣을 수 있기 때문이다.
가장 큰 블루레이의 크기는 모든 기타강의의 길이를 더한 값이다.

그래서 left값은 가장 길이가 긴 기타 강의의 길이로, right값은 기타강의의 길이를 모두 더한 total값으로 초기화해주었다.

이후 while문 안에서 기타강의 순서대로 강의를 더해주다가 mid값을 넘어가면 가장 최근에 더해주었던 기타강의를 빼주고, 블루레이 개수를 1 더해주었다.
그렇게 만들어진 블루레이 개수(cnt)에 따라서 left와 right값을 갱신해주면서 이분탐색을 진행한다.

가능한 블루레이 중 가장 크기가 작은 블루레이를 찾아야하기 때문에 마지막 이분탐색 결과 나온 left값이 최소 크기의 블루레이가 될 것이다.
## 문제 회고
처음에 기타 레슨 강의를 기준으로 나눌려고 했는데, 강의 순서가 정해져 있어 크기 순 정렬이 불가능하여 많이 헤맸다. 나중에서야 블루레이 크기를 기준으로 이분탐색함을 생각할 수 있었다. 이분탐색은 탐색의 기준을 정하는 것이 제일 중요한 것 같다.

```c++
int a = v.size() - 1;
	cout << v[a];
  ```
처음에 vector를 사용하여 vector의 size()를 통해 블루레이의 개수를 찾아 문제를 해결할려고 했는데 out of Bounds 에러가 발생하였다. 에러를 수정하고자 알아봤을 때, c++에서 vector의 최대 크기가 10억이라는 사실을 알 수 있었다.

 문제에서 주어진 범위가 각 강의의 수(100000)와 강의의 길이(10000)를 곱하였을 때,10억이 되어 vector의 최대크기를 초과했던 것으로 생각된다.
 이후, vector를 사용하지 않고 변수 cnt를 사용하여 문제를 해결할 수 있었다.

 # 2240 : 자두나무
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
typedef long long ll;
using namespace std;
const int INF = 1e9;


int t, w, ans = 0;
int dropOrder[1001];
int dp[3][31][1001];
// dp[현재위치][남은움직임횟수][현재시간] = 현재 가진 최대 자두 개수

int main() {
    FIO;
	cin >> t >> w;
	for (int i = 1; i <= t; i++) {
		cin >> dropOrder[i];
	}
	memset(dp, -1, sizeof(dp));

	dp[1][w][0] = 0;

	for (int time = 0; time < t; time++) {
		for (int cnt = 0; cnt <= w; cnt++) {
			for (int pos = 1; pos <= 2; pos++) {
				if (dp[pos][cnt][time] >= 0) {
					int nextPos = dropOrder[time + 1];

					if (pos == nextPos) {	// 현재 위치에 자두가 떨어짐
						dp[pos][cnt][time + 1] = dp[pos][cnt][time] + 1;
					}
					else {		// 현재 위치에 자두가 떨어지지 않음
						if (cnt != 0) {	// 움직여서 자두를 줍는 경우
							dp[nextPos][cnt - 1][time + 1] = max(dp[nextPos][cnt - 1][time + 1], dp[pos][cnt][time] + 1);
						}				// 움직이지 않는 경우
						dp[pos][cnt][time + 1] = dp[pos][cnt][time];
					}
				};
			}
		}
	}
	// w를 모두 소모해서 더이상 움직이지 못하는 경우와 시간이 t인 경우를 모두 비교
	int ret = 0;
	for (int pos = 1; pos <= 2; pos++) {
		for (int time = 1; time <= t; time++) {
			ret = max(ret, dp[pos][0][time]);
		}
		for (int i = 0; i <= w; i++) {
			ret = max(ret, dp[pos][i][t]);
		}
	}
	cout << ret;
	return 0;
}
  ```
## 결과
실패 후 구글링
## 접근
자두가 자두를 받기 위해 행동할 수 있는 경우의 수는

1. 현재위치에 자두가 떨어질 때 자두를 받는다.
2. 다른 위치에 자두가 떨어질 때 자리를 바꿔 자두를 받거나, 자리를 바꾸지 않고 다음 자두를 받는다.

로 구분할 수 있다. 현재상태를 나타낼 수 있는 변수는 현재 위치, 남은 이동횟수(w),현재시간(t)가 있다. 위의 변수를 수식으로 표현하면 dp[현재위치][남은 이동횟수][현재시간] = value 로 나타낼 수 있다.

수식을 통해 점화식을 구해보자
1. 자두 받음 : dp[pos][cnt][time+1] = dp[pos][cnt][time] +1
2. * 자리 바꿈 : dp[nextPos][cnt-1][time+1] = max(dp[nextPos][cnt-1][time+1], dp[pos][cnt][time+1] + 1)
	* 자리 안바꿈 :  dp[pos][cnt][time+1] = dp[pos][cnt][time]

점화식을 수행하고 최댓값을 출력한다.
## 문제 회고
다른 유형도 물론 어렵지만, 개인적으로 DP 문제가 매우 까다롭게 느껴진다.
변수를 설정하고 경우의 수까지 생각하였지만, 그 생각을 수식과 점화식으로 표현하는 과정이 어렵다. 지난 학기에 dp를 공부할 때 느꼈던 점을 다시한번 느끼면서 공부의 필요성을 깨닫고 갑니다..

# 1234 : 미로 탈출 명렁어
### code
```python
def solution(n, m, x, y, r, c, k):
    global answer
    answer = ''
    dist = abs(x-r) + abs(y-c)
    if(k < dist or (k + dist) % 2 == 1): return 'impossible'
    if (k == dist):
        if(x < r):
            for i in range(r-x):
                answer += 'd'
            if(y < c):
                for i in range(c-y):
                    answer += 'r'
            else:
                for i in range(y-c):
                    answer += 'l'
        else:
            if(y < c):
                for i in range(c-y):
                    answer += 'r'
                for j in range(x-r):
                    answer += 'u'
            else:
                for i in range(y-c):
                    answer += 'l'
                for j in range(x-r):
                    answer += 'u'
    if(k > dist):
        if(x < r):
            m = k - (r-x)
            n = dist - (r-x)
            s = m/n
            for i in range(r-x):
                answer += 'd'
            if(y < c):
                if(m % 2 == 1):
                    for i in range(s):
                        answer += 'rl'
                    for j in range(m - (2*s)):
                        answer += 'r'
                else:
                    for i in range(s-1):
                        answer += 'rl'
                    for j in range(m - 2*(s-1)):
                        answer += 'r'
            else:
                for i in range(n):
                    answer += 'l'
                for j in range((k-dist)//2):
                    answer += 'rl'
        else:
            if (y < c):
                for i in range (c-y):
                    answer += 'r'
                for j in range ((k-(c-y)-(x-r))//2):
                    answer += 'l'
                for i in range ((k-(c-y)-(x-r))//2):
                    answer += 'r'
                for j in range (x-r):
                    answer += 'u'
            else:
                for i in range(y-c):
                    answer += 'l'
                for i in range((k-(y-c)-(x-r))//2):
                    answer += 'rl'
                for i in range(x-r):
                    answer += 'u'       
    return answer

  ```
### 결과
실패
### 접근
출발지와 도착지 사이의 거리를 구하고 k가 그값보다 작다면 도착지에 갈 수 없기 때문에 impossible을 출력하고, k와 출발지와 도착지 사이 거리가 홀/짝 혹은 짝/홀로 수가 다르다면 k값만큼 이동하였을 때 도착지에 도착할 수 없기 때문에 impossible을 출력한다.

그리고 k와 출발지와 도착지 사이 거리가 같다면 최단거리로 이동하여 미로를 탈출할 수 있다.

k가 출발지와 도착지 사이 거리보다 크다면 사전순으로 가장 빠른 돌아가는 거리를 구한다.

## 문제 회고
정말 막연하게 사전 순으로 가장 빠르게 도달할 수 있는 경우의 수대로 answer에 이동을 추가하는 코드를 생각했다. impossible 케이스와 최단거리 케이스의 경우 테스트케이스를 통과하였지만, 당연히 코드를 제출하였을 때는 많은 케이스에서 런타임 에러와 실패가 있었다...

알고리즘을 전혀 생각하지 않았으니 당연한 결과..ㅎㅎ..
좀 더 고민해보고, 공부해야겠다😢

# 118667 : 두 큐 합 같게 만들기
### code
```python
from collections import deque

def solution(queue1, queue2):
    answer = 0
    n = len(queue1) + len(queue2)
    sum_q1 = sum(queue1)
    sum_q2 = sum(queue2)
    q1 = deque(queue1)
    q2 = deque(queue2)
    if ((sum_q1 + sum_q2) % 2 == 1):
        return -1
    while (1):
        if(answer >= 2*n):
            return -1
            break
        if(sum_q1 == sum_q2):
            break
        if(sum_q1 > sum_q2):
            temp1 = q1.popleft()
            q2.append(temp1)
            answer += 1
            sum_q1 -= temp1
            sum_q2 += temp1
        if(sum_q1 < sum_q2):
            temp2 = q2.popleft()
            q1.append(temp2)
            answer += 1
            sum_q1 += temp2
            sum_q2 -= temp2
    return answer

  ```
### 결과
성공 (개념 구글링)
### 접근
우선 두 큐의 합이 홀수이면 같아질 수 없기 때문에 -1을 return한다.
두 수의 합이 짝수 일 때, 듀 큐의 합을 비교해서 합이 더 큰 큐에서 배열의 첫번째 원소를 추출하여 다른 큐에 추가하여 준다. 위 과정을 반복하여 두 큐의 합이 같아졌을 때 answer값을 출력한다.
이 과정에서 answer값이 두 큐의 모든 원소를 추출하였다가 추가해주는 횟수 이상 넘어가면 두 큐의 합을 같게 만들 수 없다. 따라서 -1을 return해준다.
## 문제 회고
c++로 문제를 풀었을 때,
```c++
#include <string>
#include <vector>

using namespace std;

int solution(vector<int> queue1, vector<int> queue2) {
    int answer = -2;
    int sum_q1 = 0;
    int sum_q2 = 0;
    int cnt = 0;
    int n1 = queue1.size();
    int n2 = queue2.size();
    while(1) {
        for(int i =0; i < queue1.size(); i++) {
        sum_q1 += queue1[i];
        }
        for(int i =0; i < queue1.size(); i++) {
        sum_q2 += queue2[i];
        }
        if((sum_q1 + sum_q2) % 1 == 1) {
            return -1;
            break;
        }
        
        if (cnt >= (n1+n2)) {
            return -1;
            break;
        }
        
        if(sum_q1 > sum_q2) { 
            int temp1 = queue1.front();
            queue1.erase(queue1.begin());
            queue2.push_back(temp1);
            cnt++;
        }
        else if (sum_q1 < sum_q2) {
            int temp2 = queue2.front();
            queue2.erase(queue2.begin());
            queue1.push_back(temp2);
            cnt++;
        }
       else if (sum_q1 == sum_q2) {
           answer = cnt;
           return answer;
           break;
       }
    }
}
```
위의 코드에서 포인터 할당오류가 발생하여 이번에도 중간에 파이썬으로 언어를 바꿔 문제를 풀었다.(지금 c++코드를 보면 시간초과가 날 코드이다 ㅎㅎ;;)

c++코드에서도 볼 수 있듯이 파이썬에서도 처음에 while문 안에서 각 큐의 합을 구했다. 그리고 몇몇 케이스에서 시간초과가 발생하여 while문 밖에서 큐의 합을 구하는 방식으로 코드를 변경하였다.

그럼에도 불구하고 3~4개의 케이스에서 시간초과가 발생하여 list의 시간복잡도를 구글링하였다. 그 결과 list를 이용하여 자료구조 queue를 구현하면 O(n)의 시간복잡도를 가지지만, deque를 이용하면 O(1)의 시간복잡도를 갖는다는 것을 배울 수 있었다. 그리고 deque를 이용하여 연산을 해준 결과 통과할 수 있었다.

(참조 블로그 : https://codingpractices.tistory.com/entry/Python%ED%8C%8C%EC%9D%B4%EC%8D%AC-%EC%99%9C-%EB%A6%AC%EC%8A%A4%ED%8A%B8%EB%8C%80%EC%8B%A0-%ED%81%90-%EB%8D%B0%ED%81%AC-deque-%EB%A5%BC-%EC%93%B8%EA%B9%8C , https://velog.io/@sossont/Python-Queue-%EC%9E%90%EB%A3%8C%EA%B5%AC%EC%A1%B0-%EC%82%AC%EC%9A%A9%ED%95%98%EA%B8%B0)

항상 시작은 c++로 문제를 풀기 시작하지만 저번에는 구현의 편리성때문에, 이번에는 포인터 할당오류로 인해 파이썬으로 문제를 풀었다. 백준은 안그러는데 개인적으로 프로그래머스 문제는 파이썬으로 풀기 편하게 출제된다고 느껴졌다.