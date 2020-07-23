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

    def test_入力例1(self):
        input = """3 2
1 2
2 3"""
        output = """2"""
        self.assertIO(input, output)

    def test_入力例2(self):
        input = """3 3
1 2
2 3
2 3"""
        output = """1"""
        self.assertIO(input, output)

    def test_入力例3(self):
        input = """4 4
1 2
2 3
4 1
3 4"""
        output = """3"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
