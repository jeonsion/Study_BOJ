#통계학
#N은 홀수이다.
# 산술평균 : N개의 수들의 합을 N으로 나눈 값
# 중앙값 : N개의 수들을 증가하는 순서로 나열했을 경우 그 중앙에 위치하는 값
# 최빈값 : N개의 수들 중 가장 많이 나타나는 값
# 범위 : N개의 수들 중 최댓값과 최솟값의 차이

import sys
from collections import Counter
input = sys.stdin.readline


N =int(input())
num_list = []
for i in range(N):
    num_list.append(int(input()))
num_list.sort()

#1번째 줄 출력
print(int(round(sum(num_list)/N, 0)))
#2번째 줄 출력
print(num_list[len(num_list)//2])
#3번째 줄 출력  Counter 라이브러리를 이용한 개수 체크
num_s = Counter(num_list).most_common()
if len(num_s) > 1:
    if(num_s[0][1] == num_s[1][1]):
        print(num_s[1][0])
    else:
        print(num_s[0][0])
else:
    print(num_s[0][0])



#4번째 줄 출력
print(num_list[-1]-num_list[0])