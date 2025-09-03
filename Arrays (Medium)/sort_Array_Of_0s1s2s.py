#Q.2 SORT AN ARRAY OF 0s, 1s AND 2s
#Brute force - use merge sort - TC = O(nlogn) and SC = O(n)
#better - keep count of 0s, 1s and 2s and then fill the array with them - TC = O(n) and SC = O(1)
def sort0s1s2sBetter (arr):
    n = len(arr)
    cnt0 = 0
    cnt1 = 0
    cnt2 = 0
    for i in range (n):
        if arr[i] == 0:
            cnt0 += 1
        elif arr[i] == 1:
            cnt1 += 1
        else:
            cnt2 += 1
    #now fill the array with 0s, 1s and 2s
    for i in range (cnt0):
        arr[i] = 0
    for i in range (cnt0, cnt0 + cnt1): #until cnt0 + cnt1 because we have to fill 1s after 0s
        arr[i] = 1
    for i in range (cnt0 + cnt1, n):
        arr[i] = 2
    return arr
#Example usage
arr = [0,1,2,0,1,2,1,2,0,0,0,1]
print("Array after sorting 0s, 1s and 2s is:", sort0s1s2sBetter(arr))

#optimal - use dutch national flag algorithm - TC = O(n) and SC = O(1)
#low, mid and high pointers: low and mid start from 0 and high starts from n-1
#if arr[mid] == 0, swap arr[low] and arr[mid], increment both low and mid
#if arr[mid] == 1, increment mid
#if arr[mid] == 2, swap arr[mid] and arr[high], decrement high
def sort0s1s2sOptimal (arr):
    n = len(arr)
    low, mid = 0, 0
    high = n - 1
    while mid <= high: #when mid crosses high, all elements are sorted
        if arr[mid] == 0:
            arr[low], arr[mid] = arr[mid], arr[low]
            low += 1
            mid += 1
        elif arr[mid] == 1:
            mid += 1
        else:
            arr[mid], arr[high] = arr[high], arr[mid]
            high -= 1
    return arr
#Example usage
arr = [0,1,2,0,1,2,1,2,0,0,0,1]
print("Array after sorting 0s, 1s and 2s is:", sort0s1s2sOptimal(arr))
