def resolve():
    '''
    code here
    '''
    import string
    S = [item for item in input()]
    temp_abc = [item for item in string.ascii_lowercase]

    if len(S) < 26:
        for item in S:
            temp_abc.remove(item)
        res = ''.join(S) + temp_abc[0] 

    else:
        if S == temp_abc[::-1]:
            res = -1
        else:
            tail_inorder = []
            prev = 'a'
            cnt = 0
            for item in S[::-1]:
                if item >= prev:
                    tail_inorder += [item]
                    cnt += 1
                else:
                    break
                prev = item
            end_letter = S[-1*(cnt+1)]
            tail_inorder.sort()
            for item in tail_inorder:
                if end_letter < item:
                    res_end_letter = item
                    break

            res = S[:-1*(cnt+1)] + [res_end_letter]
    print(''.join(res)) if res != -1 else print(res)

if __name__ == "__main__":
    resolve()
