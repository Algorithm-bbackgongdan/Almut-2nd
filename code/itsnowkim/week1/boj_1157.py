# boj 1157 단어공부
# ord(), chr() function 기억해두기
# strip() 개행문자 제거

import sys

word = sys.stdin.readline().strip()
alpha = [0 for _ in range(26)]

for i in word:
    index = ord(i) - ord('A')
    if 'a' <= i <= 'z':
        index -= 32
    alpha[index] +=1

max = 0
for num in alpha:
    if num > max:
        max = num
        flag = 0
    elif num == max:
        flag = 1

if flag == 1:
    print('?')
else:
    print(chr(alpha.index(max) + ord('A')))
