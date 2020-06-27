from spillebrett import Spillebrett

#hovedprogrammet
def main():
    antallRader = int(input("Oppgi rader på rutenettet: "))
    antallKolonner = int(input("Oppgi kolonner på rutenettet: "))
    brett = Spillebrett(antallRader , antallKolonner)
    #Denne def funksjonen er for at jeg trenger ikke å skrive de samme kodene om igjen senere i filen
    def tegning():
        #Her bør rutenettet skrives ut og oppgir antall generasjoner og levende celler
        brett.tegnBrett()
        def hentGenerasjonsnummer():
            gen = brett._generasjonsnummer
            return gen
        hentGenerasjonsnummer()
        print()
        print("Generasjon: " + str(hentGenerasjonsnummer()) + " — " + "Antall levende celler: " + str(brett.finnAntallLevende()))
    tegning()
    #brukeren velger hvilken de vil velge selv, om de vil programmet skal forsette eller ikke
    trykk = input("Press enter for aa forsette. Skriv inn q og trykk enter for aa avslutte: ")
    while trykk != "q":
#         if trykk == "\n":
           tegning()
           trykk = input("Press enter for aa forsette. Skriv inn q og trykk enter for aa avslutte: ")
    

#Kaller på funksjonen 'main()'
main()


