input_n = input()
input_lst = [int(x) for x in input_n.split()]
res = 0
for i in range(1,input_lst[0] + input_lst[1]):
    if input_lst[0] % i == 0 and input_lst[1] % i == 0:
        res = i

print(res)

