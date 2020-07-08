class Greeter:
    def PrintHello(self):
        print(self.PrintHello())

    def PrintSpecificPersonHello(self):
        name = input('What is Your name?')
        print(self.ReturnSpecificPersonHello(name))

    def ReturnHello(self):
        return 'Hello my Frined'

    def ReturnSpecificPersonHello(self, name):
        return 'Hello ' + name
