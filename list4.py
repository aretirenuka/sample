nums=list(map(int,input().split()))
c=0
for i in range(len(nums)):
    for j in range(i+1,len(nums)):
        if nums[i]==nums[j]:
            c+=1
print(c)
