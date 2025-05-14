import math

from pythonProject1.Tutorial6.eighth import lista


class Wielokat:
    def __init__(self,n = 0):
        self.lista = []
        self.n = n
        self.nazwa = ""

    def askNSides(self):
        self.n = int(input())

    def inputSides(self):

        for i in range(self.n):
            self.lista.append(int(input()))
        # a = int(input())
        # b = int(input())

    def dispSides(self):
        for i in range(len(self.lista)):
            print("Bok " + str(i+1) + ": " + str(self.lista[i])+"cm")

    def whatShape(self):

        if self.n == 4:
            a = self.lista[0]
            for i in range(1,len(self.lista)):
                if self.lista[i] == a:
                    continue
                    self.nazwa = "Kwadrat"
                else:
                    print("Nie jest kwadratem")
                    self.nazwa = ""
                    break
        print("Figura jest kwadratem")
        if self.n == 3:
            a = self.lista[0]
            b = self.lista[1]
            c = self.lista[2]
            if(a + c > b and a + b > c and b + c > a):
                print("Figura jest trójkątem")
                self.nazwa = "Trójkąt"
            else:
                print("Nie jest trójkątem")
                self.nazwa = ""
        if self.n > 4:
            print("Wielokąt")
            self.nazwa = "Wielokat"
        if self.n == 2:
            print("Kąt")
            self.nazwa = "Kąt"

    def circuit(self):
        s = 0
        for i in range(self.n):
            s += self.lista[i]
        print("Obwód = " + str(s))





class Kwadrat(Wielokat):
    def __init__(self,a):
        super().__init__(1)
    # def


class Trojkat(Wielokat):
    def __init__(self):
        super().__init__(3)
    def area(self):
        p = super().circuit()/2
        s = math.sqrt(p*(p-lista[0])*p(lista[1])*lista[2])
        print("square = " + str(s))
    def isRight(self):
        sorted(self.lista)
        if self.lista[0]**2 + self.lista[1]**2 == self.lista[2]**2:
            print("Right")








w = Wielokat()
w.askNSides()
w.inputSides()
w.dispSides()