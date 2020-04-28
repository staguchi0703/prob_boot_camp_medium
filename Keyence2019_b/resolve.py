def resolve():
    '''
    code here
    '''

    S = input()

    is_flag = False
    key = 'keyence'

    for i in range(8):
        if i == 0:
            if S[-7:] == key:
                is_flag = True

        elif 1 <= i < 7:
            if S[:i] == key[:i] and S[-1*(7-i):] == key[-1*(7-i):]:
                is_flag = True
        else:
            if S[:7] == key:
                is_flag = True

    print('YES') if is_flag else print('NO') 


if __name__ == "__main__":
    resolve()
