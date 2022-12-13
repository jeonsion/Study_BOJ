n = int(input())
count = 0
def fact(n):
    global result
    if n > 1:
        return n * fact(n-1)
    else:
        return 1

num = fact(n)

while num%10 == 0:
    num//=10
    count+=1
    
print(count)