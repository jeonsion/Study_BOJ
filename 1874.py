#스택 수열
# 1-n까지의 수를 스택에 넣엏다가 뽑아 늘어놓으며 수열을 만들 수 있다.
# 스택에 push 하는 순서는 반드시 오름차순을 지킨다.
# 임이의 수열이 주어졌을 때 어떤 순서로 push, pop 해야하나??

# 수열을 저장할 리스트 생성
seq = []

#스택 생성
stack = []
# 정수 n개 입력받기
N = int(input())
for i in range(N):  #수열 입력받아 저장하기
    seq.append(int(input()))

# 생성된 수열 seq = [4, 3, 6, 8, 7, 5, 2, 1]


# 1부터 N까지 스택에 넣다 빼며 수열의 값과 비교할 것이다.
result = []
def check():
    check_count = 0
    i = 1
    while(check_count != N and i<1000001):    #모든 수열을 체크할 때 까지 반복문 수행
        if(len(stack)!=0 and seq[check_count] == stack[-1]):    #스택이 비어있지 않으며 top값과 seq[check]값이 일치하면 pop
            stack.pop()
            result.append("-")
            #print("-")
            check_count +=1 #수열 확인했으므로 그 다음 인덱스로 증가
        else:
            stack.append(i)
            result.append("+")
            #print("+")
            i+=1    # 한번 스택에 넣었으면 i를 증가한다
    return check_count  #얼만큼 체크했는지 반환한다

#수열의 길이만큼 체크를 한 경우 
if(check() == N):
    print(*result, sep = '\n')
else:
    print("NO")