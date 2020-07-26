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
        input = """3 24"""
        output = """2"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """5 1"""
        output = """1"""
        self.assertIO(input, output)

    # def test_入力例_3(self):
    #     input = """1 111"""
    #     output = """111"""
    #     self.assertIO(input, output)

    def test_入力例_4(self):
        input = """4 972439611840"""
        output = """206"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
