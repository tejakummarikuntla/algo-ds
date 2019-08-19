def startStep(s, k):
    start = 0
    step = k

    print("Inpu Str:",s)
    for i in range(len(s)+1):
        print(s[int(start):int(step)])
        start = start+1
        step = step+1

if __name__ == '__main__':
    input_str = input()
    input_step = int(input())

    startStep(input_str, input_step)
