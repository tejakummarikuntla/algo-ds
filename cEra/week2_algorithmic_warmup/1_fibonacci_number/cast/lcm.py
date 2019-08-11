# Uses python3
def gcd(a, b):
    if b == 0:
        return a
    eRem = a%b
    return gcd(b, eRem)



if __name__ == '__main__':
    a, b = [int(x) for x in input().split()]
    if a > b:
        gcd = gcd(a,b)
    else:
        gcd = gcd(b,a)

    res = (a * b)//(gcd)
    print(res)
