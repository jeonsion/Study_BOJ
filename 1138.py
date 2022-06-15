n=int(input())
narr=list(map(int, input().split()))
narr.sort()
m=int(input())
marr=list(map(int,input().split()))

for i in marr :
  start=0
  end=n-1         #-1을 하는 이유는 mid를 구할 때 배열에 접근하기 위해
  result=0
  while start <= end  :
    mid=(start+end)//2
    if  narr[mid]== i :
      result=1
      break
    elif narr[mid] > i  :
      end=mid-1
    else :
      start=mid + 1
  print(result)
