import Greeter
import pytest


def test_ReturnHello():
    assert Greeter.ReturnHello() == 'Hello my Frined'


def test_ReturnSpecificPersonHello1():
    assert Greeter.ReturnSpecificPersonHello('misha') == 'Hello misha'


def test_ReturnSpecificPersonHello2():
    assert Greeter.ReturnSpecificPersonHello('alex') == 'Hello alex'


def test_ReturnSpecificPersonHello3():
    assert Greeter.ReturnSpecificPersonHello('Gogy') == 'Hello Gogy'

# instead of 3 above functions:
@pytest.mark.parametrize(
    'input, expected_output',
    [
        ('Misha', 'Hello Misha'),
        ('Alex', 'Hello Alex'),
        ('Dov', 'Hello Dov'),
        ('Zina', 'Hello Zina')
    ]
)
def test_ReturnSpecificPersonHelloParametrizes(input, expected_output):
    assert Greeter.ReturnSpecificPersonHello(input) == expected_output
