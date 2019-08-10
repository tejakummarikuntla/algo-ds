
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
    rev = reverse_string(in_str)
    print(rev)
