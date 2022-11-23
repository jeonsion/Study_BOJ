#프린터 큐
#아이디어 : 가장 앞에 있는 원소 head가 큐에서 최대값이 아닐 때 큐의 맨 뒤로 넘겨준다. ->M의 값 -1



from collections import deque
#문서의 개수 : N, 큐에서 몇번째에 놓여있는지 위치 : M , M은 0보다 크거나 같고 N보다 작거나 같다!!!!
C = int(input())


#문서들의 중요도를 넣을 큐 생성


for i in range(C):
    N, M = map(int, input().split())
    importance_list = list(map(int, input().split()))
    queue = deque(importance_list)
    count =0
    while(range(1)):
        if(M==0 and max(queue)==queue[0]):
            count+=1
            break
        
        #큐의 맨앞에 값이 최대값보다 작을 때
        if max(queue)>queue[0]:
            if(M == 0):
                #print(queue, "1. M의 값은 : ", M, "count값 : ", count)
                a = queue.popleft()
                queue.append(a)  #큐의 맨 앞을 빼서 뒤에 추가
                M=len(queue)-1    #M의 위치 감소 
            else:
                #print(queue, "2. M의 값은 : ", M, "count값 : ", count)
                a = queue.popleft()
                queue.append(a)  #큐의 맨 앞을 빼서 뒤에 추가
                M-=1    #M의 위치 감소         
        elif max(queue) == queue[0]:    #큐의 최대값이 맨앞에 와있을 때 하지만 M이 아닐 때
            #print(queue, "3. 번째 if 문", "M의 값 : ",M)
            queue.popleft()
            count+=1
            M-=1
            #print(queue, "4.M의 값은 : ", M, "count값 : ", count)
    print(count)
