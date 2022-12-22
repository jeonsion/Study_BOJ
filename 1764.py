import sys
input = sys.stdin.readline
N_list = []
M_list = []

#사람 명단 입력받기
def make_dict():
    N, M = map(int, input().split())
    for i in range(N):
        N_list.append(input().strip())

    for i in range(M):
       M_list.append(input().strip())
        
make_dict()

print(N_list)
print(M_list)

common = set(N_list) & set(M_list)  #공통 부분 찾기 set함수 이용
print(common)



common = list(common)   #sort()메소드를 사용하기위해 list를 취해준다
common.sort()

print(len(common))  #공통된 듣보잡의 수
for i in common:    #출력하기
    print(i)





