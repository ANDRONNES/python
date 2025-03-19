# Z1 (0,75 pkt)
# 1A: Wypisz 10 następnych liczb naturalnych od wskazanej liczby (wyłącznie).
# Przykład, number = 5, wyświetl od 5 do 14
from itertools import count

a = input()

for i in range(int(a), 14, 1):
    print(i)


#1B: Napisz program, który będzie zwracał tabliczkę mnożenia dla
# podanej liczby n, jako matryca nxn (patrz pdf).
# Sprawdź czy podana liczba nie jest większa od 20,
# jeżeli jest poproś użytkownika ponownie o podanie liczby.

n = int(input())
if(n >20): print("Podaj liczbe ponownie")
n = int(input())
for i in range(1,int(n) + 1):
    for j in range(1,int(n) + 1):
      print(i*j,end=" ")
    print()


# 1C: Pobierz od użytkownika liczbę (poprzez input) dodaj
# do niej wszystkie liczby w zakresie od 0 do tej liczby.
#Przykład, liczba = 3, wyświetli 6

b = input()
res = 0
for i in range(0, int(b) + 1,1):
    res += i
print(res)

#2B
for i in range(11,0,-1):
    for j in range(i,0,-1):
        print(j, end=" ")
    print()


# 2a
for i in range(11,0,-1):
    for j in range(i,0,-1):
        if j % 5 == 0: print("#", end=" ")
        elif j % 2 == 0: print(-j,end=" ")
        else: print(j , end = " ")
    print()


#z3
n  = 1123712836
# 3a
print(len(str(n)))

# 3b
result = 0
for char in str(n):
    result += 1
print(result)

# z4
z4_inp1 = int(input())
z4_inp2 = int(input())
for i in range(z4_inp1,z4_inp2+1,1):
    if (i == 2): print(i)
    if (i == 3): print(i)
    if (i % 1 == 0 and i % i == 0 and i % 2 != 0 and i % 3 != 0): print(i)
    else: continue
