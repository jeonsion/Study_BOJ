#동전 0
import sys
input = sys.stdin.readline
N, K = map(int, input().split())
count = 0
cash_list = [int(input()) for i in range(N)]
cash_list.reverse()

#그리디 알고리즘 : 각 케이스에 최선의 경우
i = 0
while(K != 0 ):
    if K - cash_list[i] >= 0:   
        K = K-cash_list[i]
        count+=1
    else:
        i+=1
print(count)