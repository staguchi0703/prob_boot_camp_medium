#
from resolve import resolve
####################################
####################################
# 以下にプラグインの内容をペーストする
#  
import sys
from io import StringIO
import unittest


class TestClass(unittest.TestCase):
    def assertIO(self, input, output):
        stdout, stdin = sys.stdout, sys.stdin
        sys.stdout, sys.stdin = StringIO(), StringIO(input)
        resolve()
        sys.stdout.seek(0)
        out = sys.stdout.read()[:-1]
        sys.stdout, sys.stdin = stdout, stdin
        print('------------')
        print(out)
        print('------------')
        self.assertEqual(out, output)

    def test_入力例_1(self):
        input = """3
3 5 -1"""
        output = """12
8
10"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """5
1 1 1 2 0"""
        output = """4
4
4
2
4"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """6
-679 -2409 -3258 3095 -3291 -4462"""
        output = """21630
21630
19932
8924
21630
19288"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
