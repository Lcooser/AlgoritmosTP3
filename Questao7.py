def quickselect(arr, k):
    if len(arr) == 1:
        return arr[0]
    
    pivot = arr[-1]
    left = [x for x in arr[:-1] if x <= pivot]
    right = [x for x in arr[:-1] if x > pivot]
    
    if len(left) == k:
        return pivot
    elif len(left) > k:
        return quickselect(left, k)
    else:
        return quickselect(right, k - len(left) - 1)

arr = [3, 6, 8, 10, 1, 2, 1]
k = 3
print(quickselect(arr, k)) 