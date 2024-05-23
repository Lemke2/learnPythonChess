class Tabla:
    def __init__(self, input):
        self.tablaFigura = [["", "", "", "", "", "", "", ""],
                            ["", "", "", "", "", "", "", ""],
                            ["", "", "", "", "", "", "", ""],
                            ["", "", "", "", "", "", "", ""],
                            ["", "", "", "", "", "", "", ""],
                            ["", "", "", "", "", "", "", ""],
                            ["", "", "", "", "", "", "", ""],
                            ["", "", "", "", "", "", "", ""]]

        self.tabla = [["a8", "b8", "c8", "d8", "e8", "f8", "g8", "h8"],
                      ["a7", "b7", "c7", "d7", "e7", "f7", "g7", "h7"],
                      ["a6", "b6", "c6", "d6", "e6", "f6", "g6", "h6"],
                      ["a5", "b5", "c5", "d5", "e5", "f5", "g5", "h5"],
                      ["a4", "b4", "c4", "d4", "e4", "f4", "g4", "h4"],
                      ["a3", "b3", "c3", "d3", "e3", "f3", "g3", "h3"],
                      ["a2", "b2", "c2", "d2", "e2", "f2", "g2", "h2"],
                      ["a1", "b1", "c1", "d1", "e1", "f1", "g1", "h1"]]

        self.moveList = []          #istorija poteza
        self.anPasanList = []
        self.rokadeList = []
        self.bojaNaPotezu = True    #true = beli na potezu
        self.brojPoteza = 0
        self.brojPoluPoteza = 0     #50 Move rule
        self.rokade = [False, False, False, False]            #spisak dozvoljenih rokada
        self.anPasan = () #legalan an pasant (poslednji potez nekog pijuna kad se ucitava FEN
        self.legalniPotezi = []
        self.sah = False
        self.mat = False

        niz = input.split("/")
        red = 0
        kolona = 0
        for string in niz:
            for c in string:
                if (c == " "):
                    break
                if (c.isalpha()):
                    self.tablaFigura[red][kolona] = c + " "
                    kolona += 1
                elif (c.isnumeric()):
                    for i in range(int(c)):
                        self.tablaFigura[red][kolona] = "/ "
                        kolona += 1
            kolona = 0
            red += 1
        niz2 = niz[7].split()
        if len(niz2) == 6:
            self.brojPoteza = int(niz2[5])
            self.brojPoluPoteza = int(niz2[4])
            if (niz2[1] == "w"):
                self.bojaNaPotezu = True
            else:
                self.bojaNaPotezu = False
            anPasanPrivremen = niz2[3]
            if (anPasanPrivremen == "-"):
                self.anPasan = ()
            else:
                for i in range(8):
                    if (self.tabla[0][i][0] == anPasanPrivremen[0]):
                        self.anPasan = (8 - int(anPasanPrivremen[1]), i)
            if ("K" in niz2[2]):
                self.rokade[0] = True

            if ("Q" in niz2[2]):
                self.rokade[1] = True

            if ("k" in niz2[2]):
                self.rokade[2] = True

            if ("q" in niz2[2]):
                self.rokade[3] = True
        else:
            self.brojPoteza = int(niz2[4])
            self.brojPoluPoteza = int(niz2[3])
            if (niz2[1] == "w"):
                self.bojaNaPotezu = True
            else:
                self.bojaNaPotezu = False
            anPasanPrivremen = niz2[3]
            if (anPasanPrivremen == "-"):
                self.anPasan = ()
            else:
                for i in range(8):
                    if (self.tabla[0][i][0] == anPasanPrivremen[0]):
                        self.anPasan = (8 - int(anPasanPrivremen[1]), i)
        self.anPasanList.append(self.anPasan)
        self.rokadeList.append(self.rokade.copy())
    def __repr__(self):
        tabla = ""
        for x in range(0,8):
            for y in range(0,8):
                tabla = tabla + self.tablaFigura[x][y]
            tabla = tabla + "\n"
        return tabla

    def fenGenerator(self):
        povratniString = ""
        brojac = 0
        flag1 = False
        flag2 = False
        for i in range(8):
            for j in range(8):
                if self.tablaFigura[i][j][0].isalpha():
                    if brojac != 0:
                        povratniString += f"{brojac}"
                        brojac = 0
                    povratniString += self.tablaFigura[i][j][0]
                elif self.tablaFigura[i][j] == "/ ":
                    brojac += 1
                if brojac == 8 or (j == 7 and brojac != 0):
                    povratniString += f"{brojac}"
                    brojac = 0
            if i != 7:
                povratniString+= "/"
        povratniString += " "
        if self.bojaNaPotezu:
            povratniString += "w"
        else:
            povratniString += "b"
        povratniString += " "
        if self.rokade[0]:
            povratniString += "K"
            flag1 = True
        if self.rokade[1]:
            povratniString += "Q"
            flag1 = True
        if self.rokade[2]:
            povratniString += "k"
            flag1 = True
        if self.rokade[3]:
            povratniString += "q"
            flag1 = True
        if flag1:
            povratniString += " "
        else:
            povratniString += "- "
        if self.anPasan == ():
            povratniString += "- "
        else:
            povratniString += f"{self.tabla[self.anPasan[0]][self.anPasan[1]]} "
        povratniString += f"{self.brojPoluPoteza} "
        povratniString += f"{self.brojPoteza}"

        return povratniString

    def getBojaNaPotezu(self):
        return self.bojaNaPotezu

    def getTabla(self):
        return self.tabla

    def setBojaNaPotezu(self, bojaNaPotezu):
        self.bojaNaPotezu = bojaNaPotezu

    def getRokade(self):
        return self.rokade

    def getAnPasan(self):
        return self.anPasan

    def getBrojPoluPoteza(self):
        return self.brojPoluPoteza

    def getBrojPoteza(self):
        return self.brojPoteza

    def getSah(self):
        return self.sah

    def getMat(self):
        return self.mat

    def setSah(self, sah):
        self.sah = sah

    def setMat(self, mat):
        self.mat = mat

    def setRokade(self, rokade):
        self.rokade = rokade

    def setAnPasan(self, anPasan):
        self.anPasan = anPasan

    def getLegalniPotezi(self):
        return self.legalniPotezi

    def setLegalniPotezi(self, legalniPotezi):
        self.legalniPotezi = legalniPotezi

    def getFigura(self, red, kol):
        return self.tablaFigura[red][kol]

    def setFigura(self, red, kol, figura):
        self.tablaFigura[red][kol] = figura

    def generisiTabluKopiju(self):
        tabla = Tabla(self.fenGenerator())
        return tabla

    def napraviPotez(self, potez):
        polje1 = potez.getPocetniRedKol()
        polje2 = potez.getRedKol()
        tipFigure1 = self.tablaFigura[polje1[0]][polje1[1]]
        tipFigure2 = self.tablaFigura[polje2[0]][polje2[1]]
        promocija = potez.getPromocija()

        self.tablaFigura[polje2[0]][polje2[1]] = self.tablaFigura[polje1[0]][polje1[1]]
        self.tablaFigura[polje1[0]][polje1[1]] = "/ "

        if (tipFigure1 == "P "):
            if (polje1[0] == 6 and polje2[0] == 4):
                self.anPasan = (polje2[0] + 1, polje2[1])
            elif polje2[0] == 0:
                self.tablaFigura[polje2[0]][polje2[1]] = promocija
                self.anPasan = ()
            elif (len(self.anPasan) != 0):
                if (polje2 == self.anPasan):
                    self.tablaFigura[self.anPasan[0] + 1][self.anPasan[1]] = "/ "
                self.anPasan = ()
            else:
                self.anPasan = ()
        elif (tipFigure1 == "p "):
            if (polje1[0] == 1 and polje2[0] == 3):
                self.anPasan = (polje2[0] - 1, polje2[1])
            elif polje2[0] == 7:
                self.tablaFigura[polje2[0]][polje2[1]] = promocija
                self.anPasan = ()
            elif (len(self.anPasan) != 0):
                if (polje2 == self.anPasan):
                    self.tablaFigura[self.anPasan[0] - 1][self.anPasan[1]] = "/ "
                self.anPasan = ()
            else:
                self.anPasan = ()
        elif tipFigure1 == "R " and polje1 == (7, 7):
            self.rokade[0] = False
            self.anPasan = ()
        elif tipFigure1 == "R " and polje1 == (7, 0):
            self.rokade[1] = False
            self.anPasan = ()
        elif tipFigure1 == "r " and polje1 == (0, 7):
            self.rokade[2] = False
            self.anPasan = ()
        elif tipFigure1 == "r " and polje1 == (0, 0):
            self.rokade[3] = False
            self.anPasan = ()
        else:
            self.anPasan = ()

        if tipFigure1 == "K ":
            if polje1 == (7, 4) and self.rokade[0] == True and polje2 == (7, 7):
                self.tablaFigura[7][6] = "K "
                self.tablaFigura[7][5] = "R "
                self.tablaFigura[7][4] = "/ "
                self.tablaFigura[7][7] = "/ "
            elif polje1 == (7, 4) and self.rokade[1] == True and polje2 == (7, 0):
                self.tablaFigura[7][2] = "K "
                self.tablaFigura[7][3] = "R "
                self.tablaFigura[7][4] = "/ "
                self.tablaFigura[7][1] = "/ "
                self.tablaFigura[7][0] = "/ "
            self.rokade[0] = False
            self.rokade[1] = False
        elif tipFigure1 == "k ":
            if polje1 == (0, 4) and self.rokade[2] == True and polje2 == (0, 7):
                self.tablaFigura[0][6] = "k "
                self.tablaFigura[0][5] = "r "
                self.tablaFigura[0][4] = "/ "
                self.tablaFigura[0][7] = "/ "
            elif polje1 == (0, 4) and self.rokade[3] == True and polje2 == (0, 0):
                self.tablaFigura[0][2] = "k "
                self.tablaFigura[0][3] = "r "
                self.tablaFigura[0][4] = "/ "
                self.tablaFigura[0][1] = "/ "
                self.tablaFigura[0][0] = "/ "
            self.rokade[2] = False
            self.rokade[3] = False

        self.bojaNaPotezu = not self.bojaNaPotezu
        self.brojPoluPoteza += 1
        self.brojPoteza = self.brojPoluPoteza//2
        self.rokadeList.append(self.rokade.copy())
        self.anPasanList.append(self.anPasan)
        self.moveList.append((potez, tipFigure1, tipFigure2))
        return self

    def napraviPotezBezPromeneBoje(self, potez):
        polje1 = potez.getPocetniRedKol()
        polje2 = potez.getRedKol()
        tipFigure1 = self.tablaFigura[polje1[0]][polje1[1]]
        tipFigure2 = self.tablaFigura[polje2[0]][polje2[1]]
        promocija = potez.getPromocija()

        self.tablaFigura[polje2[0]][polje2[1]] = self.tablaFigura[polje1[0]][polje1[1]]
        self.tablaFigura[polje1[0]][polje1[1]] = "/ "

        if (tipFigure1 == "P "):
            if (polje1[0] == 6 and polje2[0] == 4):
                self.anPasan = (polje2[0] + 1, polje2[1])
            elif polje2[0] == 0:
                self.tablaFigura[polje2[0]][polje2[1]] = promocija
                self.anPasan = ()
            elif (len(self.anPasan) != 0):
                if (polje2 == self.anPasan):
                    self.tablaFigura[self.anPasan[0] + 1][self.anPasan[1]] = "/ "
                self.anPasan = ()
            else:
                self.anPasan = ()
        elif (tipFigure1 == "p "):
            if (polje1[0] == 1 and polje2[0] == 3):
                self.anPasan = (polje2[0] - 1, polje2[1])
            elif polje2[0] == 7:
                self.tablaFigura[polje2[0]][polje2[1]] = promocija
                self.anPasan = ()
            elif (len(self.anPasan) != 0):
                if (polje2 == self.anPasan):
                    self.tablaFigura[self.anPasan[0] - 1][self.anPasan[1]] = "/ "
                self.anPasan = ()
            else:
                self.anPasan = ()
        elif tipFigure1 == "R " and polje1 == (7, 7):
            self.rokade[0] = False
            self.anPasan = ()
        elif tipFigure1 == "R " and polje1 == (7, 0):
            self.rokade[1] = False
            self.anPasan = ()
        elif tipFigure1 == "r " and polje1 == (0, 7):
            self.rokade[2] = False
            self.anPasan = ()
        elif tipFigure1 == "r " and polje1 == (0, 0):
            self.rokade[3] = False
            self.anPasan = ()
        else:
            self.anPasan = ()

        if tipFigure1 == "K ":
            if polje1 == (7, 4) and self.rokade[0] == True and polje2 == (7, 7):
                self.tablaFigura[7][6] = "K "
                self.tablaFigura[7][5] = "R "
                self.tablaFigura[7][4] = "/ "
                self.tablaFigura[7][7] = "/ "
            elif polje1 == (7, 4) and self.rokade[1] == True and polje2 == (7, 0):
                self.tablaFigura[7][2] = "K "
                self.tablaFigura[7][3] = "R "
                self.tablaFigura[7][4] = "/ "
                self.tablaFigura[7][1] = "/ "
                self.tablaFigura[7][0] = "/ "
            self.rokade[0] = False
            self.rokade[1] = False
        elif tipFigure1 == "k ":
            if polje1 == (0, 4) and self.rokade[2] == True and polje2 == (0, 7):
                self.tablaFigura[0][6] = "k "
                self.tablaFigura[0][5] = "r "
                self.tablaFigura[0][4] = "/ "
                self.tablaFigura[0][7] = "/ "
            elif polje1 == (0, 4) and self.rokade[3] == True and polje2 == (0, 0):
                self.tablaFigura[0][2] = "k "
                self.tablaFigura[0][3] = "r "
                self.tablaFigura[0][4] = "/ "
                self.tablaFigura[0][1] = "/ "
                self.tablaFigura[0][0] = "/ "
            self.rokade[2] = False
            self.rokade[3] = False

        self.brojPoluPoteza += 1
        self.brojPoteza = self.brojPoluPoteza // 2
        self.rokadeList.append(self.rokade.copy())
        self.anPasanList.append(self.anPasan)
        self.moveList.append((potez, tipFigure1, tipFigure2))
        return self

    def undoPotez(self):
        if self.moveList and self.rokadeList and self.anPasanList:
            poslednjiPotez = self.moveList.pop()
            self.anPasanList.pop()
            self.rokadeList.pop()
            self.rokade = self.rokadeList[-1].copy()
            self.anPasan = self.anPasanList[-1]
            tipFigure1 = poslednjiPotez[1]
            tipFigure2 = poslednjiPotez[2]
            polje1 = poslednjiPotez[0].getPocetniRedKol()
            polje2 = poslednjiPotez[0].getRedKol()
            if tipFigure1 == "P " and self.anPasan == polje2 and tipFigure2 == "/ ":
                self.tablaFigura[polje2[0] + 1][polje2[1]] = "p "
                self.tablaFigura[polje1[0]][polje1[1]] = "P "
                self.tablaFigura[polje2[0]][polje2[1]] = "/ "
            elif tipFigure1 == "p " and self.anPasan == polje2 and tipFigure2 == "/ ":
                self.tablaFigura[polje2[0] - 1][polje2[1]] = "P "
                self.tablaFigura[polje1[0]][polje1[1]] = "p "
                self.tablaFigura[polje2[0]][polje2[1]] = "/ "
            if tipFigure1 == "K ":
                if polje1 == (7, 4) and polje2 == (7, 7):
                    self.tablaFigura[7][6] = "/ "
                    self.tablaFigura[7][5] = "/ "
                    self.tablaFigura[7][4] = "K "
                    self.tablaFigura[7][7] = "R "
                elif polje1 == (7, 4) and polje2 == (7, 0):
                    self.tablaFigura[7][2] = "/ "
                    self.tablaFigura[7][3] = "/ "
                    self.tablaFigura[7][4] = "K "
                    self.tablaFigura[7][1] = "/ "
                    self.tablaFigura[7][0] = "R "
                else:
                    self.tablaFigura[polje2[0]][polje2[1]] = tipFigure2
                    self.tablaFigura[polje1[0]][polje1[1]] = tipFigure1
            elif tipFigure1 == "k ":
                if polje1 == (0, 4) and polje2 == (0, 7):
                    self.tablaFigura[0][6] = "/ "
                    self.tablaFigura[0][5] = "/ "
                    self.tablaFigura[0][4] = "k "
                    self.tablaFigura[0][7] = "r "
                elif polje1 == (0, 4) and polje2 == (0, 0):
                    self.tablaFigura[0][2] = "/ "
                    self.tablaFigura[0][3] = "/ "
                    self.tablaFigura[0][4] = "k "
                    self.tablaFigura[0][1] = "/ "
                    self.tablaFigura[0][0] = "r "
                else:
                    self.tablaFigura[polje2[0]][polje2[1]] = tipFigure2
                    self.tablaFigura[polje1[0]][polje1[1]] = tipFigure1
            else:
                self.tablaFigura[polje2[0]][polje2[1]] = tipFigure2
                self.tablaFigura[polje1[0]][polje1[1]] = tipFigure1
            self.bojaNaPotezu = not self.bojaNaPotezu
            self.brojPoluPoteza -= 1
            self.brojPoteza = self.brojPoluPoteza // 2



    def undoPotezBezPromeneBoje(self):
        if self.moveList and self.rokadeList and self.anPasanList:
            poslednjiPotez = self.moveList.pop()
            self.anPasanList.pop()
            self.rokadeList.pop()
            self.rokade = self.rokadeList[-1].copy()
            self.anPasan = self.anPasanList[-1]
            tipFigure1 = poslednjiPotez[1]
            tipFigure2 = poslednjiPotez[2]
            polje1 = poslednjiPotez[0].getPocetniRedKol()
            polje2 = poslednjiPotez[0].getRedKol()
            if tipFigure1 == "P " and self.anPasan == polje2 and tipFigure2 == "/ ":
                self.tablaFigura[polje2[0] + 1][polje2[1]] = "p "
                self.tablaFigura[polje1[0]][polje1[1]] = "P "
                self.tablaFigura[polje2[0]][polje2[1]] = "/ "
            elif tipFigure1 == "p " and self.anPasan == polje2 and tipFigure2 == "/ ":
                self.tablaFigura[polje2[0] - 1][polje2[1]] = "P "
                self.tablaFigura[polje1[0]][polje1[1]] = "p "
                self.tablaFigura[polje2[0]][polje2[1]] = "/ "
            if tipFigure1 == "K ":
                if polje1 == (7, 4) and polje2 == (7, 7):
                    self.tablaFigura[7][6] = "/ "
                    self.tablaFigura[7][5] = "/ "
                    self.tablaFigura[7][4] = "K "
                    self.tablaFigura[7][7] = "R "
                elif polje1 == (7, 4) and polje2 == (7, 0):
                    self.tablaFigura[7][2] = "/ "
                    self.tablaFigura[7][3] = "/ "
                    self.tablaFigura[7][4] = "K "
                    self.tablaFigura[7][1] = "/ "
                    self.tablaFigura[7][0] = "R "
                else:
                    self.tablaFigura[polje2[0]][polje2[1]] = tipFigure2
                    self.tablaFigura[polje1[0]][polje1[1]] = tipFigure1
            elif tipFigure1 == "k ":
                if polje1 == (0, 4) and polje2 == (0, 7):
                    self.tablaFigura[0][6] = "/ "
                    self.tablaFigura[0][5] = "/ "
                    self.tablaFigura[0][4] = "k "
                    self.tablaFigura[0][7] = "r "
                elif polje1 == (0, 4) and polje2 == (0, 0):
                    self.tablaFigura[0][2] = "/ "
                    self.tablaFigura[0][3] = "/ "
                    self.tablaFigura[0][4] = "k "
                    self.tablaFigura[0][1] = "/ "
                    self.tablaFigura[0][0] = "r "
                else:
                    self.tablaFigura[polje2[0]][polje2[1]] = tipFigure2
                    self.tablaFigura[polje1[0]][polje1[1]] = tipFigure1
            else:
                self.tablaFigura[polje2[0]][polje2[1]] = tipFigure2
                self.tablaFigura[polje1[0]][polje1[1]] = tipFigure1
            self.brojPoluPoteza -= 1
            self.brojPoteza = self.brojPoluPoteza // 2