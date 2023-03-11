# 2212 : 센서
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
  ```
### 결과
성공
### 접근
멀리 떨어진 센서를 같은 집중국으로 묶었을 경우 수신가능영역이
멀어지기 때문에 최대한 가까이 위치한 센서끼리 묶어주어야한다.

위의 생각을 바탕으로 가장 인접한 두 센서 사이의 거리를 측정하여
가장 멀리 떨어져있는 센서 두 개는 다른 집중국에 묶이는 것으로 처리

집중국의 개수가 3개 이상일 때는 위의 처리과정을 거리가 먼 순서대로 진행되는 것으로 생각하였다. 
## 문제 회고
처음 문제를 읽었을 때, 수신가능영역을 특정 집중국에 속한 센서 중 가장 멀리 떨어져 있는 센서까지의 거리로 생각해서 문제를 잘 못 이해 했다. 하지만 예제의 출력 예시를 보고 특정 집중국에 속한 센서들과 집중국 사이 거리의 합이 최소가 되게 만드는 것임을 알고 문제를 풀어나갈 수 있었다. 

그리디 문제를 풀때는 항상 완전탐색방식이 가장 먼저 떠오른다. 1차원적이고 직관적이지만 시간복잡도 측면에서 굉장히 비효율적이라 시간초과가 나기 쉽다. 이번 문제 또한 처음에는 집중국 개수대로 센서들을 하나하나 묶어가며 최솟값을 찾는 방법이 먼저 떠올랐지만,
무조건 시간초과가 났을 것이다.
그래서 그리디문제는 효율적인 기준을 잡는 것이 중요한 것같다.

## 반성합니다.
개강 이후 생활이 바빠졌다는 핑계로 이번주 스터디에 많은 시간을 투자하지 못했습니다. 열심히 하자는 스터디 분위기에 안좋은 영향을 줄 수 도 있겠다는 생각에 마음이 무겁습니다..
다음 주는 좀 더 열심히 달려보겠습니다. 죄송합니다..! 
