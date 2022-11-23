#덩치

N = int(input())
P_list = []
for i in range(N):
    P_list.append(list(map(int, input().split())))

#등수 정보 저장 리스트
result_list = []

for i in range(N):
    result =0
    for j in range(N):
        if(P_list[i][0] < P_list[j][0]  and P_list[i][1] < P_list[j][1]):
            result +=1
    result_list.append(result+1)
     
print(*result_list)