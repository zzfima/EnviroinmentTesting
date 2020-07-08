from Greeter import Greeter
import pytest
g = Greeter()


def test_ReturnHello():
    assert g.ReturnHello() == 'Hello my Frined'


def test_ReturnSpecificPersonHello1():
    assert g.ReturnSpecificPersonHello('misha') == 'Hello misha'


def test_ReturnSpecificPersonHello2():
    assert g.ReturnSpecificPersonHello('alex') == 'Hello alex'


def test_ReturnSpecificPersonHello3():
    assert g.ReturnSpecificPersonHello('Gogy') == 'Hello Gogy'

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
    assert g.ReturnSpecificPersonHello(input) == expected_output
