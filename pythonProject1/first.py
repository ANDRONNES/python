#1
a = 2**(1/2)
b = a**2
c = (b-2)/2
print(c)

#2
print("Czesć, jak masz na imię?")
imie = input()
print("Miło Cię poznać, " +imie)

#3
print("Czesć, user!")
print("Wprowadź liczbę całkowitą ")
num = input()
if(int(num)%7 == 0):
    print("liczba jest podzielna przez 7")
else:
    print("liczba nie jest podzielna przez 7")


#4
print("Wprowadź 3 liczby całkowite ")
A = input()
B = input()
C = input()

#Ax^2 + Bx + C = 0
#b^2-4ac = 0 ->1
if(int(B)**2 - 4*int(A)*int(C) == 0):
    print("Jedno rozwiązanie")
elif(int(B)**2 - 4*int(A)*int(C) > 0):
    print("Są dwa rozwiązania")
else:
    print("Brak rozwiązań")


#5
print("Podaj swój wiek lub wiek koledzy(w latach)")
wiek = int(input())
if(wiek < 0): print("Nieprawidłowy wiek")
elif(wiek == 0):print("niemowlę")
elif(wiek > 0 and wiek < 18):print("dziecko")
elif(wiek >= 18 and wiek <=120):print("dorosły")
elif(wiek >120):print("ludzie tyle nie żyją")