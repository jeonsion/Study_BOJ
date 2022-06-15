s=input()
#baekjoon입력
a=list("abcdefghijklmnopqrstuvwxyz")
#a=list(map(chr,range(97,123)))과 같음
for i in a  :
  if i in s :
    print(s.index(i),end=' ')
  else :
    print("-1",end=' ')
    
