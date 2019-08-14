def plusMinus(arr):
    z_count = 0
    p_count = 0
    n_count = 0
    for i in arr:
        if i < 0:
            n_count = n_count + 1
        if i > 0:
            p_count = p_count + 1
        if i == 0:
            z_count = z_count + 1
    print(p_count/input_n)
    print(n_count/input_n)
    print(z_count/input_n)

if __name__ == '__main__':
    input_n = int(input())
    arr = [int(x) for x in input().split()]
    plusMinus(arr)
