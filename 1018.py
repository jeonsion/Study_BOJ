#체스판 다시 칠하기

N, M = map(int, input().split())
chess_board = []
for i in range(N):
    chess_board.append(input())


#맨왼쪽 위 칸이 흰색이 경우
case1 = ['WBWBWBWB',
        'BWBWBWBW',
        'WBWBWBWB',
        'BWBWBWBW',
        'WBWBWBWB',
        'BWBWBWBW',
        'WBWBWBWB',
        'BWBWBWBW']
#맨왼쪽 위 칸이 검정색인 경우
case2 = ['BWBWBWBW',
        'WBWBWBWB',
        'BWBWBWBW',
        'WBWBWBWB',
        'BWBWBWBW',
        'WBWBWBWB',
        'BWBWBWBW',
        'WBWBWBWB']


#추가로 체스판에서 반복문으로 비교해야하는 횟수
extra_N = N-7   #행
extra_M = M-7   #렬


#case1과 비교 하는 함수
def compare_case1():
    compare_stack = []
    for i in range(extra_N):
        for j in range(extra_M):
            count = 0
            for x in range(8):
                for y in range(8):
                    if case1[x][y] != chess_board[i+x][j+y]:
                        count+=1
            if len(compare_stack) == 0:
                compare_stack.append(count)
            if(compare_stack[0]>count):
                compare_stack.pop()
                compare_stack.append(count)             
    return compare_stack[0]

def compare_case2():
    compare_stack = []
    for i in range(extra_N):
        for j in range(extra_M):
            count = 0
            for x in range(8):
                for y in range(8):
                    if case2[x][y] != chess_board[i+x][j+y]:
                        count+=1
            if len(compare_stack) == 0:
                compare_stack.append(count)
            if(compare_stack[0]>count):
                compare_stack.pop()
                compare_stack.append(count)
    return compare_stack[0]

print(min(compare_case1(), compare_case2()))