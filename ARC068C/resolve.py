def resolve():
    '''
    code here
    '''
    x = int(input())
    if x%11 != 0:
        print((x//11)*2 + (x%11)//7 +1)
    else:
        print((x//11)*2 + (x%11)//7)


if __name__ == "__main__":
    resolve()
