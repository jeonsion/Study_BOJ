
a = list(map(int, input().split()))
sum=0
for i in range(5):
    sum += a[i]*a[i]
print(sum%10)
