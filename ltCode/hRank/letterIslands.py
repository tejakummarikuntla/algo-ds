def substring_search(sub_str, string):
    island_val = 0
    start = 0
    step = len(sub_str)
    for i in range(len(string)+1):
        if sub_str == string[int(start):int(step)]:
            island_val = island_val + 1
        start = start + 1
        step = step + 1
    return island_val

def letterIslands(s, k):
    is_val = 0
    count = 0  #Final output
    #if island_val == k:
    #    count = count + 1
    for i in range(len(s)):
        sub_str = s[0:i+1]
        is_val = substring_search(sub_str, s)
        if is_val == k:
            count = count + 1
    print(count)
if __name__ == '__main__':
    input_str = input()
    input_k = int(input())

    letterIslands(input_str, input_k)
    #result = letterIslands(input_str, input_k)
    #print(result)
