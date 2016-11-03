
class Wektor(object):  #nazwa klasy w nawiasach (klasy po których nasza klasa dziedziczy)
    # metoda specjalna, inicjalizacja wykonywana przy tworzeniu obiektu (coś jak konstruktor)
    # nie musi jej być
    def __init__(self, lista=[]):
        self.values = lista     #pola naszej klasy
        self.dim = len(lista)   #słowo kluczowe self odnosi się do naszego obiektu (coś jak this w C++)

    # metody klasy
    def dl(self):  #dlugosc wektora
        s=0
        for x in self.values:
            s+=x**2
        return s**(1/2.0)

    # inne metody specjalne
    # dodawanie wektorów
    def __add__(self, w):
        res = [0 for i in self.values]
        for i in range(self.dim):
            res[i] = self.values[i] + w.values[i]
        return Wektor(res)
