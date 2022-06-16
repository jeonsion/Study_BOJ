triangle =list(map(int, input().split()))
hypo = max(triangle)
remain1, remain2 = sorted(triangle)[0], sorted(triangle)[1]

while(hypo!=0 and remain1!=0 and remain2!=0):
    if(hypo*hypo == remain1*remain1+ remain2*remain2):
        print("right")
    else:
        print("wrong")
    triangle =list(map(int, input().split()))
    hypo = max(triangle)
    remain1, remain2 = sorted(triangle)[0], sorted(triangle)[1]