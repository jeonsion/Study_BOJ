#나는야 포켓몬 마스터 이다솜
import sys
input = sys.stdin.readline

Poketmon = {}
Poketmon_reverse = {}
N, M = map(int, input().split())
for i in range(1, N+1):
    key = input()
    Poketmon["{}".format(key)] = i
    Poketmon_reverse["{}".format(i)] = key
#문제 들어간다.
#아이디어 -> 딕셔너리를 뒤집어서 저장해버렷
for i in range(M):    
    #입력받기
    q = input()     
    try:
        print(Poketmon[q])  
    except:
        print(Poketmon_reverse[q])