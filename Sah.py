from Tabla import Tabla
from Potez import Potez
from Engine import Engine
import pygame as p

WIDTH = HEIGHT = 512
DIMENSION = 8
SQ_SIZE = HEIGHT // DIMENSION
MAX_FPS = 15
IMAGES = {}

def ucitajSlike():
    figure = ["wp", "wR", "wN", "wB", "wK", "wQ", "p ", "k ", "n ", "b ", "r ", "q "]
    for figura in figure:
        IMAGES[figura] = p.transform.scale(p.image.load("images/" + figura + ".png"), (SQ_SIZE-1, SQ_SIZE-1))


def nacrtajIgru(ekran, tabla, red, kol, indikator, legalniPotezi):
    nacrtajTablu(ekran)
    obojiLegalnaPolja(ekran, red, kol, indikator, legalniPotezi)
    nacrtajFigure(ekran, tabla.tablaFigura)


def nacrtajTablu(ekran):
    boje = [p.Color("white"), p.Color("gray")]
    for r in range(DIMENSION):
        for k in range(DIMENSION):
            boja = boje[((r+k)%2)]
            p.draw.rect(ekran, boja, p.Rect(k * SQ_SIZE, r*SQ_SIZE, SQ_SIZE, SQ_SIZE))


def obojiLegalnaPolja(ekran, red, kol, indikator, legalniPotezi):
    if (indikator):
        p.draw.rect(ekran, p.Color("green"), p.Rect(kol * SQ_SIZE, red * SQ_SIZE, SQ_SIZE, SQ_SIZE))
        for potez in legalniPotezi:
            red2 = potez.getRedKol()[0]
            kol2 = potez.getRedKol()[1]
            p.draw.circle(ekran, p.Color("lightgreen"), (kol2 * SQ_SIZE + SQ_SIZE/2, red2 * SQ_SIZE + SQ_SIZE/2), 10)

def nacrtajFigure(ekran, tablaFigura):
    for r in range(DIMENSION):
        for k in range(DIMENSION):
            figura = tablaFigura[r][k]
            if figura != "/ ":
                if(figura == "B "):
                    ekran.blit(IMAGES["wB"], p.Rect(k * SQ_SIZE, r * SQ_SIZE, SQ_SIZE, SQ_SIZE))
                elif(figura == "N "):
                    ekran.blit(IMAGES["wN"], p.Rect(k * SQ_SIZE, r * SQ_SIZE, SQ_SIZE, SQ_SIZE))
                elif(figura == "P "):
                    ekran.blit(IMAGES["wp"], p.Rect(k * SQ_SIZE, r * SQ_SIZE, SQ_SIZE, SQ_SIZE))
                elif(figura == "K "):
                    ekran.blit(IMAGES["wK"], p.Rect(k * SQ_SIZE, r * SQ_SIZE, SQ_SIZE, SQ_SIZE))
                elif(figura == "Q "):
                    ekran.blit(IMAGES["wQ"], p.Rect(k * SQ_SIZE, r * SQ_SIZE, SQ_SIZE, SQ_SIZE))
                elif(figura == "R "):
                    ekran.blit(IMAGES["wR"], p.Rect(k * SQ_SIZE, r * SQ_SIZE, SQ_SIZE, SQ_SIZE))
                else:
                    ekran.blit(IMAGES[figura], p.Rect(k * SQ_SIZE, r * SQ_SIZE, SQ_SIZE, SQ_SIZE))


def main():
    defaultFEN = "rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1"
    p.init()
    ekran = p.display.set_mode((WIDTH, HEIGHT))
    clock = p.time.Clock()
    ekran.fill(p.Color("white"))
    tabla = Tabla(defaultFEN)
    engine = Engine(tabla)
    radi = True
    ucitajSlike()
    klikLog = []
    kliknutoPolje = ()
    indikatorDaSvetliPolje = False
    red = 0
    kol = 0
    legalniPoteziFigure = []
    sviLegalniPotezi = []
    
    while radi:
        for e in p.event.get():
            if e.type == p.QUIT:
                radi = False
            elif e.type == p.MOUSEBUTTONDOWN:
                location = p.mouse.get_pos()
                kol = location[0]//SQ_SIZE
                red = location[1]//SQ_SIZE
                if klikLog:
                    if kliknutoPolje == (red , kol):
                        indikatorDaSvetliPolje = False
                    else:
                        #print(tabla.getRokade())
                        tipFigure = tabla.getFigura(kliknutoPolje[0], kliknutoPolje[1])
                        if tipFigure == "P " and red == 0 and Potez(kliknutoPolje[0], kliknutoPolje[1], red, kol, "Q ") in sviLegalniPotezi:
                            #print("usao")
                            tabla = engine.napraviPotezPomocna(tabla, Potez(kliknutoPolje[0], kliknutoPolje[1], red, kol, "Q "), sviLegalniPotezi)
                        elif tipFigure == "p " and red == 7 and Potez(kliknutoPolje[0], kliknutoPolje[1], red, kol, "q ") in sviLegalniPotezi:
                            tabla = engine.napraviPotezPomocna(tabla, Potez(kliknutoPolje[0], kliknutoPolje[1], red, kol, "Q "), sviLegalniPotezi)
                        elif Potez(kliknutoPolje[0], kliknutoPolje[1], red, kol) in sviLegalniPotezi:
                            tabla = engine.napraviPotezPomocna(tabla, Potez(kliknutoPolje[0], kliknutoPolje[1], red, kol), sviLegalniPotezi)
                    klikLog = []
                else:
                    sviLegalniPotezi = engine.generisiPotezeBoje(tabla)
                    print(len(sviLegalniPotezi))
                    #print(sviLegalniPotezi)
                    legalniPoteziFigure = engine.generisiPotezeFigure(tabla, red, kol)
                    klikLog.append(1)
                    kliknutoPolje = (red, kol)
                    indikatorDaSvetliPolje = True
    
            elif e.type == p.KEYDOWN:
                if e.key == p.K_BACKSPACE:
                    tabla.undoPotez()
        nacrtajIgru(ekran, tabla, red, kol, indikatorDaSvetliPolje, legalniPoteziFigure)
        clock.tick(MAX_FPS)
        p.display.flip()



if __name__ == "__main__":
    main()