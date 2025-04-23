import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from pandas.core.interchange import column

x = np.linspace(0, 10, 100)
y1 = 2 * x + 1
y2 = x ** 2 - 3 * x + 2

plt.scatter(x, y1, color="green")
plt.plot(x, y2)
plt.title("Functions")
plt.xlabel("x")
plt.ylabel("y")
plt.legend(["Funkcja liniowa", "Funkcja kwadratowa"])
plt.grid(True)
plt.show()

# z2
uczniowie = ['Anna', 'Bartek', 'Cezary', 'Daria', 'Ela']
matematyka = [78, 88, 95, 72, 80]
fizyka = [85, 79, 92, 68, 82]
chemia = [92, 85, 88, 74, 78]

fix, axs = plt.subplots(1, 3, figsize=(11, 11))
axs[0].bar(uczniowie, matematyka)
axs[0].set_title("Oceny z matematyki")
axs[0].set_xlabel("Uczniowie")
axs[0].set_ylabel("Oceny")
axs[1].bar(uczniowie, fizyka)
axs[1].set_title("Oceny z fizyki")
axs[1].set_xlabel("Uczniowie")
axs[1].set_ylabel("Oceny")
axs[2].bar(uczniowie, chemia)
axs[2].set_title("Oceny z chemii")
axs[2].set_xlabel("Uczniowie")
axs[2].set_ylabel("Oceny")
plt.show()

# z3

df = pd.read_excel(
    "..\\Dane_Pandas.xlsx",
    # sheet_name="Arkusz1",
    usecols=["Imie", "Pon", "Wt", "Śr", "Czw", "Pt", "Sob", "Nd"],
    dtype={"Imie": "string", "Pon": int, "Wt": int, "Śr": int, "Czw": int, "Pt": int, "Sob": int, "Nd": int},
    na_values=["-",0,0,0,0,0,0,0]
)
print(df)

# plt.plot(x = dzien tygodnia, y = liczba krokow)
plt.show()
days = df[1:1].columns
print(days)
for index, row in df.iterrows():
    day = row.name
    imie = row['Imie']
    steps = row[1:].values
    print(imie, steps)
lista = df.columns.tolist()
lista.remove('Imie')
print(lista)


plt.plot()

