def gcd(digit1, digit2):
    best = 0
    for i in range(2, digit1 + digit2):
        if digit1%i == 0 and digit2%i == 0:
            best = i
    print(best)

def ecludianGcd(a, b):
    if b == 0:
        return a
    eReminder = a % b
    return ecludianGcd(b, eReminder)

if __name__ == "__main__":
    n_input = input()
    n_list = [int(x) for x in n_input.split()]
    # if n_list[0] == 0:
    #     print(n_list[1])
    # reminder = int(n_list[0]%n_list[1])
    # gcd(n_list[0], reminder)
    gcdRes = ecludianGcd(n_list[0], n_list[1])
    print(gcdRes)

