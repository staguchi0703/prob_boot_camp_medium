def resolve():
    '''
    code here
    collections.Counter()
    dict.values()
    '''
    import collections
    N = int(input())
    A_list = [int(item) for item in input().split()]

    new_list = []

    for item in A_list:
        new_list += [item + i for i in [-1, 0, 1]]

    item_dict = collections.Counter(new_list)
    print(max(item_dict.values()))

if __name__ == "__main__":
    resolve()

    