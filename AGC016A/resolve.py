def resolve():
    '''
    code here
    '''
    import collections
    s = input()

    N = len(s)

    unique_num_dict = collections.Counter(s)
    most_common = unique_num_dict.most_common()[0]

    if most_common[1] == 1:
        print(N//2)
    else:
        temp_list = s.strip(most_common[0])
        res = 0
        for item in temp_list:
            res = max(res, len(item))
        print(res)
if __name__ == "__main__":
    resolve()
