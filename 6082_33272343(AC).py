n=int(input())
for i in range(n):
    if((i+1)>=10 and (i+1)%10!=0 and (i+1)%10%3==0):
        print('X',end=" ")
    elif((i+1)<10 and (i+1)%3==0 and (i+1)!=1):
        print('X',end=" ")
    else:
        print(i+1,end=" ")
