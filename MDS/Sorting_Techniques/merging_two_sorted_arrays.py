def merging(arr1, arr2):
    len_arr1 = len(arr1)
    len_arr2 = len(arr2)
    k = []
    i, j = 0, 0
    while(i<len_arr1 and j<len_arr2):
        if arr1[i] > arr2[j]:
            k.append(arr2[j])
            j +=1 
        else:
            k.append(arr1[i])
            i += 1
    
    if(i < len_arr1):
        while(i < len_arr1):
            k.append(arr1[i])
            i += 1
    if(j < len_arr2):
        while(j < len_arr2):
            k.append(arr2[j])
            j += 1
    
    return k

print(merging([2, 6, 7, 9, 10, 13, 15, 17], [1, 3, 5, 8, 11, 14, 16, 19, 22, 25]))
print(merging([2], [1]))
