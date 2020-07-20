def resolve():
    '''
    code here
    '''
    import math
    N, M = [int(item) for item in input().split()]
    S = input()
    T = input()

    res = N * M // math.gcd(N,M)

    cycle_s = res // N
    cycle_t = res // M
    cycle_overlap = cycle_s * cycle_t // math.gcd(cycle_s, cycle_t)

    for i in range(res//cycle_overlap):        
        if T[i*cycle_overlap//cycle_t] == S[i*cycle_overlap//cycle_s]:
            pass
        else:
            res = -1
            break

    print(res)

if __name__ == "__main__":
    resolve()
