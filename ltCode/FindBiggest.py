



if __name__ == '__main__':
    input_size = int(input())
    print("Enter the array elements:")
    input_lst = [int(x) for x in input().split()]
    assert len(input_lst) == input_size, "Input Size is not equal to array size"
    print(input_size, input_lst)
