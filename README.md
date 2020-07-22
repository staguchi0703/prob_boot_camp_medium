# 解法のメモ

## [ABC131C](https://atcoder.jp/contests/abc131/tasks/abc131_c)

### 方針

* Cの倍数とDの倍数以外の数の個数は？
  * 全体からCの倍数の数とDの倍数の数を引く
  * Cの倍数かつDの倍数を二回引いてしまっているから減らす必要がある
    * ドモルガンの法則
  * Cの倍数かつDの倍数はC*Dの倍数でなく、CとDの最小公倍数の倍数
    * 最小公倍数　the least common multiple(LCM)
    * $lcm = C \cdot D/gcd(C, D)$
* 範囲に含むとき含まないとき、下限が境界の時で場合分けも必要


## [ABC117C-Streamline](https://atcoder.jp/contests/abc117/tasks/abc117_c)

### 方針

 * 近い座標の集団は同じ個まで処理する
 * 遠い座標は異なるコマで処理する
   * ちがうコマとの間に仕切りをいれる考え方
 * 距離を調べるために、座標群をsortしてから隣との差をとる
 * 差が大きい順に仕切りの数だけ排除する
   * M-N個残す
   * N-1個大きいものを削除するでも正しい場合が多いが、M-Nが1になるとスライスがおかしくなるのでM-N個残すでスライスする。

## [ABC130C-Rectangle Cutting](https://atcoder.jp/contests/abc130/tasks/abc130_c)

* 半分をn//2とすると、3//2と2//2が同じになってしまう
* 半分の整数を巧く表すには、**二倍と等しい**と考える


## [ARC093C-Traveling Plan](https://atcoder.jp/contests/arc093/tasks/arc093_a)

### 方針

* 距離の累積和を利用する
  * もし要素が一つなくなると・・・
    * 無くなったものがあったとして、ひとつづつ飛ぶと、`abs(A[i] - A[i+1]) + abs(A[i+1] - A[i+2])`
    * 無くなった物を飛ばして飛ぶと`abs(A[i] - A[i+2])`
    * 上記の差を累積和から引くと答えになる

## ちょこっとメモ

```
import itertools

comb = itertools.combinations(list, 組み合わせの数)
```

```
comb = [
  (a, b, c),
  (a, c, d),
  .......
]
```

## [AGC022A](https://atcoder.jp/contests/agc022/tasks/agc022_a)

### 解法
* 激ムズなんですけど・・・
* 文字数が26未満は出てていない文字の最小を加える
* 文字数26のときは最後尾の後ろから逆順にならんでいる塊を見つけて削除
  * 残った塊の最後の文字を消して、削除した塊の中にある文字で残った塊から消した文字より大きい一番小さいものを見つける。