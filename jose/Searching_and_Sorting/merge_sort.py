def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr)//2
        lefthalf = arr[:mid]
        righthalf = arr[mid:]

        merge_sort(lefthalf)
        merge_sort(righthalf)

        i, j, k = 0, 0, 0
        while(i < len(lefthalf) and j < len(righthalf)):
            if(lefthalf[i] < righthalf[j]):
                arr[k] = lefthalf[i]
                i += 1
            else:
                arr[k] = righthalf[j]
                j += 1
            k += 1

        while(i < len(lefthalf)):
            arr[k] = lefthalf[i]
            i += 1
            k += 1
        while(j < len(righthalf)):
            arr[k] = righthalf[j]
            j += 1
            k += 1
    return arr

arr = [1, 5, 3, 2, 7,2, 8, 2, 43, 12]
print(merge_sort(arr))