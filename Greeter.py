class Greeter:
    def PrintHello(self):
        print(self.ReturnHello())

    def PrintSpecificPersonHello(self):
        name = input()
        print(self.ReturnSpecificPersonHello(name))

    def ReturnHello(self):
        return 'Hello my Frined'

    def ReturnSpecificPersonHello(self, name):
        return 'Hello ' + name
