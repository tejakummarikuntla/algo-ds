
arr1 = [1, 3, 5, 7, 9]
arr2 = [2, 4, 6, 8, 10, 11]
res = []
def merge(arr1, arr2, len_arr1, len_arr2):
    i,j = 0,0
    while(i<len_arr1 and j<len_arr2):
        if(arr1[i] > arr2[j]):
            res.append(arr2[j])
            j += 1
            # k += 1
        if(arr1[i] < arr2[j]):
            res.append(arr1[i])
            i += 1
            # k += 1
    
    while(i<len_arr1):
        res.append(arr1[i])
        # k += 1
        i += 1
    while(j<len_arr2):
        res.append(arr2[j])
        # k += 1
        j += 1
    print(res)

merge(arr1, arr2, len(arr1), len(arr2))
