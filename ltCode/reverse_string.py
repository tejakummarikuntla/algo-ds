def reverse(st):
    rev = ""
    for i in st:
        rev = i + rev
    return rev

def reverse_string(st):
#    return st[::-1]
    st_list = list(st)
    rev_lst = []
    for i in range(1,len(st_list)+1):
        rev_lst.append(st_list[-i])

    rev_str = ''.join(rev_lst)
    return rev_str

if __name__ == "__main__":
    in_str = str(input())
    rev_with_lst = reverse_string(in_str)
    print("With List conversion ", rev_with_lst)
    rev_with_rev_add = reverse(in_str)
    print("With Stack rev", rev_with_rev_add)

