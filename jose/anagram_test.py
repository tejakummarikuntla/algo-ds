def anagram(str1, str2):

    str1 = str1.replace(' ','').lower()
    str2 = str2.replace(' ','').lower()

    counts = {}

    for st in str1:
        if st in counts:
            counts[st] += 1
        else:
            counts[st] = 1

    for st in str2:
        if st in counts:
            counts[st] -= 1
        else:
            counts[st] = 1


    for count in counts:
        if counts[count] != 0:
            return False

    return True

if __name__ == '__main__':
    str1 = input()
    str2 = input()

    print(anagram(str1, str2))

