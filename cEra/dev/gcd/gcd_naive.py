def gcd():
    best = 0
    for i in range(2, n_list[0] + n_list[1]):
        if n_list[0]%i == 0 and n_list[1]%i == 0:
            best = i
    print(best)

if __name__ == "__main__":
    n_input = input()
    n_list = [int(x) for x in n_input.split()]
    gcd()
