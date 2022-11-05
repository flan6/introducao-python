# Python program to
# demonstrate private members

# Creating a Base class
class Base:
    a = "A"
    _b = "B"
    __c = "C"

    def __init__(self):
        self.a = "GeeksForGeeks A"
        self._b = "GeeksForGeeks B"
        self.__c = "GeeksForGeeks C"

    def _Apresente(self):
        print(self.a)

    def __Apresente(self):
        print(self._b)

# Creating a derived class
class Derived(Base):
    def __init__(self):
        Base.__init__(self)

        print("Calling private member of base class: ")
        print(self._b)

a = Base()
b = Base()

# Aceitavel
if a is not None:
    print(a._Apresente())


# Pythonico
if b:
    print(b.__Apresente())



derivada = Derived()

# print(derivada._b)
