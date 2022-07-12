def insertion_sort(arr):
    for i in range(1,len(arr)):
        key=arr[i]
        j=i-1
        while j>=0 and key<arr[j]:
            arr[j+1]=arr[j]
            print(arr)
            j-=1
        arr[j+1]=key
    return arr
arr=list(map(int,input().split()))
print(insertion_sort(arr))


Result: 	34 21 54 1 90
		[34, 34, 54, 1, 90]
		[21, 34, 54, 54, 90]
		[21, 34, 34, 54, 90]
		[21, 21, 34, 54, 90]
		[1, 21, 34, 54, 90]