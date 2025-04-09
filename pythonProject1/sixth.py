import os
import shutil
import datetime
import string

# 1
dir = "Tutorial6"
if not os.path.exists(dir):
    os.makedirs(dir)


file1 = "dzis.txt"
with open(file1, "w") as file:
    file.write(datetime.datetime.today().strftime("%d.%m.%Y"))
    file.close()

file_folder_path = os.path.join(dir, "dzis.txt")
if os.path.exists(file_folder_path):
    os.remove(file_folder_path)
    shutil.move(file1, file_folder_path)

lista = []
for i in range(1, -16, -1):
    lista.append(i)

with open("Tutorial6/liczby.txt", "a") as file:
    for i in lista:
        file.write(str(i) + "\n")
    file.close()

with open("Tutorial6/liczby_parzyste.txt", "w") as file:
    for i in lista:
        if (i % 2 == 0): file.write(str(i) + "\n")
    file.close()

with open("Tutorial6/liczby_nieparzyste.txt", "w") as file:
    for i in lista:
        if (i % 2 != 0): file.write(str(i) + "\n")
    file.close()

print(os.listdir("Tutorial6"))


#2
def policz_wystąpienia(pathToFile: str) -> dict[str : int]:
    mapa = {}

    with open(pathToFile, "r") as file:
        text = file.read()

    for char in string.punctuation:
        text = text.replace(char, "")

    wordsArray = text.split()

    for word in wordsArray:
        if word in mapa:
            mapa[word] += 1
        else:
            mapa[word] = 1

    return mapa

print(policz_wystąpienia("test.txt"))

