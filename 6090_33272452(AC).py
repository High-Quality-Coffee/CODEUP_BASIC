a,m,d,n=map(int,input().split())

if(n==1):
    print(a)
else:
    for i in range(n-1):
        a=a*m+d
    print(a)
    
