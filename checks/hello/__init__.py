"""
Hello check - adapted from cs50/problems/hello
"""

from bootcs.check import check, exists, run
from bootcs.check import c


@check()
def file_exists():
    """hello.c exists"""
    exists("hello.c")


@check(file_exists)
def compiles():
    """hello.c compiles"""
    c.compile("hello.c", lcs50=True)


@check(compiles)
def emma():
    """responds to name Emma"""
    run("./hello").stdin("Emma", prompt=True).stdout("Emma").exit(0)


@check(compiles)
def rodrigo():
    """responds to name Rodrigo"""
    run("./hello").stdin("Rodrigo", prompt=True).stdout("Rodrigo").exit(0)
