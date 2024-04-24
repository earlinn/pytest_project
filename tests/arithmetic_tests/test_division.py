import pytest


def division(a: int, b: int) -> int:
    return a // b


@pytest.mark.parametrize("a, b, result", ((10, 2, 5), (-20, 5, -4), (0, 100, 0)))
def test_success(a, b, result):
    assert division(a, b) == result


def test_zero_division():
    with pytest.raises(ZeroDivisionError):
        division(5, 0)


def test_with_fixture(return_10):
    assert division(100, 10) == return_10
