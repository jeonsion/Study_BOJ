import sys
input = sys.stdin.readline

n, k = map(int, input().split())
calc_n = 1
calc_k = 1
for i in range(k):
    calc_n*=(n-i)
    
for j in range(k):
    calc_k*=(k-j)
    
print(int(calc_n/calc_k))