# 그래프를 DFS로 탐색한 결과와 BFS로 탐색한 결과를 출력하는 프로그램을 작성하시오.
# 단, 방문할 수 있는 정점이 여러 개인 경우에는 정점 번호가 작은 것을 먼저 방문하고, 
# 더 이상 방문할 수 있는 점이 없는 경우 종료한다. 정점 번호는 1번부터 N번까지이다.

# 입력 : 첫째 줄에 정점의 개수 N(1 ≤ N ≤ 1,000), 간선의 개수 M(1 ≤ M ≤ 10,000), 
# 탐색을 시작할 정점의 번호 V가 주어진다. 다음 M개의 줄에는 간선이 연결하는 두 정점의 번호가 주어진다. 
# 어떤 두 정점 사이에 여러 개의 간선이 있을 수 있다. 입력으로 주어지는 간선은 양방향이다.

# 출력 : 첫째 줄에 DFS를 수행한 결과를, 그 다음 줄에는 BFS를 수행한 결과를 출력한다. V부터 방문된 점을 순서대로 출력하면 된다.

# 4 5 1               1 2 4 3                  
# 1 2                 1 2 3 4
# 1 3
# 1 4
# 2 4
# 3 4



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

def BFS(s):
    from collections import deque
    
    #visited 배열 0으로 초기화
    visited = [0 for i in range(N+1)]
    visited[s] = 1  #첫번째 노드 방문
    print(s, end = ' ')
    queue = deque([])   #큐 생성
    queue.append(s)     #큐에 방문한 노드 push
    
    while(len(queue)!=0):   #큐가 not empty라면 반복문 실행
        u = queue.popleft() #큐에서 pop한 값을 u라고 선언
        for i in Node_list[u]:  #u주변노드들을 큐에 넣는다
            if(visited[i] == 0):    #방문한 노드가 아니라면
                visited[i] = 1  #방문했다고 표시
                print(i, end = ' ')
                queue.append(i)
                


def DFS(s):
    #첫번쨰 노드 방문
    visited[s] = 1
    print(s, end = ' ')
    for i in range(len(Node_list[s])):
        x = Node_list[s][i]
        if(visited[x] == 0):
            DFS(x)
    
    
    

visited = [0 for i in range(N+1)]
DFS(V)
print()
BFS(V)