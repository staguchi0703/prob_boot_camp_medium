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
        self.assertEqual(out, output)
    def test_入力例_1(self):
        input = """2 4
0 3"""
        output = """7"""
        self.assertIO(input, output)
    def test_入力例_2(self):
        input = """2 4
0 5"""
        output = """8"""
        self.assertIO(input, output)
    def test_入力例_3(self):
        input = """4 1000000000
0 1000 1000000 1000000000"""
        output = """2000000000"""
        self.assertIO(input, output)
    def test_入力例_4(self):
        input = """1 1
0"""
        output = """1"""
        self.assertIO(input, output)
    def test_入力例_5(self):
        input = """9 10
0 3 5 7 100 110 200 300 311"""
        output = """67"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()