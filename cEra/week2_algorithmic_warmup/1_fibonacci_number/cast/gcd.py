def gcd(ar):
    res = 0
    for i in range(1, ar[0]+ar[1]):
        if ar[0] % i == 0 and ar[1] % i == 0:
            res = i
    return res

if __name__ == '__main__':
    input_lst = [int(x) for x in input().split()]
    print(gcd(input_lst))
