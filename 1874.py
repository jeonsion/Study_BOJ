#스택 수열
# <스택에 push 하는 순서는 반드시 오름차순!>
# 임의의 수열이 주어졌을 때 스택을 이용해 수열을 만들 수 있는지 없는지. 있다면 어떤 순서로
#push와 pop을 수행해야하는지 알아내자

#스택 생성
stack = []

#정수의 개수 입력
n = int(input())

def empty():
    if(len(stack)==0):
        return 1
    else:
        return 0

#A_list = [4, 3, 6, 8, 7, 5, 2, 1]
# +
#수열을 이루는 정수 하나씩 입력받기
for i in range(n):
    if(not empty()):
        stack.append(input())
    