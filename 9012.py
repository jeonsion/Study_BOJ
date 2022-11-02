#괄호
#스택이용하기

N = int(input())
A_list = []




for i in range(N):
    A_list.append(input())
    
for i in A_list:
    stack = []
    for j in i:
        #왼쪽 괄호일 때 push
        if(j == '('):
            stack.append(j)
            continue
        #오른쪽 괄호일 때
        else:
            #스택이 비어있지 않았다면
            if(len(stack)!=0):
                #스택의 top과 j를 비교
                if(stack[-1]!=j):
                    stack.pop()
            #비어있다면 스택에 넣어줌으로써 오류발생 일으킴
            else:
                stack.append(j)
    if(len(stack)!=0):
        print("NO")
    else:
        print("YES")