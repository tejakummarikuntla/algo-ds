def minimumBribes(q):
    for i in range(len(q)-1):
        j = i + 1
        if q[i] > q[j]:
            q[i], q[j] = q[j], q[i]
        print(q)

if __name__ == '__main__':
    t = int(input())

    for t_itr in range(t):
        n = int(input())

        q = list(map(int, input().rstrip().split()))
        minimumBribes(q)
