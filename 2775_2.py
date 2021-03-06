#부녀회장이 될테야 시간초과를 해결할 수 있는 고수님의 동적 프로그래밍
#참고 문헌 : https://techblog-history-younghunjo1.tistory.com/183
#입력 제한 (1 ≤ k, n ≤ 14)

#모든 층에 호실에 -1 대입

dp = [[-1 for col in range(15)] for row in range(15)]           #내가 짠 코드와 다른 점 : 메모제이션 캐싱기법 top-down(다이나믹 프로그래밍) + 재귀함수
def live(k, n):
    if(dp[k][n]!=-1):                                           
        return dp[k][n]
    sum = 0
    
    if(k ==0):
        return n
    else:
        for i in range(1, n+1):
            sum+=live(k-1, i)
        dp[k][n]=sum
    return sum

t = int(input())
for i in range(t):
    k=int(input())
    n = int(input())
    print(live(k,n))