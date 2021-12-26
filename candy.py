a=list(map(int,input().split()))
extracandies=int(input())
b=[]
for i in range(len(a)):
    if(a[i]+extracandies)<max(a):
        b.append(False)
    else:
        b.append(True)
print(b)        
