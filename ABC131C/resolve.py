def resolve():
    '''
    code here
    '''
    import math
    A, B, C, D = [int(item) for item in input().split()]

    if B//C == 0:
        num_C = 0
    elif B//C >= 1 and A % C == 0:
        num_C = B // C - A //C + 1
    elif B//C >= 1 and A % C != 0: 
        num_C = B // C - A //C
    else:
        num_C = B // C

    if B//D == 0:
        num_D = 0
    elif B//D >= 1 and A % D == 0:
        num_D = B // D - A //D + 1
    elif  B//D >= 1 and A % D != 0:
        num_D = B // D - A //D
    else:
        num_D = B // D

    lcm = C * D // math.gcd(C, D)
    if B//lcm == 0:
        num_CD = 0
    elif B//lcm > 1 and A  % lcm == 0:
        num_CD = B // lcm - A //lcm + 1
    elif B//lcm > 1 and A  % lcm != 0:
        num_CD = B // lcm - A //lcm
    else:
        num_CD = B // lcm

    # print(num_C, num_D, num_CD)
    print(B - A + 1 - (num_C + num_D - num_CD))


if __name__ == "__main__":
    resolve()
