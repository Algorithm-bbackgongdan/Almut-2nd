n ,m = map(int, input().split())

array = []
for i in range(n):
    array.append(int(input()))

# dp 테이블 초기화
d = [10001] * (m + 1)
# dp 진행
d[0] = 0
for i in range(n):
    for j in range(array[i], m+1):
        # array[i] = 화폐 단위
        d[j] = min(d[j], d[j-array[i]] + 1)

# 계산된 결과 출력
if d[m] == 10001:
    print(-1)
else:
    print(d[m])