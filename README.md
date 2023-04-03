# 알고리즘 멋쟁이 2기

# 목표

- 기업 코딩테스트에 자주 출제되는 문제 유형을 빠르게 익히고 합격할 역량 기르기

# 진행 기간 및 내용

스터디의 텐션과 시험 기간을 고려하여 6주 분량의 시즌제를 생각했습니다.

아래 표의 내용 구성은 **_이것이 취업을 위한 코딩 테스트다_** 의 목차를 참고했습니다.

알고리즘 멋쟁이 1기에서 `chapter 08. 다이나믹 프로그래밍` 까지 공부했기 때문에 3주차까지 빠르게 복습할 생각입니다.

[이것이 취업을 위한 코딩 테스트다 with 파이썬 - YES24](http://www.yes24.com/Product/Goods/91433923)

| 주차 | 기간        | 내용                                                    |
| ---- | ----------- | ------------------------------------------------------- |
| 1    | 3/6 - 3/12  | 그리디, 구현 복습 + 백준 각 1문제, 프로그래머스 2문제   |
| 2    | 3/13 - 3/19 | DFS/BFS, 정렬 복습 + 백준 각 1문제, 프로그래머스 2문제  |
| 3    | 3/20 - 3/26 | 이분탐색, DP 공부 + 백준 2문제, 프로그래머스 2문제      |
| 4    | 3/27 - 4/2  | 최단경로 공부 + 최단경로 백준 2문제, 프로그래머스 2문제 |
| 5    | 4/3 - 4/9   | 그래프이론 + 그래프이론 백준 2문제, 프로그래머스 2문제  |
| 6    | 4/10 - 4/16 | 프로그래머스 3문제 (Lv 2 이상)                          |

# 진행 방식

- 매주 진행 내용(ex. 1주차 그리디, 구현)에 맞는 알고리즘 공부하기
  - 책을 참고해도 좋고 구글링을 해도 좋습니다.
  - 또는 어느정도 개념을 알고 있다면 문제를 먼저 풀고 난 이후에 모르는 부분을 공부해도 좋습니다.
  - 6주차는 pass
- 해당 주차 총무가 백준 + 프로그래머스 문제 출제
  - 총무는 매주 돌아가면서 바꿈
- 마감일까지 출제된 3~4문제 풀기 + [README.md](http://README.md) 작성 후 깃헙에 PR
  - README.md는 공부한 내용, 문제 풀이, 접근 방법 등 자유롭게 작성하시면 됩니다.
  - 문제를 못 풀었을 경우 꼭! 접근 방법에 대해 회고하여 적어주세요.
- 코드 리뷰 후 merge
- 총무가 벌금 계산 후 -> 다음 주차 총무가 README.md 업데이트 (문제 출제)

# 보증금

- 어느 정도의 강제성을 부여하기 위해 `(인원 수) * (주차 수) * 500` 원을 1 인당 보증금으로 생각하고 있습니다
  스터디 완주 시 보증금은 반환됩니다
  단, 해당 주차에 **“미션”** 실패 시, 보증금에서 `(인원 수) * 500` 원이 차감됩니다.
  ex) 스터디 인원 5명, 총 6주차 스터디인 경우
  1인당 보증금 : `5 * 6 * 500 = 15,000` 원
  미션 실패한 주 당 `5 * 500 = 2,500` 원 차감
- 스터디 종료 후, 차감으로 인해 남은 보증금 잔액은 `(보증금 잔액) / (인원 수)` 만큼 배분합니다.
- 스터디 중도 이탈 시, 보증금은 돌려받을 수 없습니다 🥲 ( 책임감! )

# 기타

- 문제풀이를 위한 언어 선택은 자유입니다.
- 코드리뷰의 편의를 위해 Readme에 풀이를 잘 작성해주세요!
- 문제를 못 풀었다면 어디까지 생각하고 접근했는지 Readme에 기록해주세요!
- 커리큘럼과 진행방식은 협의 가능합니다.
  - +) 개인적으로 알고리즘 공부는 빠르게 최소화 하고, 알고리즘 유형을 알 수 없는 실전 문제를 풀며 감각을 끌어올리는 훈련을 하고 싶어요.
- 출제 **난이도 기준**은 대략 아래와 같습니다.
  - 백준 : Silver 1,2 ~ gold 3,4 (평균 gold 5)
  - 프로그래머스 : Lv 2 ~ 4 (평균 Lv.3) (출처: 카카오 블라인드, 테크 인턴십 등)

# 진행 방식 상세

## 매 주 일정

### 0. 시작

- git clone 후 각자 github 아이디명으로 branch 파기

### 1. 월 ~ 토요일 자정

- 알고리즘 공부
- 출제된 문제 풀기
- [README.md](http://README.md) 작성
- 내 브랜치에 push
- 내 브랜치 → main으로 pull request

### 2. 일요일

- 사이클에 맞춰 해당 사람 코드 PR 리뷰
- 주차별 해당 사람 = (자신의 번호 + 해당 주차) % 인원수
- 예) 1주차-seungwookim99 : (seungwookim99(0) + 1) % n = 1 => 1번 사람 코드 PR

### 3. 월요일

- 총무가 벌금 계산
- 문제 출제 + [README.md](http://README.md) 커리큘럼에 업데이트

## 맴버 및 번호

[seungwookim99](https://github.com/seungwooKim99)(0) → [itsme-shawn](https://github.com/itsme-shawn)(1) → [itsnowkim](https://github.com/itsnowkim)(2) → [jonghyeonjo99](https://github.com/jonghyeonjo99)(3) → [asiloveyou](https://github.com/asiloveyou)(4) → [kauthenticity](https://github.com/kauthenticity)(5)

## 코드 리뷰 예시

1. 코드의 시간 복잡도
2. 코드의 개선 방안
3. 추천해줄 새로운 함수나 라이브러리
4. 그 외의 코멘트

## 폴더 구조

```
README.md
code
   ㄴ seungwookim99
     ㄴ week1
       ㄴ boj_1541.py
       ㄴ boj_1461.py
       ㄴ boj_2138.py   // 백준 문제
       ㄴ prog_12345.py // 프로그래머스 문제
       ㄴ README.md     // 1주차 README
```

# 멤버 별 제출 현황

- 총무가 PR 기준으로 월요일마다 업데이트 해주세요!
- ✅ : 미션 성공
- 😥 : 미션 실패 (지각, 미제출, 미흡)

| 멤버                                              | 1주차 | 2주차 | 3주차 | 4주차 | 5주차 | 6주차 |
| ------------------------------------------------- | ----- | ----- | ----- | ----- | ----- | ----- |
| [seungwookim99](https://github.com/seungwooKim99) | ✅    | ✅    |✅    |
| [itsme-shawn](https://github.com/itsme-shawn)     | ✅    | ✅    |✅    |
| [itsnowkim](https://github.com/itsnowkim)         | ✅    | ✅    |✅    |
| [jonghyeonjo99](https://github.com/jonghyeonjo99) | ✅    | ✅    |✅    |
| [asiloveyou](https://github.com/asiloveyou)       | ✅    | ✅    |✅    |
| [kauthenticity](https://github.com/kauthenticity) | ✅    | ✅    |✅    |

# 커리큘럼

- 총무가 월요일마다 업데이트 해주세요!

## Week 1

- 총무 : [seungwookim99](https://github.com/seungwooKim99)

### 1. 그리디

- 문제정보 : 센서(2212)
- 출처 : 백준
- 링크 : https://www.acmicpc.net/problem/2212

### 2. 구현

- 문제정보 : 감시(15683)
- 출처 : 백준
- 링크 : https://www.acmicpc.net/problem/15683

### 3. 실전문제 1

- 문제정보 : 택배 배달과 수거하기
- 출처 : 프로그래머스 (2023 KAKAO BLIND RECRUITMENT)
- 링크 : https://school.programmers.co.kr/learn/courses/30/lessons/150369

### 4. 실전문제 2

- 문제정보 : 이모티콘 할인행사
- 출처 : 프로그래머스 (2023 KAKAO BLIND RECRUITMENT)
- 링크 : https://school.programmers.co.kr/learn/courses/30/lessons/150368

## Week 2

- 총무 : [itsme-shawn](https://github.com/itsme-shawn)

### 1. BFS/DFS

- 문제정보 : 인구 이동(16234)
- 출처 : 백준
- 링크 : https://www.acmicpc.net/problem/16234

### 2. 정렬

- 문제정보 : 수 묶기(1744)
- 출처 : 백준
- 링크 : https://www.acmicpc.net/problem/1744

### 3. 실전문제 1

- 문제정보 : 개인정보 수집 유효기간
- 출처 : 프로그래머스 (2023 KAKAO BLIND RECRUITMENT)
- 링크 : https://school.programmers.co.kr/learn/courses/30/lessons/150370

### 4. 실전문제 2

- 문제정보 : 표현 가능한 이진트리
- 출처 : 프로그래머스 (2023 KAKAO BLIND RECRUITMENT)
- 링크 : https://school.programmers.co.kr/learn/courses/30/lessons/150367

## Week 3

- 총무 : [itsnowkim](https://github.com/itsnowkim)

### 1. 이분탐색

- 문제정보 : 기타 레슨(2343)
- 출처 : 백준
- 링크 : https://www.acmicpc.net/problem/2343

### 2. DP

- 문제정보 : 자두나무(2240)
- 출처 : 백준
- 링크 : https://www.acmicpc.net/problem/2240

### 3. 실전문제 1

- 문제정보 : 미로 탈출 명령어
- 출처 : 프로그래머스 (2023 KAKAO BLIND RECRUITMENT)
- 링크 : https://school.programmers.co.kr/learn/courses/30/lessons/150365

### 4. 실전문제 2

- 문제정보 : 두 큐 합 같게 만들기
- 출처 : 프로그래머스 (2022 KAKAO TECH INTERNSHIP)
- 링크 : https://school.programmers.co.kr/learn/courses/30/lessons/118667

## Week 4

- 총무 : [jonghyeonjo99](https://github.com/jonghyeonjo99)

### 1. 최단거리 (다익스트라)

- 문제정보 : 최소비용 구하기2 (11779)
- 출처 : 백준
- 링크 : https://www.acmicpc.net/problem/11779

### 2. 최단거리 (플로이드-워셜)

- 문제정보 : 운동 (1956)
- 출처 : 백준
- 링크 : https://www.acmicpc.net/problem/1956

### 3. 실전문제 1

- 문제정보 : 주차 요금 계산 (92341)
- 출처 : 프로그래머스 (2022 KAKAO BLIND RECRUITMENT)
- 링크 : https://school.programmers.co.kr/learn/courses/30/lessons/92341

### 4. 실전문제 2

- 문제정보 : 양궁대회 (92342)
- 출처 : 프로그래머스 (2022 KAKAO BLIND RECRUITMENT)
- 링크 : https://school.programmers.co.kr/learn/courses/30/lessons/92342
