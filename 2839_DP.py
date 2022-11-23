N = int(input())
dp = [-1 for i in range(5001)] #-1로 초기화
dp[3] = 1
dp[5] = 1

if N<=5:
    print(dp[N])
else:
    for i in range(6, N+1): #6부터 N까지 DP확인
        #a: 5키로 추가 전 무게의 봉투 최소값
        #b: 3키로 추가 전 무게의 봉투 최소값
        a=b=dp[i]
        #현재무게에서 5키로 전 DP가 가능하다면 할당
        if(dp[i-5]!=-1):
            a = dp[i-5]
        #현재무게에서 3키로 전 DP가 가능하다면 할당
        if(dp[i-3]!=-1):
            b = dp[i-3]
            
        #두값을 비교해서 둘중 작은 값 선택
        if(a>0 and b>0):
            dp[i] = min(a+1, b+1)
        elif(a>0 and b<0):
            dp[i] = a+1
        elif(a<0 and b>0):
            dp[i] = b+1
        #불가능하면 -1할당
        else:
            dp[i] = -1 
            
print(dp[N])