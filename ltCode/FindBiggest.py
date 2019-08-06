def FindBiggestNumber(A, n):
    high = A[0]
    for digit in A:
        if digit > high:
            high = digit
    print("Highest Number:", high)

def FindBiggestRec(A, n):
    index_range = n-1
    high = A[0]

    if(n == -1):
        return high
    else:
        if A[index_range] > high:
            high = A[index_range]
    return FindBiggestRec(A, n-1)

if __name__ == '__main__':
    input_size = int(input())
    print("Enter the array elements:")
    input_lst = [int(x) for x in input().split()]
    assert len(input_lst) == input_size, "Input Size is not equal to array size"
    bigg = FindBiggestRec(input_lst, input_size)
    print("Bigg:", bigg)
