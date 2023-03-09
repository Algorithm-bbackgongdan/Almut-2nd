# 15683 - 감시
"""
1 : 한 방향
2 : 좌우 / 상하
3 : 직각으로 네 방향 가능
4 : 세 방향
5 : 모든 방향
6 : 벽
"""
import sys
import copy

N, M = map(int, sys.stdin.readline().split())
arr = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

ans = N * M

# cctv 위치 저장
# cctv = {1:[],2:[],3:[],4:[],5:[]}
cctv = {}

for i in range(N):
    for j in range(M):
        if 0 < arr[i][j] < 6:
            if arr[i][j] in cctv:
                cctv[arr[i][j]].append((i,j))
            else:
                cctv[arr[i][j]] = [(i,j)]
        elif arr[i][j] == 6:
            ans -= 1

# check
temp = copy.deepcopy(arr)

