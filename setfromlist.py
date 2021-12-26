a=list(map(int,input().split()))
f=[]
for i in a:
    if i not in f:
        f.append(i)
print(f)
print(set(a))
