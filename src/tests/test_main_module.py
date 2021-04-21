from demo import fibonacci as fibonacci
import pytest


@pytest.mark.parametrize("n,expected", [
    (1, 1),
    (2, 2),
    (3, 3),
    (4, 5),
])
def test_fibonacci_main_use_case(n, expected):
    assert fibonacci(n) == expected


def test_fibonacci_nagative():
    with pytest.raises(ValueError):
        fibonacci(-1)


def test_fibonacci_types():
    with pytest.raises(TypeError):
        fibonacci("Bonjour")

    with pytest.raises(TypeError):
        fibonacci(1.2)