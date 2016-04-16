import unittest

from pp20160412212350 import lib


class TestLib(unittest.TestCase):
    def test_do_sums(self):
        import argparse
        args = argparse.Namespace()
        args.number = []
        assert lib.cmdsum.do_sum(args) == 0

        args.number = [1]
        assert lib.cmdsum.do_sum(args) == 1

        args.number = [1, 2]
        assert lib.cmdsum.do_sum(args) == 3

    def test_do_copy(self):
        pass

    def test_do_ls(self):
        pass

if __name__ == '__main__':
    unittest.main()
