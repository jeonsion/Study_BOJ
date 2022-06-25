#정렬을 사용하지 않고 푸는 법

n=int(input())
a=[]
for i in range(n):
    string = input()
    a.append(string)

a = list(set(a))
a.sort()                            #사전순으로 정렬
a.sort(key = lambda x : len(x))     #단어의 길이의 순으로 정렬

# for i in range(len(a)-1, 0, -1):
#     for j in range(i):
#         if(len(a[j]) >= len(a[j+1])):
#             a[j], a[j+1] = a[j+1], a[j]


print("출력")
for i in a:
    print(i)