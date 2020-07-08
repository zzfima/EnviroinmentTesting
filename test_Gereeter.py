import Greeter


def test_ReturnHello():
    assert Greeter.ReturnHello() == 'Hello my Frined'


def test_ReturnSpecificPersonHello():
    assert Greeter.ReturnSpecificPersonHello('misha') == 'Hello misha'
