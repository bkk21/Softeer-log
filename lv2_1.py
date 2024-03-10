# 이번에는 Indirect Indexing으로, 다음과 같은 방식을 따른다.
# 1. N개의 문자열 쌍 (S1,T1), (S2,T2),…, (SN,TN)이 주어진다. 각 쌍에 대해, Si의 길이와 Ti의 길이는 같다.
# 2.  Si에서 글자 x 또는 X가 등장하는 위치를 Pi라고 하자. 이 위치는 항상 유일하다.
# 3. 이때, Ti의 Pi번째 글자를 읽으면 된다. 단, 소문자는 대문자로 바꿔야 한다.
# 4. 예를 들어, Si가 Indexing이고 Ti가 Indirect라면 읽게 되는 글자는 R이 된다.

import sys

num = int(input())


S = list(range(num))
T = list(range(num))

for i in range(num):
    S[i], T[i] = input().split() #받아서 바로 분리

for i in range(num):
    for j in range(len(S[i])):
            if S[i][j] == 'x' or S[i][j] == 'X':
                if T[i][j].isalpha() == True:
                    print(T[i][j].upper(), end = '') #대문자로 변경
                else:
                    print(T[i][j], end = '')
