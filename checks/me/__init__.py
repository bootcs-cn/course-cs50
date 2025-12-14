"""
Me check - adapted from cs50/problems/me
"""

from bootcs.check import check, exists as check_exists, run
from bootcs.check import c


@check()
def exists():
    """hello.c exists"""
    check_exists("hello.c")


@check(exists)
def compiles():
    """hello.c compiles"""
    c.compile("hello.c", lcs50=True)


@check(compiles)
def mario():
    """responds to name Mario"""
    run("./hello").stdin("Mario", prompt=False).stdout("[Hh]ello, Mario").exit(0)


@check(compiles)
def peach():
    """responds to name Peach"""
    run("./hello").stdin("Peach", prompt=False).stdout("[Hh]ello, Peach").exit(0)


@check(compiles)
def bowser():
    """responds to name Bowser"""
    run("./hello").stdin("Bowser", prompt=False).stdout("[Hh]ello, Bowser").exit(0)
