x,y,w,h=map(int, input().split())

compare_x = 0
compare_y = 0
if (abs(h-y)<y):
    compare_x = abs(h-y)
else:
    compare_x = y
    
if (abs(x-w)<x):
    compare_y = abs(x-w)
else:
    compare_y = x
    
if(compare_x<compare_y):
    print(compare_x)
else :
    print(compare_y)
    
