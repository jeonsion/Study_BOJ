
#마인크래프트
import sys
input = sys.stdin.readline

#N: 세로, M: 가로, B: 인벤토리안에 들어있는 블록의 개수
N, M, B = map(int, input().split())
land = []

for _ in range(N):  #입력을 1차원으로 리스트로 받기
    land += list(map(int, input().split()))


#블록을 제거하여 인벤토리에 넣는 경우 : 2초
#인벤토리에서 블록을 꺼내어 좌표에 놓는 경우 : 1초
#최대한 빠르게 땅을 고르게 해야함

#출력 : 땅을 고르게 만드는데 걸리는 시간, 땅의 높이 출력



time =0
compare_result_range = []

for i in range(0, 257):
    avg_land = i
    time = 0
    b = B
    for j in land:
        #만약 j가 평균보다 크면 j의 높이를 빼서 인벤토리를 넣는 과정을 통해 고르게 만들어주자
        if j> avg_land:
            b += j-avg_land
            time += 2*(j-avg_land)
        elif j == avg_land :    #기준 값과 동일한경우 pass
            #print("패스")
            continue
        else:                   #기준 값보다 작은 경우 인벤토리에서 블록을 빼서 땅에 추가해주는 작업
                b-=avg_land - j
                time += avg_land - j
    
    if(b < 0):  #최종적으로 인벤토리에 블록의 개수가 -, 즉 부족하다면 블록을 채우는 방법으로는 안되는거임 -> 무시
        pass
    else:
        compare_result_range.append([time, avg_land])

compare_result_range.sort(key=lambda x: (x[0], -x[1]))
print(compare_result_range[0][0], compare_result_range[0][1] )





