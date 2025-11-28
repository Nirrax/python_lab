class Prostokat:
    def __init__(self, szerokosc, wysokosc):
        if szerokosc <= 0 or wysokosc <= 0:
            raise ValueError("Wymiary muszą być dodatnie.")
        self.szerokosc = szerokosc
        self.wysokosc = wysokosc

    def pole(self):
        return self.szerokosc * self.wysokosc

    def obwod(self):
        return 2 * (self.szerokosc + self.wysokosc)
