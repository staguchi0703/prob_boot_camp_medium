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
