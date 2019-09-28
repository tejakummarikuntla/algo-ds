import collections

def find_miss(arr, brr):
    arr_sum = 0
    brr_sum = 0

    for ar in arr:
        arr_sum += ar
    for br in brr:
        brr_sum += br

    return arr_sum - brr_sum
###################################
def find2(arr, brr):
    dic = collections.defaultdict(int)

    for num in brr:
        dic[num] += 1

    for num in arr:
        if dic[num] == 0:
            return num
        else:
            dic[num] -= 1



if __name__ == '__main__':

    input_oarr = [int(x) for x in input().split()]
    input_tarr = [int(x) for x in input().split()]

    print(find_miss(input_oarr, input_tarr))
    print(find2(input_oarr, input_tarr))
