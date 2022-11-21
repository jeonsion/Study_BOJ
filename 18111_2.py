
#마인크래프트
import sys
import copy
input = sys.stdin.readline

#N: 세로, M: 가로, B: 인벤토리안에 들어있는 블록의 개수
N, M, B = map(int, input().split())
land = [list(map(int, input().split())) for i in range(N)]


MAX = max(map(max, land))

#블록을 제거하여 인벤토리에 넣는 경우 : 2초
#인벤토리에서 블록을 꺼내어 좌표에 놓는 경우 : 1초
#최대한 빠르게 땅을 고르게 해야함

#출력 : 땅을 고르게 만드는데 걸리는 시간, 땅의 높이 출력


#평균 구하기



#고르게 만드는시간, 땅 선언

time =0

def make_land_flat_(n, P_land):
    virtual_land = copy.deepcopy(P_land)
    global B
    global time
    avg_land = n
    time = 0
    b = B
    
    for i in range(N):
        for j in range(M):
            #만약 j가 평균보다 크면 j의 높이를 빼서 인벤토리를 넣는 과정을 통해 고르게 만들어주자
            if virtual_land[i][j]> avg_land:
                b += virtual_land[i][j]-avg_land
                time += 2*(virtual_land[i][j]-avg_land)
                virtual_land[i][j] = avg_land

            elif virtual_land[i][j] == avg_land :
                #print("패스")
                continue
            else: 
                    b-=avg_land - virtual_land[i][j]
                    time += avg_land - virtual_land[i][j]
                    virtual_land[i][j] = avg_land

    
    if(b < 0):  #만약 인벤토리에 블록의 개수가 부족하다면 블록을 채우는 방법으로는 안되는거임 -> 평균층수를 낮추자
        pass
    else:
        compare_result_range.append([time, avg_land])




compare_result_range = []

for i in range(0, MAX+1):
    result_land = make_land_flat_(i, land)
    result_land = 0

compare_result_range.sort(key=lambda x: (x[0], -x[1]))
print(*compare_result_range[0])





