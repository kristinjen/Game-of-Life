"""
Dette programmet definerer klassen Celle. Objekter av klassen Celle har kun en 
instansvariabel, og den viser cellens status. Objektene er i utgangspunktet
"døde", og derfor er denne variabelen satt til 0. Cellene har to mulige
statuser, levende og død. Det er to metoder for å endre cellens status, enn som 
endrer statusen til levende, og en som endrer den til død. I tillegg er det to 
metoder for å hente cellens status. Den ene representerer statusen som True
eller False, den andre som bokstaven O(levende) eller punktum (død). Objektene 
av denne klassen er det som utgjør elementene på spillebrettet i simuleringen
Game of Life. 

"""

class Celle:
    def __init__ (self):        #konstruktør med instansvariabelen status
        self._status = 0        #cellen har 0 som utgangspunkt, altså død
    
    def settDoed(self):                 #endrer status til død
        self._status = 0
        
    def settLevende(self):              #endrer status til levende
        self._status = 1
    
    def erLevende(self):                #henter status på boolsk format
        if self._status == 1:           # True (levende) eller False (død)
            return True
        if self._status == 0:
            return False
    
    def hentStatusTegn(self):           #henter status i tegnformat
        if self.erLevende() == True:    #O for levende og . for død
            return "O"
        else:
            return "."