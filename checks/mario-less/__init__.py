"""
Mario Less check - adapted from cs50/problems/mario/less
"""

from bootcs.check import check, exists, run, include, Mismatch
from bootcs.check import c


@check()
def file_exists():
    """mario.c exists"""
    exists("mario.c")
    include("1.txt", "2.txt", "8.txt", "12.txt")


@check(file_exists)
def compiles():
    """mario.c compiles"""
    c.compile("mario.c", lcs50=True)


@check(compiles)
def test_reject_negative():
    """rejects a height of -1"""
    run("./mario").stdin("-1").reject()


@check(compiles)
def test0():
    """rejects a height of 0"""
    run("./mario").stdin("0").reject()


@check(compiles)
def test1():
    """handles a height of 1 correctly"""
    out = run("./mario").stdin("1").stdout()
    check_pyramid(out, open("1.txt").read())


@check(compiles)
def test2():
    """handles a height of 2 correctly"""
    out = run("./mario").stdin("2").stdout()
    check_pyramid(out, open("2.txt").read())


@check(compiles)
def test8():
    """handles a height of 8 correctly"""
    out = run("./mario").stdin("8").stdout()
    check_pyramid(out, open("8.txt").read())


@check(compiles)
def test9():
    """rejects a height of -1, and then accepts a height of 2"""
    out = run("./mario").stdin("-1").reject().stdin("2").stdout()
    check_pyramid(out, open("2.txt").read())


@check(compiles)
def test_reject_foo():
    """rejects a non-numeric height of "foo" """
    run("./mario").stdin("foo").reject()


@check(compiles)
def test_reject_empty():
    """rejects a non-numeric height of "" """
    run("./mario").stdin("").reject()


def check_pyramid(output, correct):
    if output == correct:
        return

    output_lines = [line for line in output.splitlines() if line != ""]
    correct_lines = correct.splitlines()

    help_msg = None
    if len(output_lines) == len(correct_lines):
        if all(ol.rstrip() == cl for ol, cl in zip(output_lines, correct_lines)):
            help_msg = "did you add too much trailing whitespace to the end of your pyramid?"
        elif all(ol[1:] == cl for ol, cl in zip(output_lines, correct_lines)):
            help_msg = "are you printing an additional character at the beginning of each line?"

    raise Mismatch(correct_lines, output_lines, help=help_msg)
