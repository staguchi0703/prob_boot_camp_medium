def resolve():
    '''
    code here
    '''
    import collections
    n = int(input())
    vs = [int(item) for item in input().split()]
    num_max = max(vs)

    cnt_od = collections.Counter(vs[::2])
    cnt_ev = collections.Counter(vs[1::2])

    cnt_od = cnt_od.most_common()
    cnt_ev = cnt_ev.most_common()

    if cnt_od[0][0] == cnt_ev[0][0]:
        if (len(cnt_od)>1) and (len(cnt_ev)>1):
            ans = min(n - cnt_od[1][1] - cnt_ev[0][1], n - cnt_od[0][1] - cnt_ev[1][1])
        elif len(cnt_od) > 1:
            ans = n//2 - cnt_od[1][1]
        elif len(cnt_ev) > 1:
            ans = n//2 - cnt_ev[1][1]
        else:
            ans = n//2
    else:
        ans = n - cnt_ev[0][1] - cnt_od[0][1]

    print(ans)
if __name__ == "__main__":
    resolve()
