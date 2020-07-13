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
* 