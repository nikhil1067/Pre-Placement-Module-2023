string=input()
n=len(string)
target=input()
m=len(target)
res=[]
for i in range(n-m+1):
    temp=string[i:i+m]
    if target==temp:
        res.append([i,i+m-1])
if len(res)==0:
    print("Not Found")
else:
    print(res)