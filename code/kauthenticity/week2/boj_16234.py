import sys
from collections import deque

n, l, r = map(int, input().split())
countries = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

DIRECTIONS = [(1, 0), (0, 1), (-1, 0), (0, -1)]
COUNTRIES_ALL = n * n


def checkBoundary(x, y):
    if x < 0 or x >= n or y < 0 or y >= n:
        return False
    return True


def openBoundary(x, y, visited):
    queue = deque([])  # bfs를 위한 "국경이 열린 나라" 큐
    openedCountries = []  # 국경이 열린 나라를 전부 저장
    populationSum = 0  # 국경이 열린 나라들의 인구 합

    queue.append((x, y))
    openedCountries.append((x, y))

    visited[x][y] = True
    populationSum += countries[x][y]

    while queue:
        curX, curY = queue.popleft()
        curPopulation = countries[curX][curY]

        for dirX, dirY in DIRECTIONS:
            newX = curX + dirX
            newY = curY + dirY

            if checkBoundary(newX, newY) and not visited[newX][newY]:
                newPopulation = countries[newX][newY]
                populationDiff = abs(curPopulation - newPopulation)

                if l <= populationDiff <= r:
                    queue.append((newX, newY))
                    openedCountries.append((newX, newY))

                    visited[newX][newY] = True
                    populationSum += countries[newX][newY]

    return openedCountries, populationSum


def proceedDay():
    visited = [[False for _ in range(n)] for _ in range(n)]
    closedCountries = 0

    for i in range(n):
        for j in range(n):
            # 이미 이전에 인구 이동이 일어난 경우
            if visited[i][j]:
                continue

            openedCountries, populationSum = openBoundary(i, j, visited)

            # 국경을 연 경우
            if len(openedCountries) > 1:
                populationAvg = int(populationSum / len(openedCountries))

                for x, y in openedCountries:
                    countries[x][y] = populationAvg
            # 국경을 열지 않은 경우
            else:
                closedCountries += 1

    return closedCountries == COUNTRIES_ALL


def solution():
    done = False
    day = -1

    while not done:
        done = proceedDay()
        day += 1

    return day


print(solution())
