import sys
import copy
input = sys.stdin.readline

#N: 세로, M: 가로, B: 인벤토리안에 들어있는 블록의 개수
N, M, B = map(int, input().split())
land = []
for _ in range(N):
    land += list(map(int, input().split()))


MAX = max(land)
print(land)