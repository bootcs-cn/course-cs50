"""
Scrabble check - adapted from cs50/problems/scrabble
"""

from bootcs.check import check, exists as check_exists, run
from bootcs.check import c


@check()
def exists():
    """scrabble.c exists"""
    check_exists("scrabble.c")


@check(exists)
def compiles():
    """scrabble.c compiles"""
    c.compile("scrabble.c", lcs50=True)


@check(compiles)
def tie_letter_case():
    """handles letter cases correctly"""
    run("./scrabble").stdin("LETTERCASE").stdin("lettercase").stdout("[Tt]ie!?").exit(0)


@check(compiles)
def tie_punctuation():
    """handles punctuation correctly"""
    run("./scrabble").stdin("Punctuation!?!?").stdin("punctuation").stdout("[Tt]ie!?").exit(0)


@check(compiles)
def test1():
    """correctly identifies 'Question?' and 'Question!' as a tie"""
    run("./scrabble").stdin("Question?").stdin("Question!").stdout("[Tt]ie!?").exit(0)


@check(compiles)
def test2():
    """correctly identifies 'drawing' and 'illustration' as a tie"""
    run("./scrabble").stdin("drawing").stdin("illustration").stdout("[Tt]ie!?").exit(0)


@check(compiles)
def test3():
    """correctly identifies 'hai!' as winner over 'Oh,'"""
    run("./scrabble").stdin("Oh,").stdin("hai!").stdout("[Pp]layer 2 [Ww]ins!?").exit(0)


@check(compiles)
def test4():
    """correctly identifies 'COMPUTER' as winner over 'science'"""
    run("./scrabble").stdin("COMPUTER").stdin("science").stdout("[Pp]layer 1 [Ww]ins!?").exit(0)


@check(compiles)
def test5():
    """correctly identifies 'Scrabble' as winner over 'wiNNeR'"""
    run("./scrabble").stdin("Scrabble").stdin("wiNNeR").stdout("[Pp]layer 1 [Ww]ins!?").exit(0)


@check(compiles)
def test6():
    """correctly identifies 'pig' as winner over 'dog'"""
    run("./scrabble").stdin("pig").stdin("dog").stdout("[Pp]layer 1 [Ww]ins!?").exit(0)


@check(compiles)
def complex_case():
    """correctly identifies 'Skating!' as winner over 'figure?'"""
    run("./scrabble").stdin("figure?").stdin("Skating!").stdout("[Pp]layer 2 [Ww]ins!?").exit(0)
