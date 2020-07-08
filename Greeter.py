def PrintHello():
    print(PrintHello())


def PrintSpecificPersonHello():
    name = input('What is Your name?')
    print(ReturnSpecificPersonHello(name))


def ReturnHello():
    return 'Hello my Frined'


def ReturnSpecificPersonHello(name):
    return 'Hello ' + name
