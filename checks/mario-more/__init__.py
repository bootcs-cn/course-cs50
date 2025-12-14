"""
Mario (More) check - adapted from cs50/problems/mario/more
双侧金字塔版本
"""

from bootcs.check import check, exists as check_exists, run, include, Mismatch
from bootcs.check import c


@check()
def exists():
    """mario.c exists"""
    check_exists("mario.c")
    include("1.txt", "2.txt", "8.txt", "12.txt")


@check(exists)
def compiles():
    """mario.c compiles"""
    c.compile("mario.c", lcs50=True)


@check(compiles)
def test_reject_negative():
    """rejects a height of -1"""
    run("./mario").stdin("-1", prompt=False).reject()


@check(compiles)
def test0():
    """rejects a height of 0"""
    run("./mario").stdin("0", prompt=False).reject()


@check(compiles)
def test1():
    """handles a height of 1 correctly"""
    run("./mario").stdin("1").stdout("#  #").exit(0)


@check(compiles)
def test2():
    """handles a height of 2 correctly"""
    run("./mario").stdin("2").stdout(" #  #").stdout("##  ##").exit(0)


@check(compiles)
def test8():
    """handles a height of 8 correctly"""
    run("./mario").stdin("8").stdout("       #  #").stdout("########  ########").exit(0)


@check(compiles)
def test9():
    """rejects a height of -1, and then accepts a height of 2"""
    run("./mario").stdin("-1").reject().stdin("2").stdout(" #  #").stdout("##  ##").exit(0)


@check(compiles)
def test_reject_foo():
    """rejects a non-numeric height of "foo" """
    run("./mario").stdin("foo", prompt=False).reject()


@check(compiles)
def test_reject_empty():
    """rejects a non-numeric height of "" """
    run("./mario").stdin("", prompt=False).reject()


def check_pyramid(output, correct):
    if output == correct:
        return

    output = [line for line in output.splitlines() if line != ""]
    correct = correct.splitlines()

    help = None
    if len(output) == len(correct):
        if all(ol.rstrip() == cl for ol, cl in zip(output, correct)):
            help = "did you add too much trailing whitespace to the end of your pyramid?"
        elif all(ol[1:] == cl for ol, cl in zip(output, correct)):
            help = "are you printing an additional character at the beginning of each line?"

    raise Mismatch(correct, output, help=help)
