#피보나치 함수

T = int(input())

def fibonacci(n):
    N = [-1 for i in range(40)]
    
    N[1] = N[2] = 1
    for i in range(3, n+1):
        N[i] = N[i-1] + N[i-2]
    return N[n]


    