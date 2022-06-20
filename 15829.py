#'a'의 아스키 코드 값은 97 ord('a')=>>97

def print_sum_list(list):
    sum = 0
    for i in list:
        sum+=i
    print(sum%1234567891)

l = int(input())
string = input()
ascii=[]
sum=0
for i in string:                #리스트 아스키 값으로 변환
    ascii.append((ord(i)-96))
    
for i in range(l):          #31를 등비로 갖는 등비수열로 리스트 값 변환
    ascii[i]*=(31**i)

print_sum_list(ascii)