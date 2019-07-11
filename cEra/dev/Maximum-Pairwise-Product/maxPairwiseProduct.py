lst_arr = []
input_size = input("Enter Input Size: ")
for i in range(0, int(input_size)):
    temp_arr = input("Enter List Elements: ")
    lst_arr.append(temp_arr)

mult_arr = []
temp_val = 0
for i in range(0, len(lst_arr)):
    for j in range(0, len(lst_arr)):
        if i == j:
            continue
        temp_val = int(lst_arr[i])*int(lst_arr[j])
        #print(lst_arr[i], " * ", lst_arr[j], " = ", temp_val)
        mult_arr.append(temp_val)
print("MAX: ", max(mult_arr))
