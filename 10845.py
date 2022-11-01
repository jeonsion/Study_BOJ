#큐
#출력해야하는 명령어가 주어질 때 마다 한 줄에 하나씩 출력


from collections import deque



import sys
input = sys.stdin.readline


N = int(input())
A_list = []
queue = deque()
for i in range(N):
    A_list.append(input().split())
    
for j in range(N):
    if(A_list[j][0] == 'push'):     #큐에 넣는 연산
        queue.append(A_list[j][1])
    elif (A_list[j][0] == 'front'): #큐아 가장 앞에있는 정수 출력
        if(len(queue)==0):
            print(-1)
        else:
            print(queue[0])
    elif (A_list[j][0]=='back'):  #큐의 가장 뒤에있는 정수 출력
        if(len(queue)==0):
            print(-1)
        else:
            print(queue[-1])
    elif(A_list[j][0] == 'size'):   #큐에 있는 정수 개수 출력
        print(len(queue))
    elif(A_list[j][0]=='empty'):    #큐가 비어있으면 1, 아니면 0 출력
        if(len(queue)==0):
            print(1)
        else:
            print(0)
    elif(A_list[j][0]=='pop'):      #큐에서 가장앞에있는 정수 출력, 비어있는 경우 -1 출력
        if(len(queue)==0):
            print(-1)
        else:
            print(queue.popleft())        
    
