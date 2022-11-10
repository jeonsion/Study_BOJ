#좌표정렬하기 

N = int(input())
A_list = []
for i in range(N):
    A_list.append(list(map(int, input().split())))
    
A_list = sorted(A_list,key = lambda x:(x[1], x[0]), reverse = False)

for i in A_list:
    print(*i)