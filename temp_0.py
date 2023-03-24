import inspect

class Foo:
    def getVarName(self):
        for i in inspect.currentframe().f_back.f_locals.items():
            print(i)
            if id(self) == id(i[1]):
                return i[0]


if __name__ == '__main__':
    x = Foo()
    x1 = Foo()
    x2 = Foo()

    print(x.getVarName())
    print(x1.getVarName())
    print(x2.getVarName())