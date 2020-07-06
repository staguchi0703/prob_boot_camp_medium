import collections

def resolve():
    '''
    code here
    '''
    s = collections.deque([item for item in input()])
    que = collections.deque()

    while s:
        try:
            temp = s.popleft()
            if temp == 'B':
                que.pop()
            else:
                que.append(temp)
        except:
            pass

    print(''.join(list(que)))


if __name__ == "__main__":
    resolve()
