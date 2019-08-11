# Uses python3
def gcd(ar):
    a = ar[0]
    b = ar[1]
    if b ==  0:
        return a

    ereminder = a % b
    return gcd([b, ereminder])



if __name__ == "__main__":
     n_input = input()
     n_list = [int(x) for x in n_input.split()]
     print(gcd(n_list))

