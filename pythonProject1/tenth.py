import math


def decoraator(function):
    def opakownie(self):
        if function(self) is None:
            print("Brak rozwiązań")
        elif isinstance(function(self), tuple):
            if (function(self)[0] == function(self)[1]):
                print("Jedno rozwiązanie")
            else:
                print("Wiele rozwiązań")
        return function(self)

    return opakownie


class FunkcjaKwadratowa:
    def __init__(self, a=None, b=None, c=None):
        if a is None:
            a = input()
        if b is None:
            b = input()
        if c is None:
            c = input()

        self.a = a
        self.b = b
        self.c = c

    @decoraator
    def Rozwiaz(self):
        r = self.b ** 2 - 4 * self.a * self.c
        if (r < 0):
            return None
        elif (r == 0):
            x = (-self.b) / (2 * self.a)
            return (x, x)
        else:
            x1 = (-self.b + math.sqrt(r)) / (2 * self.a)
            x2 = (-self.b - math.sqrt(r)) / (2 * self.a)
            return (x1, x2)

    @property
    def a(self):
        return self._a

    @a.setter
    def a(self, value):
        try:
            value = float(value)
        except ValueError:
            raise ValueError("Współczynnik 'a' musi być liczbą")
        if value == 0:
            raise ValueError("Współczynnik 'a' nie może być zerem")
        self._a = value

    @property
    def b(self):
        return self._b

    @b.setter
    def b(self, value):
        try:
            value = float(value)
        except ValueError:
            raise ValueError("Współczynnik 'a' musi być liczbą")
        if value == 0:
            raise ValueError("Współczynnik 'a' nie może być zerem")
        self._b = value

    @property
    def c(self):
        return self._c

    @c.setter
    def c(self, value):
        try:
            value = float(value)
        except ValueError:
            raise ValueError("Współczynnik 'a' musi być liczbą")
        if value == 0:
            raise ValueError("Współczynnik 'a' nie może być zerem")
        self._c = value


    def __add__(self, innaFunkcjaKwadratowa):
        if not isinstance(innaFunkcjaKwadratowa, FunkcjaKwadratowa):
            raise TypeError("Niepoprawny typ")
        return FunkcjaKwadratowa(self.a + innaFunkcjaKwadratowa.a, self.b + innaFunkcjaKwadratowa.b,
                                 self.c + innaFunkcjaKwadratowa.c)

    def __sub__(self, innaFunkcjaKwadratowa):
        if not isinstance(innaFunkcjaKwadratowa, FunkcjaKwadratowa):
            raise TypeError("Niepoprawny typ")
        return FunkcjaKwadratowa(self.a - innaFunkcjaKwadratowa.b, self.b - innaFunkcjaKwadratowa.b,
                                 self.c - innaFunkcjaKwadratowa.c)

    def Nalezy(self, koordynaty):
        if not isinstance(koordynaty, tuple):
            return None
        x = koordynaty[0]
        y = koordynaty[1]

        if (y == self.a * (x ** 2) + self.b * x + self.c):
            return 1
        else:
            return 0


FK = FunkcjaKwadratowa()
FK1 = FunkcjaKwadratowa()

NEWF = FK + FK1
print(NEWF)
newf = FK - FK1
print(newf)