def merge_sort(arr):
    if len(arr)>1:
        mid=len(arr)//2
        arr1=arr[:mid]
        arr2=arr[mid:]
        merge_sort(arr1)
        merge_sort(arr2)
        i=j=k=0
        while i<len(arr1) and j<len(arr2):
            if arr1[i]<arr2[j]:
                arr[k]=arr1[i]
                i+=1
            else:
                arr[k]=arr2[j]
                j+=1
            k+=1
        while i<len(arr1):
            arr[k]=arr1[i]
            i+=1
            k+=1
        while j<len(arr2):
            arr[k]=arr2[j]
            j+=1
            k+=1
arr=list(map(int,input().split()))
merge_sort(arr)
print(arr)



Result: 	1 12 34 21 11
		[1, 11, 12, 21, 34]