word=input().lower()   #baaa
word_list=list(set(word)) #word_list =['b', 'a']
#print(word_list)
cnt=[]
for i in word_list :
    count = word.count(i)
    cnt.append(count)   #cnt = ['3', '1']
#print("cnt : ", cnt)

if cnt.count(max(cnt)) >=2 :
    print("?")
else :
    print(word_list[cnt.index(max(cnt))].upper())

#참고 : https://wook-2124.tistory.com/257