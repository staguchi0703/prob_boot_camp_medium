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
    N = int(input())
    S = input()

    # res = 0
    # for i in range(1, N):
    #     A = set(S[:i])
    #     B = set(S[i:])

    #     res = max(res, len(A * B))

    # print(res)

    A = set(S[:3])
    B = set(S[3:])

    print(A & B)

if __name__ == "__main__":
    resolve()