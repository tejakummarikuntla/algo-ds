# input_txt = [int(x) for x in input().split()]
input_txt = [2, 6, 8, 1, 4]
def inesertion_sort(arr):
    for j in range(1, len(arr)):
        key = arr[j]
        i = j-1

        while(i>0 and arr[i] > key):
            arr[i+1] = arr[i]
            i = i-1

        arr[i+1] = key
    print(arr)

inesertion_sort(input_txt)
