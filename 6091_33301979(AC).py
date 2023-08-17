a,b,c=map(int,input().split())
n=1
while n%a!=0 or n%b!=0 or n%c!=0:
    n+=1
    
print(n)
