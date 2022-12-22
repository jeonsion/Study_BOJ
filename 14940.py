# BFS 이용하기
# BFS(넓이 우선 탐색) : 출발 노드로부터 가까운 정점을 먼저 방문하고 멀리 떨어져 있는 정점을 나중에 방문하는 방법!
# 큐를 이용한다

# 문제 : 모든 지점에 대해서 목표 지점 까지의 거리 구하기
# 0은 갈 수 없는 땅, 1은 갈 수 있는 땅, 2는 목표지점
#
from collections import deque
import sys
input = sys.stdin.readline


n, m = map(int, input().split())
map_list = [input().split() for i in range(n)] # 맵 정보 받기
distance_list = [[-1]*m for i in range(n)]   #거리 0으로 초기화
queue = deque([])   #큐선언
distance = 0


# 목표지점으로부터 시작
i,j = 0,0
distance_list[i][j] = 0         #0으로 셋팅
queue.append([i,j])             #큐에 넣기
while len(queue)!=0:        #큐가 비어있을 때 까지 실행
    u = queue.popleft() 
    distance+=1
    x,y=u[0], u[1]
    #1. 상하 좌우 전부 이동 가능 할 때 -> [i+1, j], [i-1, j], [i, j-1], [i, j+1] 넣기
    #2. 오른쪽과 아래만 가능할 때 -> [i, j+1], [i+1, j] 큐에 넣기
    #3. 왼쪽과 아래만 가능할 때 -> [i, j-1], [i+1, j] 큐에 넣기
    #4. 위와 오른쪽만 가능할 때 -> [i-1, j], [i, j+1] 큐에 넣기
    #5. 왼쪽과 위만 가능할 때 -> [i, j-1], [i-1, j] 큐에 넣기
    if(map_list[x][y] == 0):
        distance_list[x][y] = 0
    if(x-1 != -1 and x+1 != -1 and y-1 != -1 and y+1 != -1 and distance_list[x][y] == "No"):   #상하좌우 전부 이동 가능할 때
        distance_list[x-1, y]=distance_list[x+1, y]= distance
        distance_list[x, y-1]=distance_list[x, y+1] = distance
        queue.append([x-1, y], [x+1, y], [x, y-1], [x, y+1] )
    elif(y-1 == -1 and x-1 == -1 and distance_list[x][y] == "No"):    #오른쪽과 아래만 가능할 때
        distance_list[x, y+1] = distance_list[x+1, y] = distance
        queue.append([x, y+1], [x+1, x])
    elif(y+1 == n and x-1 == -1 and distance_list[x][y] == "No"):  #왼쪽과 아래만 가능할 때
        distance_list[x,y-1]=distance_list[x+1, y] = distance
        queue.append([x,y-1], [x+1,y])
    elif(y-1 == -1 and x+1 == n and distance_list[x][y] == "No"):    #위와 오른쪽만 가능할 때
        distance_list[x-1,y] = distance_list[x,j+1] = distance
        queue.append([x-1,y], [x, y+1])
    elif(x+1 == n and y+1 == n and distance_list[x][y] == "No"):
        distance_list[x, y-1]=distance_list[x-1,y] = distance
        queue.append([x,y-1], [x-1, y])
    
for i in distance_list:
    print(i)