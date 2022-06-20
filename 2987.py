


n, m = map(int, input().split())
card = list(map(int,input().split()))
max = 0
sum_card = 0
for i in range(len(card)):
    for j in range(i+1, len(card)):
        for k in range(j+1, len(card)):
            sum_card = card[i]+card[j]+ card[k]
            if(max<=sum_card and   sum_card<=m):
                max = sum_card
print(max)