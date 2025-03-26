import statistics


def calculate(*args, **kwargs):
    wynik = args[0]
    list = []
    for key, value in kwargs.items():
        list.append(value)
    for i in range(1, len(args)):
        operacja = list[i-1]
        if operacja == '+':
            wynik += args[i]
        elif operacja == '-':
            wynik -= args[i]
        elif operacja == '*':
            wynik *= args[i]
        elif operacja == '/':
            if args[i] != 0:
                wynik /= args[i]
    return wynik

print(calculate(1,3,2,działanie_1='+',działanie_2='-'))
print(calculate(1, 2, 3, działanie_1='+', działanie_2='+', działanie_3='+'))



def calculate_statistics(operation,*args):
    result = 0
    if operation=="mean":
        for i in range(len(args)):
            result += args[i]
        return result/len(args)
    if operation=="median":
        if len(args)%2 == 0:
            return args[int(len(args)/2)]
        else:
            return args[int(len(args)+1/2)]
    if operation=="mode":
        return statistics.mode(args)




print(calculate_statistics("mean", 1, 2, 3, 4, 5))  # 3.0
print(calculate_statistics("median", 1, 2, 3, 4, 5,6,7,8))  # 3
print(calculate_statistics("mode", 1, 2, 2, 3, 3, 3))  # [3]



def validate_pesel(pesel):
    suma_kontrolna = 0
    if len(pesel) != 11:
        return False
    weights = [1, 3, 7, 9, 1, 3, 7, 9, 1, 3]
    for i in range(10):
        suma_kontrolna += int(pesel[i]) * weights[i]
    lastDigit = (10 - (suma_kontrolna % 10)) % 10
    return lastDigit == int(pesel[-1])


print(validate_pesel('12345678901'))  # False
print(validate_pesel('44051401458'))  # True







