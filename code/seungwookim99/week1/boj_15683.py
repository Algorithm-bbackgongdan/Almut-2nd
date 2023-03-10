import sys
import copy
from itertools import product

DIR = {'E': (0, 1), 'S': (1, 0), 'W': (0, -1), 'N': (-1, 0)} # 동서남북
CCTV = [ # CCTV별 탐색 방향 정의
  [], 
  [('E'), ('S'), ('W'), ('N')], # 1번 cctv 
  [('E', 'W'), ('S', 'N')], # 2번 cctv
  [('E', 'S'), ('S', 'W'), ('W', 'N'), ('N', 'E')], # 3번 cctv
  [('E', 'S', 'W'), ('S', 'W', 'N'), ('W', 'N', 'E'), ('N', 'E', 'S')], # 4번 cctv
  [('E', 'S', 'W', 'N')] # 5번 cctv
]

def pickCCTVsDirections(cctvs):
    # CCTV들이 감시할 수 있는 방향들의 모든 경우의 수 (최대 4^8)
    res = []
    for (y, x, num) in cctvs:
        res.append(CCTV[num])
    return list(product(*res))


def out_of_range(y, x):
    # office 범위 벗어나는지 test
    return y < 0 or y >= n or x < 0 or x >= m


def calcMarkedPoints(office_):
    # '#'개수 계산 (cctv의 감시 구역 수)
    res = 0
    for i in range(n):
        for j in range(m):
            if office_[i][j] == '#':
                res += 1
    return res


def mark(y, x, dirs, office_):
    # dirs 정보에 맞게 cctv 감시 처리 ('#' 표시)
    for char in dirs:
        ny, nx = y, x
        dy, dx = DIR[char]
        while not out_of_range(ny + dy, nx + dx):
            ny += dy
            nx += dx
            if office_[ny][nx] == 0:
                office_[ny][nx] = '#'
            elif office_[ny][nx] == 6: # 벽을 만나면 너머로 감시 불가
                break

    return office_


def calcCoverSpots(cctvDir):
    # cctvDir 정보에 담긴 cctv들이 감시할 수 있는 영역 계산
    # (cctvDir는 각 cctv들이 탐색할 방향들에 대한 정보가 정의되어 있음)
    office_ = copy.deepcopy(office) # 원본 복사
    for idx, (y, x, num) in enumerate(cctvs):
        # idx 번째로 담긴 cctv의 방향 가져오기 (from cctvDir)
        dirs = cctvDir[idx]

        # office_ 에 # 마킹
        office_ = mark(y, x, dirs, office_)

    return calcMarkedPoints(office_)


n, m = map(int, sys.stdin.readline().rstrip().split(' '))
office = [list(map(int,sys.stdin.readline().rstrip().split(' '))) for _ in range(n)]

# cctv 위치 / 사각지대 개수 저장
blindSpotsNum = 0
cctvs = []
for i in range(n):
    for j in range(m):
        if 0 < office[i][j] < 6:
            cctvs.append((i, j, office[i][j]))  # (y, x, cctv번호)
        elif office[i][j] == 0:
            blindSpotsNum += 1

candidate = []
for cctvDirs in pickCCTVsDirections(cctvs):
    candidate.append(blindSpotsNum - calcCoverSpots(cctvDirs))

print(min(candidate))