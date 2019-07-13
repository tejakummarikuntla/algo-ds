# python3

def max_pairwise_product(numbers):
    n = len(numbers)
    max_product = 0
    for first in range(n):
        for second in range(first + 1, n):
            max_product = max(max_product,
                    numbers[first] * numbers[second])

    return max_product

def max_pairwise_product_fast(numbers):
    max_num_1 = max(numbers)
    numbers.remove(max_num_1)
    max_num_2 = max(numbers)

    return max_num_1 * max_num_2

if __name__ == '__main__':
    input_n = int(input())
    input_numbers = [int(x) for x in input().split()]
    print(max_pairwise_product_fast(input_numbers))



