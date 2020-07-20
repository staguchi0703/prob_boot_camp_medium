def resolve():
    '''
    code here
    '''
    import string
    S = input()

    if S == "zyxwvutsrqponmlkjihgfedcba":
        print(-1)
    else:
        if len(S) < 26:
            temp_str = [item for item in string.ascii_lowercase]
            for item in S:
                temp_str.remove(item)
            print(S+temp_str[0])
            
        else:
            res_s = S[0]
            temp_str = [item for item in string.ascii_lowercase]
            temp_str.remove(S[0])
            for i in range(1,26):
                if ord(S[i-1]) + 1 < ord(S[i]):
                    break
                
                temp_str.remove(S[i])
                res_s += S[i]
            else:
                res_s = res_s[:-1]
                temp_str = 'z'


            print(res_s[:-1] + temp_str[0])


if __name__ == "__main__":
    resolve()
