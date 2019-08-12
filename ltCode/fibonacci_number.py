def fibonacci(n):
    if n == 0 :
        return n
    if n == 1 :
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)


if __name__ == '__main__':
    input_n = int(input())
    res = fibonacci(input_n)
    print(res)
