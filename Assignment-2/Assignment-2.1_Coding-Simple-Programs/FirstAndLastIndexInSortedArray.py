def indexfirstlast(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            start =i
            while (i+1<=len(arr) and arr[i+1]) == target:
                i += 1
            return [start,i]
    return [-1,-1]
# this was using linear search
# T(n): O(n)
# S(n) : O(1)

# now binary search
def findstart(arr, target):
    if arr[0] == target:
        return 0
    left, right = 0, len(arr)-1
    while left <= right:
        mid = (left+right)//2
        if arr[mid] == target and arr[mid-1] < target:
            return mid
        elif arr[mid] < target:
            left = mid+1
        else:
            right = mid-1
    return -1
def findend(arr, target):
    if arr[-1] == target:
        return len(arr)-1
    left, right = 0, len(arr)-1
    while left <= right:
        mid = (left+right)//2
        if arr[mid] == target and arr[mid-1] > target:
            return mid
        elif arr[mid] > target:
            left = mid-1
        else:
            right = mid+1
    return -1
def firstandlast(arr, target):
    if len(arr) == 0 or arr[0] > target or arr[-1] < target:
        return [-1,-1]
    else:
        start = findstart(arr,target)
        end = findend(arr,target)
    return [start,end]
# T(O) : 2 * O(log n) = O(log n)
# S(O) : O(1)