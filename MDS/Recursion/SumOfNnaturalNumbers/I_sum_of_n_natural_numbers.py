def sum_of_n_numbers(n):
    global x
    if(n>0):
        if(n != x):
            x += n 
        return sum_of_n_numbers(n-1) 
    return x

if __name__ == '__main__':
    global x
    x = int(input())
    print(sum_of_n_numbers(x))