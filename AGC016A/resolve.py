def resolve():
    '''
    code here
    '''
    import collections
    s = input()

    N = len(s)

    unique_num_dict = collections.Counter(s)
    most_common = unique_num_dict.most_common()[0]

    if len(unique_num_dict) == 1:
        print(0)
    elif most_common[1] == 1:
        print(N//2)
    else:
        s_set = set(s)
        temp_min_num = 101
        for item in s_set:
            temp_max_num = max([len(item) for item in s.split(item)])
            temp_min_num = min(temp_min_num, temp_max_num)
        print(temp_min_num)
            

if __name__ == "__main__":
    resolve()
