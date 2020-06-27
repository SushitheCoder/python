from random import randint
from celle import Celle
import os

class Spillebrett:
    def __init__ (self , rader , kolonner):
        self._rader = rader
        self._kolonner = kolonner

        self._rutenett = [[Celle() for j in range(self._kolonner)]
                                   for i in range(self._rader)]
        #for i in range(self._rader):
        #    rad = [] * self._kolonner
        #for i in range(self._rader):
        #    for j in range(self._kolonner):
        #        kolon = []
        #self._rutenett.append(rad)
        #self._rutenett.append(kolon)
        #for elementer in self._rutenett:
        #    Celle()
        self._generasjonsnummer = 0
        self.generer()
        
    def tegnBrett(self):
        #Dette er koden jeg fant på nettet for å tømme skjermen før et nytt brett
#        os.system('clear')
        for i in range(self._rader):
            print()
            for j in range(self._kolonner):
                print(self._rutenett[i][j].hentStatusTegn() , end = " ")
        #Jeg valgte å kalle 'oppdatering' her for å forberede brettet for neste runden
#        self._rutenett[i][j].oppdatering()
        Spillebrett.oppdatering(self)
                
    def oppdatering(self):
        #To tomme lister for celle-endring fra død til levende og levende til død
        doed_levende = []
        levende_doed = []
        #Her trekker det funksjonen 'erLevende' fra kodefilen celle.py for å sjekke hver celle sin status om den er levende eller ikke og returnere verdi basert av det
        for i in range(self._rader):
            for j in range(self._kolonner):
                status = self._rutenett[i][j].erLevende()
                naboLevende = 0
                for nabo in self.finnNabo(i,j):
                    levendeNabo = nabo.erLevende()
                    if levendeNabo == True:
                        naboLevende += 1
                #Her følger jeg bare reglene eller lover fra det originale spillet 'Conway's Game of Life'
                if status == True:
                    if naboLevende < 2 or naboLevende > 3:
                        levende_doed.append(self._rutenett[i][j])
                elif status == False:                   
                    if naboLevende == 3:
                        doed_levende.append(self._rutenett[i][j])

        #Status til cellene i listene blir forandret på grunn av reglene fra tidligere
        for celle in doed_levende:
            celle.settLevende()
        for celle in levende_doed:
            celle.settDoed()

        #Legger til generasjonsnummer
        self._generasjonsnummer += 1
        return self._generasjonsnummer


    #Dette teller og holder bare kontroll på antall levende celle på brettet
    def finnAntallLevende(self):
        antallLevende = 0
        for i in range(self._rader):
            for j in range(self._kolonner):
                if self._rutenett[i][j].erLevende():
                   antallLevende += 1
        return antallLevende

    #Denne metoden setter tilfeldig celle til levende for startpunktet og utgjør utgangspunktet for spillet ("generasjon 0")
    def generer(self):
        for i in range (self._rader):
            for j in range (self._kolonner):
                rand = randint(0,2)
                if rand == 2:
                    self._rutenett[i][j].settLevende()

    #Dette finner de åtte naboene rundt en bestemt celle på rutenettet
    def finnNabo(self , x , y):
        naboliste = []
        for i in range (-1 , 2):
            for j in range (-1 , 2):
                naboX = x+i
                naboY = y+j
                if (naboX == x and naboY == y) != True:
                    if (naboX < 0 or naboY < 0 or naboX > self._rader-1 or naboY > self._kolonner-1) != True:
                        naboliste.append(self._rutenett[naboX][naboY])
        return naboliste
        
        
