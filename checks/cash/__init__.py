"""
Cash check - adapted from cs50/problems/cash
"""

from bootcs.check import check, exists, run
from bootcs.check import c


@check()
def file_exists():
    """cash.c exists"""
    exists("cash.c")


@check(file_exists)
def compiles():
    """cash.c compiles"""
    c.compile("cash.c")


@check(compiles)
def test041():
    """input of 41 yields output of 4"""
    run("./cash").stdin("41").stdout(coins(4), "4\n").exit(0)


@check(compiles)
def test001():
    """input of 1 yields output of 1"""
    run("./cash").stdin("1").stdout(coins(1), "1\n").exit(0)


@check(compiles)
def test015():
    """input of 15 yields output of 2"""
    run("./cash").stdin("15").stdout(coins(2), "2\n").exit(0)


@check(compiles)
def test160():
    """input of 160 yields output of 7"""
    run("./cash").stdin("160").stdout(coins(7), "7\n").exit(0)


@check(compiles)
def test230():
    """input of 2300 yields output of 92"""
    run("./cash").stdin("2300").stdout(coins(92), "92\n").exit(0)


@check(compiles)
def test_reject_negative():
    """rejects a negative input like -1"""
    run("./cash").stdin("-1").reject()


def coins(num):
    """regex that matches `num` not surrounded by any other numbers"""
    return fr"(?<!\d){num}(?!\d)"
