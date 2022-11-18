
import sys
input = sys.stdin.readline

#노드 개수 : N, 엣지 개수 : M, 탐색 시작노드 : V
N, M, V = map(int, input().split())

#노드 개수만큼 노드 리스트를 생성해준다, N+1까지 생성해서 1부터 N까지 접근할 수 있도록 고려(인접배열 개념)
Node_list = [[] for i in range(N+1)]

for i in range(M):
    #두 정점의 정보
    s, e = map(int, input().split())
    Node_list[s].append(e)
    Node_list[e].append(s)
    Node_list[s].sort()
    Node_list[e].sort()

#print("Node_list : ", Node_list)

#BFS함수    (잠재적으로 큐 이용)
def BFS(s):
    from collections import deque
    
    #visited 배열 0으로 초기화
    visited = [0 for i in range(N+1)]
    visited[s] = 1  #첫번째 노드 방문
    print(s, end = ' ') #방문한 노드출력
    queue = deque([])   #큐 생성
    queue.append(s)     #큐에 방문한 노드 push
    
    while(len(queue)!=0):   #큐가 not empty라면 반복문 실행
        u = queue.popleft() #큐에서 pop한 값을 u라고 선언
        for i in Node_list[u]:  #u주변노드들을 큐에 넣는다
            if(visited[i] == 0):    #방문한 노드가 아니라면
                visited[i] = 1  #방문했다고 표시
                print(i, end = ' ') #방문한 노드 출력
                queue.append(i) #방문한 노드 큐에 push
                



#깊이 우선 탐색 (잠재적으로 스택 이용), 재귀함수 이용
def DFS(s):
    #첫번쨰 노드 방문
    visited[s] = 1
    print(s, end = ' ') #방문한 노드 출력
    for i in range(len(Node_list[s])):  #방문한 노드 주변 노드 탐색
        x = Node_list[s][i] #인근 노드에 접근
        if(visited[x] == 0):    #방문하지 않은 노드라면 그 노드자리에서 DFS
            DFS(x)  #깊이 우선 탐색
    
    
    

visited = [0 for i in range(N+1)]
DFS(V)
print()
BFS(V)