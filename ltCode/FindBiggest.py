def FindBiggestNumber(A, n):
    high = A[0]
    for digit in A:
        if digit > high:
            high = digit
    print("Highest Number:", high)


if __name__ == '__main__':
    input_size = int(input())
    print("Enter the array elements:")
    input_lst = [int(x) for x in input().split()]
    assert len(input_lst) == input_size, "Input Size is not equal to array size"
    FindBiggestNumber(input_lst, input_size)
