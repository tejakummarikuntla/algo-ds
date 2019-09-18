def pair_sum(arr,k):
    lst = []
    counts = {}

    for ar in arr:
        for ae in arr:
            if int(ar+ae) == int(k):
                if ((ar, ae) or (ae, ar)) in counts:
                    counts[(ar, ae)] += 1
                else:
                    counts[(ar, ae)] = 1
                lst.append((ar,ae))
    print(lst)
    print(counts)

    rep_list = []
    tmp_count = len(counts)
    for dic in counts:
        if counts[dic] == 1:
            rep_list.append(dic)

    print(rep_list)

    for tup in rep_lst:
        if tup[0], tup [1] == tup

