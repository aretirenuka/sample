a=int(input())
b=int(input())
d=list(map(int,input().split()))
d.sort()
print(len(d[:-b]))
