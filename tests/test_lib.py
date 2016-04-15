from pp20160412212350 import lib


def test_do_sum():
    import argparse
    args = argparse.Namespace()
    args.number = []
    assert lib.cmdsum.do_sum(args) == 0

    args.number = [1]
    assert lib.cmdsum.do_sum(args) == 1

    args.number = [1, 2]
    assert lib.cmdsum.do_sum(args) == 3


def test_do_copy():
    pass


def test_do_ls():
    pass
