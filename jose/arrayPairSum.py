def arrayPairSum(arr, n):
    count = 0
    repeat_lst = [0]

    for el in arr:
        for r in arr:
            if int(el+r) == int(n):
                for i in range(len(repeat_lst)):
                    if repeat_lst[i] == el or repeat_lst[i] == r:
                        continue
                    else:
                        repeat_lst.append(el)
                        repeat_lst.append(r)
                        print(repeat_lst)
                        count = count + 1

    return count

if __name__ == '__main__':
    input_arr = [int(x) for x in input().split()]
    input_n = int(input())

    print(arrayPairSum(input_arr, input_n))
