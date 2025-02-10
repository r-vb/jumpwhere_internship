# removing k-1 times maximum number from array and result would be Kth largest number
def kthlargest(arr, k):
    for i in range(k-1):
        arr.remove(max(arr))
    return max(arr)
# T: O(kn)
# S(n,k): O(1)

# using sorting
def kthlargest(arr, k):
    arr.sort(reverse=True)
    return arr[k-1]
# T: O(nlogn)
# S: O(n)

# using priority queue and heap
# yt-sol
import heapq
def kthlargest(arr, k):
    arr = [-ele for ele in arr]
    heapq.heapify(arr)
    for i in range(k-1):
        heapq.heappop(arr)
    return -heapq.heappop(arr)
# T: O(nlogk) when k almost = n T: O(nlogn)
# S: O(n)
import heapq
def kthlargest(arr, k):
    return heapq.nlargest(k, arr)[-1]
# T: O(nlogk)
# S: O(k)

# using quick select
def kthlargest(arr, k):
    if len(arr) == 1:
        return arr[0]
    pivot = partition(arr, 0, len(arr)-1)
    if k-1 == pivot:
        return arr[pivot]
    elif k-1 < pivot:
        return kthlargest(arr[:pivot], k)
    else:
        return kthlargest(arr[pivot+1:], k-(pivot+1))
# T: O(n) on average, O(n^2) in worst case
# S: O(logn) on average, O(n) in worst case