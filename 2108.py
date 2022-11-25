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
#정렬이 전제되어 있어야함
num_s = Counter(num_list).most_common()
if len(num_s) > 1:  #만약에 최빈값이 여러개 이상인 경우 most_common()안에 itterable 수는 1부터 시작
    if(num_s[0][1] == num_s[1][1]): #만약 두개의 최빈값이 있다며 두번째로 작은 값 출력 ex) 0 0 1 1 -> 1출력
        print(num_s[1][0])
    else:
        print(num_s[0][0])  #같지 않다면 즉 압도적으로 많이 나오는 최빈값이 있다면 그 값 출력 ex)1 1 1 0 0 -> 1출력
else:
    print(num_s[0][0])  #최빈값이 하나만 존재한다면 하나 출력 ex) 1 1 1 2 3 4 -> 1출력



#4번째 줄 출력
print(num_list[-1]-num_list[0])