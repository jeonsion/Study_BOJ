#0-20개 총 21개 문자열 생성 -> 이진수 역할
import sys
input = sys.stdin.readline

S = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
for i in range(int(input())):
    oper = input().split()
    
    if oper[0] == "add":
        oper[1] = int(oper[1])
        S[oper[1]] = 1
    elif oper[0] == "remove":
        oper[1] = int(oper[1])
        S[oper[1]] = 0
    elif oper[0] == "check":
        oper[1] = int(oper[1])
        print(S[oper[1]])
    elif oper[0] == "toogle":
        oper[1] = int(oper[1])
        if(S[oper[1]] != 0):
            S[oper[1]] = 0
        else:
            S[oper[1]]=1
    elif oper[0] == "all":
        S = [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
    elif oper[0] == "empty":
        S = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]