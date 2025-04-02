from random import random
import itertools


class TypeError(Exception):
    "Nipoprawnie podałeś wartości"
    pass


class ZeroDivisionError(Exception):
    "Nie można dzielić przez 0"
    pass


class IndexError(Exception):
    "Znaków jest więcej niż liczb"
    pass


class ZnakError(Exception):
    "Nipoprawnie podałeś znak"
    pass


def calculate(*args, **kwargs):
    if len(args) <= len(kwargs):
        raise IndexError("Znaków jest więcej niż liczb")
    for i in range(0, len(args)):
        if not isinstance(args[i], (int,float)):
            raise TypeError("Nipoprawnie podałeś wartości")
    for key, value in kwargs.items():
        if not isinstance(value, (str)):
            raise TypeError("Nipoprawnie podałeś wartości")
    wynik = args[0]
    list = []
    operators = ["/","*","-","+"]
    for key, value in kwargs.items():
        if not value in operators: # == operators.__contains__(value)
            raise ZnakError("Nipoprawnie podałeś operator")
        list.append(value)
    for i in range(1, len(args)):
        operacja = list[i - 1]
    if operacja == '+':
        wynik += args[i]
    elif operacja == '-':
        wynik -= args[i]
    elif operacja == '*':
        wynik *= args[i]
    elif operacja == '/':
        if args[i] != 0:
            wynik /= args[i]
        else:
            raise ZeroDivisionError("Nie można dzielić przez 0")
    return wynik


# calculate(1,3,2,działanie_1='+',działanie_2=1)#typ args
# calculate("f",3,2,działanie_1='+',działanie_2='-')#typ args
# calculate(3,2,działanie_1='+',działanie_2='-')#Index error
# calculate(3, 2, 0, działanie_1='+', działanie_2='/')  # Divide by 0
# calculate(3, 2,1, działanie_1='%', działanie_2='/')  # niepoprawny operator


class isLista(Exception):
    "Argument is list"
    pass
class ListaIsEmpty(Exception):
    "empty list"
    pass
class BadValuesInList(Exception):
    "value is not int/float/str"
    pass
# zad2
def wszystkie_podzbiory(zbior : set[int, float, str]) -> list[list[int, float, str]]:
    if not isinstance(zbior, set):
        raise isLista("Argument musi miec elementy unikalne")
    for i in zbior:
        if not isinstance(i, (int,float,str)):
            raise BadValuesInList("value is not int/float/str")
    if(len(zbior) == 0):
        raise ListaIsEmpty("The list is empty")


    lista = []
    for i in range(len(zbior) + 1):
        lista.extend(itertools.combinations(zbior, i))
    return lista

print(wszystkie_podzbiory({1, 2, 3}))

def even_numbers(m):
    f = 0
    while f + 2 < m:
        yield f
        f=f+2
# print(even_numbers(11))
for i in even_numbers(11):
    print(i)

