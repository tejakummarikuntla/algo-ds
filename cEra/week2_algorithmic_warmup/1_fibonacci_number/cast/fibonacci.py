# Uses python3
def fibonacci(n):
    fib_seq = [0, 1]

    for i in range(n):
        temp_val = fib_seq[i] + fib_seq[i + 1]
        fib_seq.append(temp_val)

    return fib_seq[n]

if __name__ == '__main__':
    input_n = int(input())
    res = fibonacci(input_n)
    print(res)

