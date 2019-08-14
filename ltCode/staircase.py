def stair_case(n):
    chars = [" ", "#"]
    for i in range(1,n+1):
        print((n-i)*chars[0]+(i*chars[1]))

if __name__ == '__main__':
    input_n = int(input())
    stair_case(input_n)
