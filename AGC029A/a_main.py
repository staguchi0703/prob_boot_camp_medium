# %%
# VScodeで入力をテキストから読み込んで標準入力に渡す
import sys
import os

file_path = __file__.rsplit('/',1)[0]
f=open(file_path + '/input.txt', 'r', encoding="utf-8")
# inputをフルパスで指定
# win10でファイルを作るとs-jisで保存されるため、読み込みをutf-8へエンコードする必要あり
# VScodeでinput file開くとutf8になってるんだけど中身は結局s-jisになっているらしい
sys.stdin=f

#
# 入力スニペット
# num = int(input())
# num_list = [int(item) for item in input().split()]
# num_list = [input() for _ in range(3)]
##################################
# %%
# 以下ペースト可


def resolve():
    '''
    code here
    '''
    S = [item for item in input()]
    rev_S = S[::-1]
    print(S)
    if len(S) >= 2:
        prev = S[-1]
        cnt = 0
        is_search = True

        while is_search:
            is_break = False
            for i, s in enumerate(rev_S):
                print(i,s,cnt)
                if s == 'B' and prev == 'W':
                    rev_S[i] = 'W'
                    rev_S[i-1] = 'B'
                    cnt += 1
                    is_break = True
                    break
                else:
                    prev = s
                    
            if is_break:
                is_break = False
            else:
                is_search = False
    else:
        cnt = 0

    print(cnt)


if __name__ == "__main__":
    resolve()
