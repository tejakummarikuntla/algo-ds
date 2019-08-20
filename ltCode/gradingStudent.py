def calc_five_mult(arr):
    five_mult = []
    for el in arr:
        if el >= 38:
            for i in range(5):
                if (el + i) % 5 == 0:
                    five_mult.append(el+i)
                    break
        else:
            five_mult.append(el)
    return five_mult

def gradingStudents(arr):
    result = []
    five_mult = calc_five_mult(arr)
    for i in range(len(arr)):
        if arr[i] >= 38 and five_mult[i] - arr[i] <3:
            result.append(five_mult[i])
        else:
            result.append(arr[i])

    for res in result:
        print (res)

if __name__ == '__main__':
    input_n = int(input())
    input_arr = []
    for i in range(input_n):
        input_arr.append(int(input()))
    gradingStudents(input_arr)
