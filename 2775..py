def live(k, n):                 #재귀함수
    sum=0
    if(k == 0):                 #0층에는 호수만큼 사람들이 살고 있다
        return n
    else:                       #각 층을 고려해야하고 호수도 고려해야하기 때문에 2차원 배열이나 파스칼 삼각형(?)을 떠올려봄
        for i  in range(1, n+1):        #for문으로 각 층마다 접근하고 범위로 호수에 접근
            sum+=live(k-1, i)
    
    return sum

t = int(input())
for i in range(t):
    k=int(input())
    n = int(input())
    print(live(k,n))
    
# <고찰>
# python3로 제출시 컴파일 시간초과
# ->pypy3로 제출시 정답처리
