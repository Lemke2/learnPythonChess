class Potez():
    def __init__(self, red1, kol1, red2, kol2, promocija = None):
        self.red1, self.kol1 = red1, kol1
        self.red2, self.kol2 = red2, kol2
        if promocija is None:
            self.promocija = ""
            self.moveID = self.red1 * 1000 + self.kol1 * 100 + self.red2 * 10 + self.kol2
        elif promocija == "Q ":
            self.promocija = "Q "
            self.moveID = self.red1 * 1000 + self.kol1 * 100 + self.red2 * 10 + self.kol2 + 9
        elif promocija == "R ":
            self.promocija = "R "
            self.moveID = self.red1 * 1000 + self.kol1 * 100 + self.red2 * 10 + self.kol2 + 5
        elif promocija == "N ":
            self.promocija = "N "
            self.moveID = self.red1 * 1000 + self.kol1 * 100 + self.red2 * 10 + self.kol2 + 3
        elif promocija == "B ":
            self.promocija = "B "
            self.moveID = self.red1 * 1000 + self.kol1 * 100 + self.red2 * 10 + self.kol2 + 4
        elif promocija == "q ":
            self.promocija = "q "
            self.moveID = self.red1 * 1000 + self.kol1 * 100 + self.red2 * 10 + self.kol2 + 12
        elif promocija == "r ":
            self.promocija = "r "
            self.moveID = self.red1 * 1000 + self.kol1 * 100 + self.red2 * 10 + self.kol2 + 8
        elif promocija == "n ":
            self.promocija = "n "
            self.moveID = self.red1 * 1000 + self.kol1 * 100 + self.red2 * 10 + self.kol2 + 6
        else:
            self.promocija = "b "
            self.moveID = self.red1 * 1000 + self.kol1 * 100 + self.red2 * 10 + self.kol2 + 7

        #self.tipFigure1, self.tipFigure2 = "", ""
        # LEVO = KOL - 1  DESNO = KOL + 1 GORE = RED - 1 DOLE = RED + 1  GORELEVO = -1/-1 DOLELEVO = +1/-1 GOREDESNO = -1/+1 DOLEDESNO = +1/+1


    def __repr__(self):
        if self.promocija is None:
            return f"|{(self.red1, self.kol1)} {(self.red2, self.kol2)}|"
        else:
            return f"|{(self.red1, self.kol1)} {(self.red2, self.kol2)} {self.promocija}|"

    def __eq__(self, other):
        if isinstance(other, Potez):
            return self.moveID == other.moveID
        return False

    def getRedKol(self):
        return (self.red2, self.kol2)

    def getPocetniRedKol(self):
        return (self.red1, self.kol1)

    def getPromocija(self):
        return self.promocija