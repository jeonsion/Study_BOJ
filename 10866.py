#덱
from collections import deque
import sys
input = sys.stdin.readline
N = int(input())

A_list = []
Deque = deque()
for i in range(N):
    A_list.append(input().split())

for j in A_list:
    if(j[0]=='push_front'):
        Deque.appendleft(j[1])
    elif(j[0]=='push_back'):
        Deque.append(j[1])
    elif(j[0]=='pop_front'):
        if(len(Deque)==0):
            print(-1)
        else:
            print(Deque.popleft())
    elif(j[0]=='pop_back'):
        if(len(Deque)==0):
            print(-1)
        else:
            print(Deque.pop())
    elif(j[0]=='size'):
        print(len(Deque))
    elif(j[0]=='empty'):
        if(len(Deque)==0):
            print(1)
        else:
            print(0)
    elif(j[0]=='front'):
        if(len(Deque)==0):
            print(-1)
        else:
            print(Deque[0])
    elif(j[0]=='back'):
        if(len(Deque)==0):
            print(-1)
        else:
            print(Deque[-1])    