def motu_patlu(arr):
    for i in range(len(arr)):
        len_ar = len(arr[i])
        mid_val = int(len_ar//2)

        mt_sum = 0
        pt_sum = 0
        mt_lst = arr[0:mid_val]
        pt_lst = arr[mid_val:]
        for dig in mt_lst:
            mt_lst = mt_lst + dig
        for dig in pt_lst:
            pt_lst = pt_lst + dig





if __name__ == '__main__':
    test_cases_len = int(input())
    i_lst = []
    for _ in range(test_cases_len):
        input_n = int(input())
        lst = [int(x) for x in input().split()]
        i_lst.append(lst))
    motu_patlu(i_lst)

