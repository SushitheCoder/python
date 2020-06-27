class Celle:
    #Constuctor
    #Dette setter startstatus som "død"
    def __init__(self):
        self._status = "doed"
    #Endre status
    def settDoed(self):
        self._status = "doed"
    def settLevende(self):
        self._status = "levende"
    #Hente status
    #Dette returnerre verdien til status som True dersom 'self'(cellen) er levende, og som False dersom cellen er død
    def erLevende(self):
        if self._status == "levende":
            return True
        else:
            return False
    #Det viser hvordan rutenettet kommer til å visualisere seg, med symbol 'O' og '.' å representere hver celle sin status
    def hentStatusTegn(self):
        if self._status == "levende":
            return "O"
        elif self._status == "doed":
            return "."
