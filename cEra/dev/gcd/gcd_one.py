input_n = input()
input_lst = [int(x) for x in input_n.split()]
gcd_lst = []
gcd_lst_ano = []
#for dig in input_lst:
#    for i in range(1,11):
#        if(dig % i == 0):
#            gcd_lst.append(i)

min_number = min(input_lst)
for i in range(1,11):
    if (min_number % i == 0):
        gcd_lst.append(i)

for item in gcd_lst:
    if(max(gcd_lst) % item == 0):
        gcd_lst_ano.append(item)

print("Min:", gcd_lst)
print("max:", gcd_lst_ano)

