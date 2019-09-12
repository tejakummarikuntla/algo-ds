def Anagram(str1, str2):
    str1 = str1.remove(' ', '').lower()
    str2 = str2.remove(' ', '').lower()

    return sorted(str1) == sorted(str2)


#########################################3
def AnagramCheck(str1, str2):
    str1 = str1.replace(' ','').lower()
    str2 = str2.replace(' ','').lower()

    counts = {}

    for letter in str1:
        if letter in counts:
            counts[letter] += 1
        else:
            counts[letter] = 1
    for letter in str2:
        if letter in counts:
            counts[letter] -= 1
        else:
            counts[letter] = 1

    for k in counts:
        if counts[k] != 0:
            return False

    return True


if __name__ == '__main__':
    input_str1 = input()
    input_str2 = input()

    print(AnagramCheck(input_str1, input_str2))

