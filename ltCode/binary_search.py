
def binSearch(ar, key):
    if ar[0] == [-1]:
        if ar[0] == key:
            return "Found"
        else:
            return "No element Found in single element Array"

    mid_val = ar[int(len(ar)/2)]
    if mid_arr == key:
        return "Element Found"
    if mid_arr > key:
        mid_arr_left = int(len(ar[:mid_arr])/2)
        if mid_arr_left == key:
            return "Found"
        if`




if __name__ == "__main__":
    in_arr = [int(x) for x in input().split()]
    in_key = int(input())

    binSearch(in_arr, in_key)
