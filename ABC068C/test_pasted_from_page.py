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
        input = """3 2
1 2
2 3"""
        output = """POSSIBLE"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """4 3
1 2
2 3
3 4"""
        output = """IMPOSSIBLE"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """100000 1
1 99999"""
        output = """IMPOSSIBLE"""
        self.assertIO(input, output)

    def test_入力例_4(self):
        input = """5 5
1 3
4 5
2 3
2 4
1 4"""
        output = """POSSIBLE"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
