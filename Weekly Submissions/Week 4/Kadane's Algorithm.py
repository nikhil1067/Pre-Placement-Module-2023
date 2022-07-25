from math import inf
arr=[-2,1,-3,4,-1,2,1,-5,4]
n=len(arr)
res=-inf
temp=0
for num in arr:
    temp+=num
    res=max(res,temp)
    if temp<0:
        temp=0
print(res)