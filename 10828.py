#스택
import sys
input = sys.stdin.readline

N = int(input())
A_list = []

stack = []
for i in range(N):
    A_list.append(input().split())

for j in A_list:
    if(j[0]=='push'):
        stack.append(j[1])
    elif(j[0]=='top'):
        if(len(stack)==0):
            print(-1)
        else:
            print(stack[-1])
    elif(j[0]=='size'):
        print(len(stack))
    elif(j[0]=='empty'):
        if(len(stack)==0):
            print(1)
        else:
            print(0)
    elif(j[0] == 'pop'):
        if(len(stack)==0):
            print(-1)
        else:
            print(stack.pop())