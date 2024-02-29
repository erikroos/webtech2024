import random

class Aardman:
    def __init__(self, naam="Aardman", hit_points=0, levens=1):
        self._naam = naam
        self._hit_points = hit_points
        self._points_left = hit_points # extra t.b.v. de hitpoints-bug
        self._levens = levens
        self._levend = True

    def schade(self, geraakt):
        # Opgave 2: aanpassing om dode orks niet nog doder te maken
        if self._levend == False:
            print(f"{self._naam} is al dood")
            return
        self._points_left = self._points_left - geraakt # aangepast t.b.v. de hitpoints-bug
        print(f"Je bent {geraakt} keer geraakt en hebt nog {self._points_left} hit points over")
        if self._points_left < 0:
            self._levens -= 1
            self._points_left = self._hit_points # points herstellen, t.b.v. de hitpoints-bug
            #self._hit_points = 12 # Magic constant! Dit is een bug: deze klasse zou het initiële aantal hitpoints moeten onthouden
            if self._levens > 0:
                print(f"{self._naam} heeft een leven verloren")
            else:
                print(f"{self._naam} heeft alle levens verloren en is dood")
                self._levend = False

    def __str__(self):
        return f"Naam: {self._naam}, Levens: {self._levens}, Hit points: {self._points_left} / {self._hit_points}"


class Uruk_Hai(Aardman):
    def __init__(self, naam=""):
        super().__init__(naam=naam, levens=3, hit_points=12)

    def dodges(self):
        if random.randint(1, 3) == 3:
            print(f"***** {self._naam} dodges *****")
            return True
        else:
            return False
        
    def schade(self, geraakt):
        if not self.dodges():
            super().schade(geraakt)


class Ork(Aardman):
    def __init__(self, naam="", levens=1):
        super().__init__(naam=naam, levens=levens, hit_points=23)

    def slaan(self):
        print("Me {0._naam}. {0._naam} stomp you!".format(self))


class Mordor(Ork):
    def __init__(self, naam):
        super().__init__(naam)
        self._hit_points = 140
        self._points_left = 140

    def schade(self, geraakt):
        super().schade(geraakt // 4)


class Saruman(Ork):
    def __init__(self, naam):
        super().__init__(naam, 2) # 2 levens
        self._hit_points = 80
        self._points_left = 80

    def schade(self, geraakt):
        super().schade(geraakt // 2)