
ascending = [ i for i in range(1, 9)]
print(ascending)
descending = list(reversed(ascending))


a = list(map(int, input("정수입력하세요 : ").split()))
if(a == ascending):
    print("ascending")
elif (a==descending):
    print("descending")
else :
    print("mixed")
