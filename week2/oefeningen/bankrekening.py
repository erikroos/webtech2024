import datetime

class Bankrekening:

    def _current_time():
        now = datetime.datetime.now()
        return now.strftime("%Y-%m-%d %H:%M:%S")

    def __init__(self, naam, saldo):
        self._name = naam
        #self.__saldo = saldo # Aanpassing opgave 1
        self.__saldo = 0 # Aanpassing opgave 1
        self._transactie_overzicht = []
        print("Bankrekening aangemaakt voor " + self._name)
        self.storten(saldo) # Toevoeging opgave 1

    def storten(self, bedrag):
        if bedrag > 0:
            self.__saldo += bedrag
            self._transactie_overzicht.append((Bankrekening._current_time(), bedrag))
        self.toon_saldo()

    def opnemen(self, bedrag):
        if 0 < bedrag <= self.__saldo:
            self.__saldo -= bedrag
            self._transactie_overzicht.append((Bankrekening._current_time(), -bedrag))
        else:
            print(f"Het bedrag dient groter dan nul (0) en maximaal gelijk aan het saldo ({self.__saldo}) te zijn")
        self.toon_saldo()

    def toon_saldo(self):
        print ("Saldo bedraagt {}".format(self.__saldo))

    def toon_transacties(self):
        print(f"Transacties van {self._name}s rekening:")
        for date, bedrag in self._transactie_overzicht:
            if bedrag > 0:
                trans_type = "gestort"
            else:
                trans_type = "opgenomen"
                bedrag *= -1
            print("{} {} op {}".format(bedrag, trans_type, date))

britt = Bankrekening("Britt", 800)
britt.storten(100)
britt.opnemen(200)
britt.toon_transacties()
