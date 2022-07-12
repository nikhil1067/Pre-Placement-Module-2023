def binary_search(arr,target):
    low=0
    high=len(arr)-1
    while low<=high:
        mid=(low+high)//2
        if arr[mid]==target:
            return mid
        elif arr[mid]>target:
            high=mid-1
        else:
            low=mid+1
    return "Not Found"
arr=list(map(int,input().split()))
target=int(input())
print(binary_search(arr,target))

Result: 	12 34 56 78 90
		78
		3