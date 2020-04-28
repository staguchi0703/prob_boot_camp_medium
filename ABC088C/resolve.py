def resolve():
    '''
    code here
    '''

    grid = [[int(i) for i in input().split()] for _ in range(3)]

    is_flag = True

    for i in range(3):
        A = grid[0][i-1] -grid[0][i]
        C = grid[2][i-1] -grid[2][i]
        B = grid[1][i-1] -grid[1][i]

        if  A == B and B == C:
            pass
        else:
            is_flag = False

    print('Yes') if is_flag else print('No')



if __name__ == "__main__":
    resolve()
