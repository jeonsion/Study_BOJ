#수 정렬하게3 아주 나이스한 문제 접근을 다르게함
import sys
input = sys.stdin.readline
n = int(input())
num = [0]*10001

for i in range(n):
    num[int(input())] +=1 
for i in range(1,10001):    #range(n)-->>range(1, 10001)로 변경하였을 때 통과 
    if(num[i]!=0):
        for j in range(num[i]):
            print(i)