# 기타 레슨
import sys

N, M = map(int, sys.stdin.readline().split(' '))
arr = list(map(int, sys.stdin.readline().split(' ')))
arr.sort(reverse=True)
print(N, M)
print(arr)