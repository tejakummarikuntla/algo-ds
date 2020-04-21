def sel_sort(arr):
    for i in range(0, len(arr)):
        k = i
        for j in range(i+1, len(arr)):
            if(arr[j] < arr[k]):
                k = j
        arr[i], arr[k] = arr[k], arr[i]
        
        return arr
