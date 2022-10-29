#요세푸스 문제


#큐 라이브러리 import
from collections import deque



queue = deque()

#N = 7, K = 3
N, K = map(int, input().split())

A_list = [i for i in range(1,N+1)]  #[1,2,3,4,5,6,7]



# K번째 위치 사람 제거, N은 1부터 시작하기 때문에 K-1 할당
Del = K-1
while(len(A_list)!= 0):
    
    #원형 큐에서 해당 위치 삭제하는 방법 
    Del = Del % len(A_list)
    #삭제할 요소
    pop_index = A_list.pop(Del)
    queue.append(pop_index )
    #삭제했으면 원소의 K번째 사실은 K-1번째로 실행되는 로직 필자의 코드는 N이 0부터 시작하기 때문!
    Del += K-1
    
print("<", end = '')
print(*queue, sep = ", ", end = '')
print(">")


