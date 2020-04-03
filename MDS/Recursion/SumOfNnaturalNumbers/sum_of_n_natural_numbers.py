def sum_of_n_natural_numbers(n):
    if(n == 0):
        return 0
    else:
        return sum_of_n_natural_numbers(n-1)+n

if __name__ == '__main__':
    x = int(input())
    print(sum_of_n_natural_numbers(x))