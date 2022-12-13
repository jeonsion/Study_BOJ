#피보나치 함수
#이 주어졌을때 0과 1이 각각 몇번 출력되는지 구하는 프로그램

import sys
input = sys.stdin.readline
def fib(n):
    result = [[0,0] for i in range(41)]
    result[0][0] = 1
    result[1][1] = 1
    for i in range(2, n+1):
        result[i][0] = result[i-2][0] + result[i-1][0]
        result[i][1] = result[i-2][1] + result[i-1][1]
    return result[n]



for i in range(int(input())):
    n = int(input())
    print(fib(n)[0], fib(n)[1])