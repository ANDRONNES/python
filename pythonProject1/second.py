
scores = {"Ania" : [101, 75, 33],
                 "Kasia" :[76, 55, 12],
                 "Bartek": [65, 55, 60],
                 "Marek" : [23, 80, 98]}

for key, value in scores.items():
    for val in value:
        if val > 100: scores[key].remove(val)

print (scores)

avg = 0
average_score = dict()
for key, value in scores.items():
    avg = 0
    for val in value:
        avg += val
    avg/=len(value)
    average_score.update({key:avg})
print(average_score)
for value in average_score.values():
    if value == max(average_score.values()):
        imie = key
print("Najwyższą średnią uzyskał/ła ",imie," , która wynosiła " , max(average_score.values()))



# Zadanie 2 (0,5 pkt)
# Napisz kod, który wyświetli słowa z listy, które są ,,podobne" do napisu s
# w tym sensie, że składające się z tych samych znaków — ale ewentualnie występujących inną liczbę razy.
#PRZYKŁAD
# s = 'one'
# lista = ['one', 'two', 'none', 'three', 'neon', 'eon']
# >> none neon eon

s = 'one'
lista = ['one', 'two', 'none', 'three', 'neon', 'eon']
for string in lista:
    if set(string) == set(s) : print(string)


# Zadanie 3 (1,5 pkt)
# Napisz program, który umożliwia zarządzanie książką adresową. Program powinien umożliwiać użytkownikowi wykonywanie następujących operacji:
#
# Dodawanie nowego kontaktu do książki adresowej.
# Wyświetlanie wszystkich kontaktów z książki adresowej.
# Wyszukiwanie kontaktu po nazwie i wyświetlanie szczegółów.
# Usuwanie kontaktu z książki adresowej.
#
# Użyj słownika, gdzie kluczem będzie nazwa kontaktu, a wartością będzie lista informacji o kontakcie (np. imię, nazwisko, numer telefonu).


contactBook = {"żona" : ["Ania","Ml",342672387],
                 "siostra" :["Kasia","Bdfs",478214672],
                 "brat": ["Bartek","fhsuh",238772333],
                 "Marek" : ["Marek","fskhdf",346772783]}



def addToContactBook(nickname,numer):
    contactBook.update({nickname:[numer]})

def showAllContacts():
    print(contactBook)

def searchByNickname(nickname):
    for k,v in contactBook.items():
        if k == nickname:
            print(v)
def deleteByNickname(nickname):
        if nickname in contactBook:
             del contactBook[nickname]

addToContactBook("sjak",147829182)
print(contactBook)
deleteByNickname("sjak")
print(contactBook)
searchByNickname("sjak")
showAllContacts()



































