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
    c.compile("hello.c")


@check(compiles)
def prints_hello():
    """prints hello"""
    # 简化版：只检查输出包含 hello
    run("./hello").stdout("[Hh]ello").exit(0)
