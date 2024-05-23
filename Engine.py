from Tabla import Tabla
from Potez import Potez
import re
tab = '\n'
map = {}
for i in range(100):
    map[i] = 0

class Engine:
    def __init__(self, tabla):
        self.tabla = tabla

    def napraviPotezPomocna(self, tabla, potez, legalniPotezi):
        for potez2 in legalniPotezi:
            if potez == potez2:
                return tabla.napraviPotez(potez)
        return None

    def napraviPotezPomocnaBezPromeneBoje(self, tabla, potez, legalniPotezi):
        for potez2 in legalniPotezi:
            if potez == potez2:
                return tabla.napraviPotezBezPromeneBoje(potez)
        return None

    def pretraziSah(self, tabla):
        sah = False
        bojaNaPotezu = tabla.getBojaNaPotezu()
        potezi = self.generisiPotezeProtivnickeBoje(tabla)

        for potez in potezi:
            polje = potez.getRedKol()
            if (tabla.getFigura(polje[0], polje[1]) == "K " and bojaNaPotezu) or (tabla.getFigura(polje[0], polje[1]) == "k " and not bojaNaPotezu):
                sah = True
        tabla.setSah(sah)
        return sah

    def test(self, tabla, dubina):
        if dubina == 0:
            return 1
        legalniPotezi = self.generisiPotezeBoje(tabla)
        brojPozicija = 0
        for potez in legalniPotezi:
            self.napraviPotezPomocna(tabla, potez, legalniPotezi)
            brojPozicija += self.test(tabla, dubina-1)
            tabla.undoPotez()
        if dubina == 1:
            print(f"{tabla} {brojPozicija} {tab}")  # file=open("output.txt", "a")
            val = map.get(brojPozicija) + 1
            map[brojPozicija] = val
        return brojPozicija

    def generisiPotezeBoje(self, tabla):
        self.pretraziSah(tabla)
        bojaNaPotezu = tabla.getBojaNaPotezu()
        sah = False
        legalniPotezi = []
        legalniPoteziSah = []
        if tabla.getBojaNaPotezu():
            for i in range(8):
                for j in range(8):
                    if tabla.getFigura(i, j).isupper():
                        legalniPotezi += self.generisiPotezeFigure(tabla, i, j)
        else:
            for i in range(8):
                for j in range(8):
                    if tabla.getFigura(i,j).islower():
                        legalniPotezi += self.generisiPotezeFigure(tabla, i, j)
        for potez in legalniPotezi:
            self.napraviPotezPomocnaBezPromeneBoje(tabla, potez, legalniPotezi)
            sah = self.pretraziSah(tabla)
            tabla.undoPotezBezPromeneBoje()
            if not sah:
                legalniPoteziSah.append(potez)
        return legalniPoteziSah

    def generisiPotezeProtivnickeBoje(self, tabla):
        bojaNaPotezu = tabla.getBojaNaPotezu()
        legalniPotezi = []
        if bojaNaPotezu:
            for i in range(8):
                for j in range(8):
                    if tabla.getFigura(i,j).islower():
                        legalniPotezi += self.generisiPotezeProtivnickeFigure(tabla, i, j)
        else:
            for i in range(8):
                for j in range(8):
                    if tabla.getFigura(i, j).isupper():
                        legalniPotezi += self.generisiPotezeProtivnickeFigure(tabla, i, j)

        return legalniPotezi

    def generisiPotezeFigure(self, tabla, red, kol):
        legalniPotezi = []
        tipFigure = tabla.getFigura(red, kol)
        bojaNaPotezu = tabla.getBojaNaPotezu()
        if bojaNaPotezu:
            if tipFigure == "P ":
                legalniPotezi = self.generisiPotezePijuna(tabla, red, kol)
            elif tipFigure == "R ":
                legalniPotezi = self.generisiPotezeTopa(tabla, red, kol)
            elif tipFigure == "N ":
                legalniPotezi = self.generisiPotezeKonja(tabla, red, kol)
            elif tipFigure == "B ":
                legalniPotezi = self.generisiPotezeLovca(tabla, red, kol)
            elif tipFigure == "Q ":
                legalniPotezi = self.generisiPotezeTopa(tabla, red, kol)
                legalniPotezi += self.generisiPotezeLovca(tabla, red, kol)
            elif tipFigure == "K ":
                legalniPotezi = self.generisiPotezeKralja(tabla, red, kol)
        else:
            if tipFigure == "p ":
                legalniPotezi = self.generisiPotezePijuna(tabla, red, kol)
            elif tipFigure == "r ":
                legalniPotezi = self.generisiPotezeTopa(tabla, red, kol)
            elif tipFigure == "n ":
                legalniPotezi = self.generisiPotezeKonja(tabla, red, kol)
            elif tipFigure == "b ":
                legalniPotezi = self.generisiPotezeLovca(tabla, red, kol)
            elif tipFigure == "q ":
                legalniPotezi = self.generisiPotezeTopa(tabla, red, kol)
                legalniPotezi += self.generisiPotezeLovca(tabla, red, kol)
            elif tipFigure == "k ":
                legalniPotezi = self.generisiPotezeKralja(tabla, red, kol)
        return legalniPotezi

    def generisiPotezeProtivnickeFigure(self, tabla, red, kol):
        legalniPotezi = []
        tipFigure = tabla.getFigura(red, kol)
        bojaNaPotezu = tabla.getBojaNaPotezu()
        tabla.setBojaNaPotezu(not bojaNaPotezu)
        if not bojaNaPotezu:
            if tipFigure == "P ":
                legalniPotezi = self.generisiPotezeProtivnickogPijuna(tabla, red, kol)
            elif tipFigure == "R ":
                legalniPotezi = self.generisiPotezeTopa(tabla, red, kol)
            elif tipFigure == "N ":
                legalniPotezi = self.generisiPotezeKonja(tabla, red, kol)
            elif tipFigure == "B ":
                legalniPotezi = self.generisiPotezeLovca(tabla, red, kol)
            elif tipFigure == "Q ":
                legalniPotezi = self.generisiPotezeTopa(tabla, red, kol)
                legalniPotezi += self.generisiPotezeLovca(tabla, red, kol)
            elif tipFigure == "K ":
                legalniPotezi = self.generisiPotezeProtivnickogKralja(tabla, red, kol)
        else:
            if tipFigure == "p ":
                legalniPotezi = self.generisiPotezeProtivnickogPijuna(tabla, red, kol)
            elif tipFigure == "r ":
                legalniPotezi = self.generisiPotezeTopa(tabla, red, kol)
            elif tipFigure == "n ":
                legalniPotezi = self.generisiPotezeKonja(tabla, red, kol)
            elif tipFigure == "b ":
                legalniPotezi = self.generisiPotezeLovca(tabla, red, kol)
            elif tipFigure == "q ":
                legalniPotezi = self.generisiPotezeTopa(tabla, red, kol)
                legalniPotezi += self.generisiPotezeLovca(tabla, red, kol)
            elif tipFigure == "k ":
                legalniPotezi = self.generisiPotezeProtivnickogKralja(tabla, red, kol)
        tabla.setBojaNaPotezu(bojaNaPotezu)
        return legalniPotezi


    def generisiPotezePijuna(self, tabla, red, kol):
        legalniPotezi = []
        bojaNaPotezu = tabla.getBojaNaPotezu()
        anPasan = tabla.getAnPasan()
        if bojaNaPotezu:
            if(tabla.getFigura(red, kol) == "P "):
                if (red == 6):
                    if (tabla.getFigura(red - 1, kol) == "/ " and tabla.getFigura(red - 2, kol) == "/ "):
                        legalniPotezi.append(Potez(red, kol, red-2, kol))
                if (red > 0 and tabla.getFigura(red - 1, kol) == "/ "):
                    if red == 1:
                        legalniPotezi.append(Potez(red, kol, red - 1, kol, "Q "))
                        legalniPotezi.append(Potez(red, kol, red - 1, kol, "R "))
                        legalniPotezi.append(Potez(red, kol, red - 1, kol, "N "))
                        legalniPotezi.append(Potez(red, kol, red - 1, kol, "B "))
                    else:
                        legalniPotezi.append(Potez(red, kol, red - 1, kol))
                if (kol > 0 and red > 0 and tabla.getFigura(red - 1, kol - 1).islower()):
                    if red == 1:
                        legalniPotezi.append(Potez(red, kol, red - 1, kol - 1, "Q "))
                        legalniPotezi.append(Potez(red, kol, red - 1, kol - 1, "R "))
                        legalniPotezi.append(Potez(red, kol, red - 1, kol - 1, "N "))
                        legalniPotezi.append(Potez(red, kol, red - 1, kol - 1, "B "))
                    else:
                        legalniPotezi.append(Potez(red, kol, red - 1, kol - 1))
                if (kol < 7 and red > 0 and tabla.getFigura(red - 1, kol + 1).islower()):
                    if red == 1:
                        legalniPotezi.append(Potez(red, kol, red - 1, kol + 1, "Q "))
                        legalniPotezi.append(Potez(red, kol, red - 1, kol + 1, "R "))
                        legalniPotezi.append(Potez(red, kol, red - 1, kol + 1, "N "))
                        legalniPotezi.append(Potez(red, kol, red - 1, kol + 1, "B "))
                    else:
                        legalniPotezi.append(Potez(red, kol, red - 1, kol + 1))
                if (len(anPasan) != 0 and anPasan[0] == red - 1):
                    if (anPasan[1] == kol - 1):
                        legalniPotezi.append(Potez(red, kol, red - 1, kol - 1))
                    elif (anPasan[1] == kol + 1):
                        legalniPotezi.append(Potez(red, kol, red - 1, kol + 1))
        else:
            if(tabla.getFigura(red, kol) == "p "):
                if (red == 1):
                    if (tabla.getFigura(red + 1, kol) == "/ " and tabla.getFigura(red + 2, kol) == "/ "):
                        legalniPotezi.append(Potez(red, kol, red + 2, kol))
                if (red < 7 and tabla.getFigura(red + 1, kol) == "/ "):
                    if red == 6:
                        legalniPotezi.append(Potez(red, kol, red + 1, kol, "q "))
                        legalniPotezi.append(Potez(red, kol, red + 1, kol, "r "))
                        legalniPotezi.append(Potez(red, kol, red + 1, kol, "n "))
                        legalniPotezi.append(Potez(red, kol, red + 1, kol, "b "))
                    else:
                        legalniPotezi.append(Potez(red, kol, red + 1, kol))
                if (kol > 0 and red < 7 and tabla.getFigura(red + 1, kol - 1).isupper()):
                    if red == 6:
                        legalniPotezi.append(Potez(red, kol, red + 1, kol - 1, "q "))
                        legalniPotezi.append(Potez(red, kol, red + 1, kol - 1, "r "))
                        legalniPotezi.append(Potez(red, kol, red + 1, kol - 1, "n "))
                        legalniPotezi.append(Potez(red, kol, red + 1, kol - 1, "b "))
                    else:
                        legalniPotezi.append(Potez(red, kol, red + 1, kol - 1))
                if (kol < 7 and red < 7 and tabla.getFigura(red + 1, kol + 1).isupper()):
                    if red == 6:
                        legalniPotezi.append(Potez(red, kol, red + 1, kol + 1, "q "))
                        legalniPotezi.append(Potez(red, kol, red + 1, kol + 1, "r "))
                        legalniPotezi.append(Potez(red, kol, red + 1, kol + 1, "n "))
                        legalniPotezi.append(Potez(red, kol, red + 1, kol + 1, "b "))
                    else:
                        legalniPotezi.append(Potez(red, kol, red + 1, kol + 1))
                if (len(anPasan) != 0 and anPasan[0] == red + 1):
                    if (anPasan[1] == kol - 1):
                        legalniPotezi.append(Potez(red, kol, red + 1, kol - 1))
                    elif (anPasan[1] == kol + 1):
                        legalniPotezi.append(Potez(red, kol, red + 1, kol + 1))
        return legalniPotezi


    def generisiPotezeProtivnickogPijuna(self, tabla, red, kol):
        legalniPotezi = []
        bojaNaPotezu = tabla.getBojaNaPotezu()
        if not bojaNaPotezu:
            if tabla.getFigura(red, kol) =="p ":
                red2 = red + 1
                kol2 = kol + 1
                red3 = red + 1
                kol3 = kol - 1
                if self.poljeUTabli((red2,kol2)):
                    legalniPotezi.append(Potez(red, kol, red2, kol2))
                if self.poljeUTabli((red3,kol3)):
                    legalniPotezi.append(Potez(red, kol, red3, kol3))
        else:
            if tabla.getFigura(red, kol) =="P ":
                red2 = red - 1
                kol2 = kol + 1
                red3 = red - 1
                kol3 = kol - 1
                if self.poljeUTabli((red2,kol2)):
                    legalniPotezi.append(Potez(red, kol, red2, kol2))
                if self.poljeUTabli((red3,kol3)):
                    legalniPotezi.append(Potez(red, kol, red3, kol3))
        return legalniPotezi

    def generisiPotezeTopa(self, tabla, red, kol):
        legalniPotezi = []
        bojaNaPotezu = tabla.getBojaNaPotezu()
        i = 1
        while (red - i >= 0 and tabla.getFigura(red - i, kol) == "/ "):
            legalniPotezi.append(Potez(red, kol, red - i, kol))
            i += 1
        if red - i >= 0:
            if (tabla.getFigura(red - i, kol).islower() and bojaNaPotezu) or (tabla.getFigura(red - i, kol).isupper() and not bojaNaPotezu):
                legalniPotezi.append(Potez(red, kol, red - i, kol))
        i = 1
        while (i + red < 8 and tabla.getFigura(red + i, kol) == "/ "):
            legalniPotezi.append(Potez(red, kol, red + i, kol))
            i += 1
        if red + i < 8:
            if (tabla.getFigura(red + i, kol).islower() and bojaNaPotezu) or (tabla.getFigura(red + i, kol).isupper() and not bojaNaPotezu):
                legalniPotezi.append(Potez(red, kol, red + i, kol))
        i = 1
        while (kol - i >= 0 and tabla.getFigura(red, kol - i) == "/ "):
            legalniPotezi.append(Potez(red, kol, red, kol - i))
            i += 1
        if kol - i >= 0:
            if (tabla.getFigura(red, kol - i).islower() and bojaNaPotezu) or (tabla.getFigura(red, kol - i).isupper() and not bojaNaPotezu):
                legalniPotezi.append(Potez(red, kol, red, kol - i))
        i = 1
        while (kol + i < 8 and tabla.getFigura(red, kol + i) == "/ "):
            legalniPotezi.append(Potez(red, kol, red, kol + i))
            i += 1
        if kol + i < 8:
            if (tabla.getFigura(red, kol + i).islower() and bojaNaPotezu) or (tabla.getFigura(red, kol + i).isupper() and not bojaNaPotezu):
                legalniPotezi.append(Potez(red, kol, red, kol + i))
        return legalniPotezi

    def generisiPotezeKonja(self, tabla, red, kol):
        legalniPotezi = []
        bojaNaPotezu = tabla.getBojaNaPotezu()
        polje1 = (red - 2, kol - 1)
        polje2 = (red - 2, kol + 1)
        polje3 = (red - 1, kol + 2)
        polje4 = (red + 1, kol + 2)
        polje5 = (red + 2, kol + 1)
        polje6 = (red + 2, kol - 1)
        polje7 = (red + 1, kol - 2)
        polje8 = (red - 1, kol - 2)
        listaPolja = [polje1, polje2, polje3, polje4, polje5, polje6, polje7, polje8]

        for polje in listaPolja:
            if self.poljeUTabli(polje):
                if tabla.getFigura(polje[0], polje[1]) == "/ ":
                    legalniPotezi.append(Potez(red, kol, polje[0], polje[1]))
                elif (tabla.getFigura(polje[0], polje[1]).islower() and bojaNaPotezu) or (tabla.getFigura(polje[0], polje[1]).isupper() and not bojaNaPotezu):
                    legalniPotezi.append(Potez(red, kol, polje[0], polje[1]))
        return legalniPotezi

    def generisiPotezeLovca(self, tabla, red, kol):
        legalniPotezi = []
        bojaNaPotezu = tabla.getBojaNaPotezu()
        i = 1
        polje = (red + i, kol + i)
        while self.poljeUTabli(polje) and tabla.getFigura(polje[0], polje[1]) == "/ ":
            legalniPotezi.append(Potez(red, kol, polje[0], polje[1]))
            i += 1
            polje = (red + i, kol + i)
        if self.poljeUTabli(polje):
            if (tabla.getFigura(polje[0], polje[1]).islower() and bojaNaPotezu) or (tabla.getFigura(polje[0], polje[1]).isupper() and not bojaNaPotezu):
                legalniPotezi.append(Potez(red, kol, polje[0], polje[1]))
        i = 1
        polje = (red + i, kol - i)
        while self.poljeUTabli(polje) and tabla.getFigura(polje[0], polje[1]) == "/ ":
            legalniPotezi.append(Potez(red, kol, polje[0], polje[1]))
            i += 1
            polje = (red + i, kol - i)
        if self.poljeUTabli(polje):
            if (tabla.getFigura(polje[0], polje[1]).islower() and bojaNaPotezu) or (tabla.getFigura(polje[0], polje[1]).isupper() and not bojaNaPotezu):
                legalniPotezi.append(Potez(red, kol, polje[0], polje[1]))
        i = 1
        polje = (red - i, kol - i)
        while self.poljeUTabli(polje) and tabla.getFigura(polje[0], polje[1]) == "/ ":
            legalniPotezi.append(Potez(red, kol, polje[0], polje[1]))
            i += 1
            polje = (red - i, kol - i)
        if self.poljeUTabli(polje):
            if (tabla.getFigura(polje[0], polje[1]).islower() and bojaNaPotezu) or (tabla.getFigura(polje[0], polje[1]).isupper() and not bojaNaPotezu):
                legalniPotezi.append(Potez(red, kol, polje[0], polje[1]))
        i = 1
        polje = (red - i, kol + i)
        while self.poljeUTabli(polje) and tabla.getFigura(polje[0], polje[1]) == "/ ":
            legalniPotezi.append(Potez(red, kol, polje[0], polje[1]))
            i += 1
            polje = (red - i, kol + i)
        if self.poljeUTabli(polje):
            if (tabla.getFigura(polje[0], polje[1]).islower() and bojaNaPotezu) or (tabla.getFigura(polje[0], polje[1]).isupper() and not bojaNaPotezu):
                legalniPotezi.append(Potez(red, kol, polje[0], polje[1]))
        return legalniPotezi

    def generisiPotezeKralja(self, tabla, red, kol):
        legalniPotezi = []
        bojaNaPotezu = tabla.getBojaNaPotezu()
        rokade = tabla.getRokade()
        protivnickiPotezi = self.generisiPotezeProtivnickeBoje(tabla)
        uSahu = tabla.getSah()
        napadnutaPolja = []
        wkingside = True
        wqueenside = True
        bkingside = True
        bqueenside = True
        listaPolja = [(red + 1, kol), (red + 1, kol + 1), (red, kol + 1), (red - 1, kol + 1), (red - 1, kol),(red - 1, kol - 1), (red, kol - 1), (red + 1, kol - 1)]

        for potez in protivnickiPotezi:
            napadnutaPolja.append(potez.getRedKol())

        if ((7,5) in napadnutaPolja) or ((7,6) in napadnutaPolja):
            wkingside = False
        if ((0,5) in napadnutaPolja) or ((0,6) in napadnutaPolja):
            bkingside = False
        if ((7,1) in napadnutaPolja) or (7,2) in napadnutaPolja or ((7,3) in napadnutaPolja):
            wqueenside = False
        if (0,2) in napadnutaPolja or (0,3) in napadnutaPolja:
            bqueenside = False

        for polje in listaPolja:
            if self.poljeUTabli(polje):
                if polje in napadnutaPolja:
                    pass
                elif (bojaNaPotezu and tabla.getFigura(polje[0], polje[1]).isupper()) or (not bojaNaPotezu and tabla.getFigura(polje[0], polje[1]).islower()):
                    pass
                else:
                    legalniPotezi.append(Potez(red, kol, polje[0], polje[1]))
        if not uSahu:
            if bojaNaPotezu and rokade[0] == True and wkingside:
                if tabla.getFigura(7, 5) == "/ " and tabla.getFigura(7, 6) == "/ " and tabla.getFigura(7,7) == "R ":
                    legalniPotezi.append(Potez(red, kol, 7, 7))
            if bojaNaPotezu and rokade[1] == True and wqueenside:
                if tabla.getFigura(7, 1) == "/ " and tabla.getFigura(7, 2) == "/ " and tabla.getFigura(7, 3) == "/ " and tabla.getFigura(7,0) == "R ":
                    legalniPotezi.append(Potez(red, kol, 7, 0))
            if not bojaNaPotezu and rokade[2] == True and bkingside:
                if tabla.getFigura(0, 5) == "/ "and tabla.getFigura(0, 6) == "/ "  and tabla.getFigura(0,7) == "r ":
                    legalniPotezi.append(Potez(red, kol, 0, 7))
            if not bojaNaPotezu and rokade[3] == True and bqueenside:
                if tabla.getFigura(0, 1) == "/ " and tabla.getFigura(0, 2) == "/ " and tabla.getFigura(0, 3) == "/ "  and tabla.getFigura(0,0) == "r ":
                    legalniPotezi.append(Potez(red, kol, 0, 0))
        return legalniPotezi

    def generisiPotezeProtivnickogKralja(self, tabla, red, kol):
        legalniPotezi = []
        listaPolja = [(red + 1, kol), (red + 1, kol + 1), (red, kol + 1), (red - 1, kol + 1), (red - 1, kol),
                      (red - 1, kol - 1), (red, kol - 1), (red + 1, kol - 1)]
        for polje in listaPolja:
            if self.poljeUTabli(polje):
                legalniPotezi.append(Potez(red, kol, polje[0], polje[1]))
        return legalniPotezi

    def poljeUTabli(self, p1):
        if (0 <= p1[0] < 8 and 0 <= p1[1] < 8):
            return True

    def algebarskaNotacijaParser(self, tabla, potez):
        kolone = ["a", "b", "c", "d", "e", "f", "g", "h"]
        redovi = ["8","7","6","5","4","3","2","1"]
        red1, kol1, red2, kol2 = 0, 0, 0, 0
        tipFigure1 = ""
        bojaNaPotezu = tabla.getBojaNaPotezu()
        regexKRokada = "^O-O.?$"
        regexQRokada = "^O-O-O.?$"
        regexPijunNapred = "^[a-h][1-8].?$"
        regexFiguraNapred = "^[BNKQR][a-h][1-8].?$"
        regexPijunJede = "^[a-h]x[a-h][1-8].?$"
        regexFiguraJede = "^[BNKQR]x[a-h][1-8].?$"
        regexFiguraNapredNejasnaKolona = "^[BNKQR][a-h][a-h][1-8].?$"
        regexFiguraNapredNeJasnaKolonaJede = "^[BNKQR][a-h]x[a-h][1-8].?$"
        regexFiguraNapredNejasanRed = "^[BNKQR][1-8][a-h][1-8].?$"
        regexFiguraNapredNejasanRedJede = "^[BNKQR][1-8]x[a-h][1-8].?$"
        regexFiguraNapredNejasnoRedKol = "^[BNKQR][a-h][1-8][a-h][1-8].?$"
        regexFiguraNapredNejasnoRedKolJede = "^[BNKQR][a-h][1-8]x[a-h][1-8].?$"
        regexPromocija = "^[a-h][1-8]=[BNKQR].?$"
        regexPromocijaJede = "^[a-h]x[a-h][1-8]=[BNKQR].?$"
        flagRed1 = False
        flagKol1 = False
        flagPromocija = False
        promocija = ""

        if re.match(regexKRokada, potez):
            if bojaNaPotezu:
                return Potez(7,4,7,7)
            return Potez(0,4,0,7)
        elif re.match(regexQRokada, potez):
            if bojaNaPotezu:
                return Potez(7,4,7,0)
            return Potez(0,4,0,0)
        elif re.match(regexPijunNapred, potez):
            tipFigure1 = "P " if bojaNaPotezu else "p "
            kol2Pom = potez[0]
            kol2 = kolone.index(kol2Pom)
            red2Pom = potez[1]
            red2 = redovi.index(red2Pom)
            kol1 = kol2
            flagKol1 = True
        elif re.match(regexFiguraNapred, potez):
            tipFigure1 = potez[0] + " " if bojaNaPotezu else potez[0].lower() + " "
            kol2Pom = potez[1]
            kol2 = kolone.index(kol2Pom)
            red2Pom = potez[2]
            red2 = redovi.index(red2Pom)
        elif re.match(regexPijunJede, potez):
            tipFigure1 = "P " if bojaNaPotezu else "p "
            kol2Pom = potez[2]
            kol2 = kolone.index(kol2Pom)
            red2Pom = potez[3]
            red2 = redovi.index(red2Pom)
            kol1Pom = potez[0]
            kol1 = kolone.index(kol1Pom)
            flagKol1 = True
        elif re.match(regexFiguraJede, potez):
            tipFigure1 = potez[0] + " " if bojaNaPotezu else potez[0].lower() + " "
            kol2Pom = potez[2]
            kol2 = kolone.index(kol2Pom)
            red2Pom = potez[3]
            red2 = redovi.index(red2Pom)
        elif re.match(regexFiguraNapredNejasnaKolona, potez):
            tipFigure1 = potez[0] + " " if bojaNaPotezu else potez[0].lower() + " "
            kol2Pom = potez[2]
            kol2 = kolone.index(kol2Pom)
            red2Pom = potez[3]
            red2 = redovi.index(red2Pom)
            kol1Pom = potez[1]
            kol1 = kolone.index(kol1Pom)
            flagKol1 = True
        elif re.match(regexFiguraNapredNeJasnaKolonaJede, potez):
            tipFigure1 = potez[0] + " " if bojaNaPotezu else potez[0].lower() + " "
            kol2Pom = potez[3]
            kol2 = kolone.index(kol2Pom)
            red2Pom = potez[4]
            red2 = redovi.index(red2Pom)
            kol1Pom = potez[1]
            kol1 = kolone.index(kol1Pom)
            flagKol1 = True
        elif re.match(regexFiguraNapredNejasanRed, potez):
            tipFigure1 = potez[0] + " " if bojaNaPotezu else potez[0].lower() + " "
            kol2Pom = potez[2]
            kol2 = kolone.index(kol2Pom)
            red2Pom = potez[3]
            red2 = redovi.index(red2Pom)
            red1Pom = potez[1]
            red1 = redovi.index(red1Pom)
            flagRed1 = True
        elif re.match(regexFiguraNapredNejasanRedJede, potez):
            tipFigure1 = potez[0] + " " if bojaNaPotezu else potez[0].lower() + " "
            kol2Pom = potez[3]
            kol2 = kolone.index(kol2Pom)
            red2Pom = potez[4]
            red2 = redovi.index(red2Pom)
            red1Pom = potez[1]
            red1 = redovi.index(red1Pom)
            flagRed1 = True
        elif re.match(regexFiguraNapredNejasnoRedKol, potez):
            tipFigure1 = potez[0] + " " if bojaNaPotezu else potez[0].lower() + " "
            kol2Pom = potez[3]
            kol2 = kolone.index(kol2Pom)
            red2Pom = potez[4]
            red2 = redovi.index(red2Pom)
            kol1Pom = potez[1]
            kol1 = kolone.index(kol1Pom)
            red1Pom = potez[2]
            red1 = redovi.index(red1Pom)
            return Potez(red1, kol1, red2, kol2)
        elif re.match(regexFiguraNapredNejasnoRedKolJede, potez):
            tipFigure1 = potez[0] + " " if bojaNaPotezu else potez[0].lower() + " "
            kol2Pom = potez[4]
            kol2 = kolone.index(kol2Pom)
            red2Pom = potez[5]
            red2 = redovi.index(red2Pom)
            kol1Pom = potez[1]
            kol1 = kolone.index(kol1Pom)
            red1Pom = potez[2]
            red1 = redovi.index(red1Pom)
            return Potez(red1, kol1, red2, kol2)
        elif re.match(regexPromocija, potez):
            tipFigure1 = "P " if bojaNaPotezu else "p "
            kol2Pom = potez[0]
            kol2 = kolone.index(kol2Pom)
            red2Pom = potez[1]
            red2 = redovi.index(red2Pom)
            kol1 = kol2
            flagPromocija = True
            promocija = potez[3] + " " if bojaNaPotezu else potez[3].lower() + " "
        elif re.match(regexPromocijaJede, potez):
            tipFigure1 = "P " if bojaNaPotezu else "p "
            kol2Pom = potez[2]
            kol2 = kolone.index(kol2Pom)
            red2Pom = potez[3]
            red2 = redovi.index(red2Pom)
            kol1Pom = potez[0]
            kol1 = kolone.index(kol1Pom)
            flagPromocija = True
            promocija = potez[3] + " " if bojaNaPotezu else potez[3].lower() + " "

        if flagPromocija:
            for i in range(8):
                if tabla.getFigura(i, kol1) == tipFigure1:
                    if Potez(i, kol1, red2, kol2, promocija) in self.generisiPotezeFigure(tabla, i, kol1):
                        return Potez(i, kol1, red2, kol2, promocija)
        if flagKol1:
            for i in range(8):
                if tabla.getFigura(i, kol1) == tipFigure1:
                    if Potez(i, kol1, red2, kol2) in self.generisiPotezeFigure(tabla, i, kol1):
                        return Potez(i, kol1, red2, kol2)
        elif flagRed1:
            for i in range(8):
                if tabla.getFigura(red1, i) == tipFigure1:
                    if Potez(red1, i, red2, kol2) in self.generisiPotezeFigure(tabla, red1, i):
                        return Potez(red1, i, red2, kol2)
        else:
            for i in range(8):
                for j in range(8):
                    if tabla.getFigura(i, j) == tipFigure1:
                        if Potez(i, j, red2, kol2) in self.generisiPotezeFigure(tabla, i , j):
                            return Potez(i, j, red2, kol2)