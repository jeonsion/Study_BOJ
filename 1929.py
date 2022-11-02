#소수구하기
#에라토스 테네스의 체

M, N = map(int, input().split())

A_list = [i for i in range(N+1)]

#1은 소수가 아니므로 False할당
A_list[1] = False


#M까지 에라토스테네스의 체 만들기

for i in range(2, N):
    if(A_list[i]!=False):
        mul = 2
        while(i*mul<=N):
            A_list[i*mul] = False
            mul+=1

for i in range(M, N+1):
    if(A_list[i] != False):
        print(A_list[i])
        