def resolve():
    '''
    code here
    '''
    import collections
    import math
    N = int(input())
    Ss = [sorted([item for item in input()]) for _ in range(N)]
    
    sss = []
    for line in Ss:
        sss.append(''.join(line))
    line_cnt = collections.Counter(sss)

    cnt = 0
    for letter, num in line_cnt.most_common():
        if num >=2:
            cnt += math.comb(num, 2)

    print(cnt)
if __name__ == "__main__":
    resolve()
