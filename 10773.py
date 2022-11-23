#제로
K = int(input())
stack = []
for i in range(K):
    number = int(input())
    if(number !=0):
        stack.append(number)
    else:
        stack.pop(-1)

print(sum(stack))