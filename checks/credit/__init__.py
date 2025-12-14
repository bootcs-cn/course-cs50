"""
Credit check - adapted from cs50/problems/credit
信用卡号验证（Luhn算法）
"""

from bootcs.check import check, exists as check_exists, run
from bootcs.check import c


@check()
def exists():
    """credit.c exists"""
    check_exists("credit.c")


@check(exists)
def compiles():
    """credit.c compiles"""
    c.compile("credit.c", lcs50=True)


def _test_credit_card(card_number, expected_output):
    """Helper function to test credit card validation"""
    run("./credit").stdin(card_number).stdout(expected_output).exit(0)


@check(compiles)
def test1():
    """identifies 378282246310005 as AMEX"""
    _test_credit_card("378282246310005", "AMEX")


@check(compiles)
def test2():
    """identifies 371449635398431 as AMEX"""
    _test_credit_card("371449635398431", "AMEX")


@check(compiles)
def test3():
    """identifies 5555555555554444 as MASTERCARD"""
    _test_credit_card("5555555555554444", "MASTERCARD")


@check(compiles)
def test4():
    """identifies 5105105105105100 as MASTERCARD"""
    _test_credit_card("5105105105105100", "MASTERCARD")


@check(compiles)
def test5():
    """identifies 4111111111111111 as VISA"""
    _test_credit_card("4111111111111111", "VISA")


@check(compiles)
def test6():
    """identifies 4012888888881881 as VISA"""
    _test_credit_card("4012888888881881", "VISA")


@check(compiles)
def test7():
    """identifies 4222222222222 as VISA"""
    _test_credit_card("4222222222222", "VISA")


@check(compiles)
def test8():
    """identifies 1234567890 as INVALID"""
    _test_credit_card("1234567890", "INVALID")


@check(compiles)
def test9():
    """identifies 369421438430814 as INVALID"""
    _test_credit_card("369421438430814", "INVALID")


@check(compiles)
def test10():
    """identifies 4062901840 as INVALID"""
    _test_credit_card("4062901840", "INVALID")


@check(compiles)
def test11():
    """identifies 5673598276138003 as INVALID"""
    _test_credit_card("5673598276138003", "INVALID")


@check(compiles)
def test12():
    """identifies 4111111111111113 as INVALID"""
    _test_credit_card("4111111111111113", "INVALID")


@check(compiles)
def test13():
    """identifies 4222222222223 as INVALID"""
    _test_credit_card("4222222222223", "INVALID")


@check(compiles)
def test14():
    """identifies 3400000000000620 as INVALID"""
    _test_credit_card("3400000000000620", "INVALID")


@check(compiles)
def test15():
    """identifies 430000000000000 as INVALID"""
    _test_credit_card("430000000000000", "INVALID")
